from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con reservas
    reservations = db.relationship('Reservation', backref='user', lazy='dynamic')
    # Relación con notificaciones
    notifications = db.relationship('Notification', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    fuel_efficiency = db.Column(db.Float, nullable=False)  # km/litro
    price_per_day = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 'vehiculo' o 'maquinaria'
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200))
    available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relación con reservas
    reservations = db.relationship('Reservation', backref='vehicle', lazy='dynamic')

    def __repr__(self):
        return f'<Vehicle {self.name} {self.model}>'

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, in_progress, cancelled, completed
    cancellation_reason = db.Column(db.Text)  # Motivo de cancelación
    cancelled_by_admin = db.Column(db.Boolean, default=False)  # Si fue cancelada por admin
    cancelled_at = db.Column(db.DateTime)  # Fecha de cancelación
    started_at = db.Column(db.DateTime)  # Fecha cuando se inició el uso
    completed_at = db.Column(db.DateTime)  # Fecha cuando se completó
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Reservation {self.id} - {self.user.username} - {self.vehicle.name}>'

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(20), default='info')  # info, warning, error, success
    read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Notification {self.id} - {self.user.username} - {self.title}>'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id)) 