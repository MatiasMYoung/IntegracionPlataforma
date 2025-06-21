#!/usr/bin/env python3
"""
Script para actualizar la base de datos con los nuevos campos
de notificaciones y cancelación de reservas.
"""

from app import create_app, db
from app.models import Reservation, Notification

def update_database():
    app = create_app()
    
    with app.app_context():
        print("🔄 Actualizando esquema de base de datos...")
        
        try:
            # Crear las nuevas tablas
            db.create_all()
            print("✅ Tablas creadas/actualizadas exitosamente")
            
            # Verificar si hay reservas existentes y actualizar su estado
            reservas = Reservation.query.all()
            for reserva in reservas:
                if not hasattr(reserva, 'status') or reserva.status is None:
                    reserva.status = 'pending'
                if not hasattr(reserva, 'cancelled_by_admin'):
                    reserva.cancelled_by_admin = False
                if not hasattr(reserva, 'started_at'):
                    reserva.started_at = None
                if not hasattr(reserva, 'completed_at'):
                    reserva.completed_at = None
            
            db.session.commit()
            print(f"✅ {len(reservas)} reservas actualizadas")
            
            print("\n🎉 Base de datos actualizada exitosamente!")
            print("📋 Nuevas funcionalidades disponibles:")
            print("   - Sistema de notificaciones")
            print("   - Cancelación de reservas por administrador")
            print("   - Estados de reservas (pending, confirmed, cancelled, completed)")
            print("   - Motivos de cancelación")
            
        except Exception as e:
            print(f"❌ Error al actualizar la base de datos: {e}")
            db.session.rollback()

if __name__ == '__main__':
    update_database() 