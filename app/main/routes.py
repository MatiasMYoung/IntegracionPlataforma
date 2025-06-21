from flask import render_template, flash, redirect, url_for, request, jsonify
from app.main import bp
from app.models import Vehicle, User, Reservation, Notification
from app import db
import os
from app.utils.currency import convert_to_uf, convert_to_usd, format_currency
from flask_login import login_required, current_user, login_user, logout_user
from datetime import datetime, date, timedelta

@bp.route('/')
@bp.route('/index')
def index():
    vehicles = Vehicle.query.filter_by(available=True).all()
    return render_template('index.html', title='Inicio', vehicles=vehicles)

@bp.route('/vehiculos')
def vehiculos():
    vehicles = Vehicle.query.filter_by(category='vehiculo', available=True).all()
    return render_template('vehiculos.html', title='Vehículos', vehicles=vehicles, today=date.today().isoformat())

@bp.route('/maquinaria')
def maquinaria():
    machinery = Vehicle.query.filter_by(category='maquinaria', available=True).all()
    return render_template('maquinaria.html', title='Maquinaria', vehicles=machinery, today=date.today().isoformat())

@bp.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('Acceso restringido solo para administradores.', 'danger')
        return redirect(url_for('main.index'))
    vehiculos = Vehicle.query.filter_by(category='vehiculo').all()
    maquinaria = Vehicle.query.filter_by(category='maquinaria').all()
    return render_template('admin.html', vehiculos=vehiculos, maquinaria=maquinaria)

@bp.route('/admin/usuarios')
@login_required
def admin_usuarios():
    if not current_user.is_admin:
        flash('Acceso restringido solo para administradores.', 'danger')
        return redirect(url_for('main.index'))
    usuarios = User.query.all()
    reservas = Reservation.query.order_by(Reservation.created_at.desc()).all()
    return render_template('admin_usuarios.html', usuarios=usuarios, reservas=reservas)

@bp.route('/mis_reservas')
@login_required
def mis_reservas():
    # Obtener reservas del usuario ordenadas por fecha de creación
    reservas = current_user.reservations.order_by(Reservation.created_at.desc()).all()
    return render_template('mis_reservas.html', reservas=reservas)

# --- CRUD VEHÍCULOS ---
@bp.route('/vehiculos/add', methods=['GET', 'POST'])
def add_vehiculo():
    img_folder = os.path.join('app', 'static', 'img')
    images = [f for f in os.listdir(img_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if request.method == 'POST':
        v = Vehicle(
            name=request.form['name'],
            model=request.form['model'],
            year=int(request.form['year']),
            fuel_efficiency=float(request.form['fuel_efficiency']),
            price_per_day=float(request.form['price_per_day']),
            category='vehiculo',
            description=request.form['description'],
            image_url=request.form['image_url']
        )
        db.session.add(v)
        db.session.commit()
        flash('Vehículo agregado correctamente', 'success')
        return redirect(url_for('main.vehiculos'))
    return render_template('vehiculo_form.html', images=images, action='Agregar', vehiculo=None)

@bp.route('/vehiculos/edit/<int:id>', methods=['GET', 'POST'])
def edit_vehiculo(id):
    vehiculo = Vehicle.query.get_or_404(id)
    img_folder = os.path.join('app', 'static', 'img')
    images = [f for f in os.listdir(img_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if request.method == 'POST':
        vehiculo.name = request.form['name']
        vehiculo.model = request.form['model']
        vehiculo.year = int(request.form['year'])
        vehiculo.fuel_efficiency = float(request.form['fuel_efficiency'])
        vehiculo.price_per_day = float(request.form['price_per_day'])
        vehiculo.description = request.form['description']
        vehiculo.image_url = request.form['image_url']
        db.session.commit()
        flash('Vehículo actualizado correctamente', 'success')
        return redirect(url_for('main.vehiculos'))
    return render_template('vehiculo_form.html', images=images, action='Editar', vehiculo=vehiculo)

@bp.route('/vehiculos/delete/<int:id>', methods=['POST'])
def delete_vehiculo(id):
    vehiculo = Vehicle.query.get_or_404(id)
    db.session.delete(vehiculo)
    db.session.commit()
    flash('Vehículo eliminado correctamente', 'success')
    return redirect(url_for('main.vehiculos'))

# --- CRUD MAQUINARIA ---
@bp.route('/maquinaria/add', methods=['GET', 'POST'])
def add_maquinaria():
    img_folder = os.path.join('app', 'static', 'img')
    images = [f for f in os.listdir(img_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if request.method == 'POST':
        m = Vehicle(
            name=request.form['name'],
            model=request.form['model'],
            year=int(request.form['year']),
            fuel_efficiency=float(request.form['fuel_efficiency']),
            price_per_day=float(request.form['price_per_day']),
            category='maquinaria',
            description=request.form['description'],
            image_url=request.form['image_url']
        )
        db.session.add(m)
        db.session.commit()
        flash('Maquinaria agregada correctamente', 'success')
        return redirect(url_for('main.maquinaria'))
    return render_template('maquinaria_form.html', images=images, action='Agregar', maquinaria=None)

@bp.route('/maquinaria/edit/<int:id>', methods=['GET', 'POST'])
def edit_maquinaria(id):
    maquinaria = Vehicle.query.get_or_404(id)
    img_folder = os.path.join('app', 'static', 'img')
    images = [f for f in os.listdir(img_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    if request.method == 'POST':
        maquinaria.name = request.form['name']
        maquinaria.model = request.form['model']
        maquinaria.year = int(request.form['year'])
        maquinaria.fuel_efficiency = float(request.form['fuel_efficiency'])
        maquinaria.price_per_day = float(request.form['price_per_day'])
        maquinaria.description = request.form['description']
        maquinaria.image_url = request.form['image_url']
        db.session.commit()
        flash('Maquinaria actualizada correctamente', 'success')
        return redirect(url_for('main.maquinaria'))
    return render_template('maquinaria_form.html', images=images, action='Editar', maquinaria=maquinaria)

@bp.route('/maquinaria/delete/<int:id>', methods=['POST'])
def delete_maquinaria(id):
    maquinaria = Vehicle.query.get_or_404(id)
    db.session.delete(maquinaria)
    db.session.commit()
    flash('Maquinaria eliminada correctamente', 'success')
    return redirect(url_for('main.maquinaria'))

@bp.route('/vehiculos/<int:vehicle_id>/reservar', methods=['POST'])
@login_required
def reservar_vehiculo(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    
    if not vehicle.available:
        flash('Este vehículo no está disponible para reserva.', 'error')
        return redirect(url_for('main.vehiculos'))
    
    start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
    
    # Validaciones
    if start_date < datetime.now():
        flash('La fecha de inicio no puede ser anterior a hoy.', 'error')
        return redirect(url_for('main.vehiculos'))
    
    if end_date <= start_date:
        flash('La fecha de fin debe ser posterior a la fecha de inicio.', 'error')
        return redirect(url_for('main.vehiculos'))
    
    # Calcular días y precio total
    days = (end_date - start_date).days
    total_price = days * vehicle.price_per_day
    
    # Verificar si hay conflictos de reserva
    existing_reservation = Reservation.query.filter(
        Reservation.vehicle_id == vehicle_id,
        Reservation.status.in_(['pending', 'confirmed']),
        Reservation.start_date <= end_date,
        Reservation.end_date >= start_date
    ).first()
    
    if existing_reservation:
        flash('Este vehículo ya está reservado para las fechas seleccionadas.', 'error')
        return redirect(url_for('main.vehiculos'))
    
    # Crear la reserva
    reservation = Reservation(
        user_id=current_user.id,
        vehicle_id=vehicle_id,
        start_date=start_date,
        end_date=end_date,
        total_price=total_price,
        status='pending'
    )
    
    db.session.add(reservation)
    db.session.commit()
    
    flash(f'Reserva creada exitosamente. Total: {format_currency(total_price, "CLP")}', 'success')
    return redirect(url_for('main.mis_reservas'))

@bp.route('/maquinaria/<int:vehicle_id>/reservar', methods=['POST'])
@login_required
def reservar_maquinaria(vehicle_id):
    vehicle = Vehicle.query.get_or_404(vehicle_id)
    
    if not vehicle.available:
        flash('Esta maquinaria no está disponible para reserva.', 'error')
        return redirect(url_for('main.maquinaria'))
    
    start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
    project_location = request.form['project_location']
    
    # Validaciones
    if start_date < datetime.now():
        flash('La fecha de inicio no puede ser anterior a hoy.', 'error')
        return redirect(url_for('main.maquinaria'))
    
    if end_date <= start_date:
        flash('La fecha de fin debe ser posterior a la fecha de inicio.', 'error')
        return redirect(url_for('main.maquinaria'))
    
    # Calcular días y precio total
    days = (end_date - start_date).days
    total_price = days * vehicle.price_per_day
    
    # Verificar si hay conflictos de reserva
    existing_reservation = Reservation.query.filter(
        Reservation.vehicle_id == vehicle_id,
        Reservation.status.in_(['pending', 'confirmed']),
        Reservation.start_date <= end_date,
        Reservation.end_date >= start_date
    ).first()
    
    if existing_reservation:
        flash('Esta maquinaria ya está reservada para las fechas seleccionadas.', 'error')
        return redirect(url_for('main.maquinaria'))
    
    # Crear la reserva
    reservation = Reservation(
        user_id=current_user.id,
        vehicle_id=vehicle_id,
        start_date=start_date,
        end_date=end_date,
        total_price=total_price,
        status='pending'
    )
    
    db.session.add(reservation)
    db.session.commit()
    
    flash(f'Solicitud de maquinaria creada exitosamente. Total: {format_currency(total_price, "CLP")}', 'success')
    return redirect(url_for('main.mis_reservas'))

@bp.route('/admin/reservas')
@login_required
def admin_reservas():
    if not current_user.is_admin:
        flash('Acceso denegado. Solo administradores pueden ver esta página.', 'error')
        return redirect(url_for('main.index'))
    
    # Obtener todas las reservas ordenadas por fecha de creación
    reservas = Reservation.query.order_by(Reservation.created_at.desc()).all()
    return render_template('admin_reservas.html', reservas=reservas)

@bp.route('/admin/reservas/<int:reservation_id>/confirmar', methods=['POST'])
@login_required
def confirmar_reserva(reservation_id):
    if not current_user.is_admin:
        flash('Acceso denegado. Solo administradores pueden confirmar reservas.', 'error')
        return redirect(url_for('main.index'))
    
    reserva = Reservation.query.get_or_404(reservation_id)
    
    if reserva.status != 'pending':
        flash('Solo se pueden confirmar reservas pendientes.', 'error')
        return redirect(url_for('main.admin_reservas'))
    
    # Cambiar estado a confirmada
    reserva.status = 'confirmed'
    
    # Crear notificación para el usuario
    notificacion = Notification(
        user_id=reserva.user_id,
        title='Reserva Confirmada',
        message=f'Su reserva del vehículo "{reserva.vehicle.name}" ha sido confirmada.\n\nPuede retirar el vehículo en la fecha programada: {reserva.start_date.strftime("%d/%m/%Y %H:%M")}',
        type='success'
    )
    
    db.session.add(notificacion)
    db.session.commit()
    
    flash(f'Reserva #{reservation_id} confirmada exitosamente. Se ha enviado una notificación al usuario.', 'success')
    return redirect(url_for('main.admin_reservas'))

@bp.route('/admin/reservas/<int:reservation_id>/iniciar', methods=['POST'])
@login_required
def iniciar_reserva(reservation_id):
    if not current_user.is_admin:
        flash('Acceso denegado. Solo administradores pueden iniciar reservas.', 'error')
        return redirect(url_for('main.index'))
    
    reserva = Reservation.query.get_or_404(reservation_id)
    
    if reserva.status not in ['pending', 'confirmed']:
        flash('Solo se pueden iniciar reservas pendientes o confirmadas.', 'error')
        return redirect(url_for('main.admin_reservas'))
    
    # Cambiar estado a en curso
    reserva.status = 'in_progress'
    reserva.started_at = datetime.utcnow()
    
    # Crear notificación para el usuario
    notificacion = Notification(
        user_id=reserva.user_id,
        title='Uso Iniciado',
        message=f'El uso del vehículo "{reserva.vehicle.name}" ha sido iniciado.\n\nFecha de inicio: {reserva.started_at.strftime("%d/%m/%Y %H:%M")}',
        type='info'
    )
    
    db.session.add(notificacion)
    db.session.commit()
    
    flash(f'Reserva #{reservation_id} iniciada exitosamente. El vehículo está en uso.', 'success')
    return redirect(url_for('main.admin_reservas'))

@bp.route('/admin/reservas/<int:reservation_id>/completar', methods=['POST'])
@login_required
def completar_reserva(reservation_id):
    if not current_user.is_admin:
        flash('Acceso denegado. Solo administradores pueden completar reservas.', 'error')
        return redirect(url_for('main.index'))
    
    reserva = Reservation.query.get_or_404(reservation_id)
    
    if reserva.status != 'in_progress':
        flash('Solo se pueden completar reservas en curso.', 'error')
        return redirect(url_for('main.admin_reservas'))
    
    # Cambiar estado a completada
    reserva.status = 'completed'
    reserva.completed_at = datetime.utcnow()
    
    # Crear notificación para el usuario
    notificacion = Notification(
        user_id=reserva.user_id,
        title='Reserva Completada',
        message=f'El uso del vehículo "{reserva.vehicle.name}" ha sido completado.\n\nFecha de finalización: {reserva.completed_at.strftime("%d/%m/%Y %H:%M")}',
        type='success'
    )
    
    db.session.add(notificacion)
    db.session.commit()
    
    flash(f'Reserva #{reservation_id} completada exitosamente.', 'success')
    return redirect(url_for('main.admin_reservas'))

@bp.route('/admin/reservas/<int:reservation_id>/cancelar', methods=['GET', 'POST'])
@login_required
def cancelar_reserva(reservation_id):
    if not current_user.is_admin:
        flash('Acceso denegado. Solo administradores pueden cancelar reservas.', 'error')
        return redirect(url_for('main.index'))
    
    reserva = Reservation.query.get_or_404(reservation_id)
    
    if request.method == 'POST':
        motivo = request.form.get('motivo', 'Sin motivo especificado')
        
        # Actualizar estado de la reserva
        reserva.status = 'cancelled'
        reserva.cancellation_reason = motivo
        reserva.cancelled_by_admin = True
        reserva.cancelled_at = datetime.utcnow()
        
        # Crear notificación para el usuario
        notificacion = Notification(
            user_id=reserva.user_id,
            title='Reserva Cancelada',
            message=f'Su reserva del vehículo "{reserva.vehicle.name}" ha sido cancelada por el administrador.\n\nMotivo: {motivo}\n\nFecha de cancelación: {reserva.cancelled_at.strftime("%d/%m/%Y %H:%M")}',
            type='warning'
        )
        
        db.session.add(notificacion)
        db.session.commit()
        
        flash(f'Reserva #{reservation_id} cancelada exitosamente. Se ha enviado una notificación al usuario.', 'success')
        return redirect(url_for('main.admin_reservas'))
    
    return render_template('cancelar_reserva.html', reserva=reserva)

@bp.route('/notificaciones')
@login_required
def notificaciones():
    # Obtener notificaciones del usuario ordenadas por fecha
    notificaciones = current_user.notifications.order_by(Notification.created_at.desc()).all()
    return render_template('notificaciones.html', notificaciones=notificaciones)

@bp.route('/notificaciones/<int:notification_id>/marcar-leida')
@login_required
def marcar_notificacion_leida(notification_id):
    notificacion = Notification.query.get_or_404(notification_id)
    
    # Verificar que la notificación pertenece al usuario actual
    if notificacion.user_id != current_user.id:
        flash('Acceso denegado.', 'error')
        return redirect(url_for('main.notificaciones'))
    
    notificacion.read = True
    db.session.commit()
    
    return redirect(url_for('main.notificaciones'))

@bp.route('/notificaciones/marcar-todas-leidas')
@login_required
def marcar_todas_leidas():
    # Marcar todas las notificaciones del usuario como leídas
    current_user.notifications.filter_by(read=False).update({'read': True})
    db.session.commit()
    
    flash('Todas las notificaciones han sido marcadas como leídas.', 'success')
    return redirect(url_for('main.notificaciones'))

@bp.context_processor
def utility_processor():
    def format_currency(amount, currency='CLP'):
        if currency == 'CLP':
            return f"${amount:,.0f} CLP"
        elif currency == 'USD':
            return f"US${amount:,.2f}"
        elif currency == 'UF':
            return f"{amount:,.2f} UF"
        else:
            return f"{amount:,.2f} {currency}"
    
    def nl2br(text):
        if text:
            return text.replace('\n', '<br>')
        return text
    
    return {
        'convert_to_uf': convert_to_uf,
        'convert_to_usd': convert_to_usd,
        'format_currency': format_currency,
        'nl2br': nl2br
    } 