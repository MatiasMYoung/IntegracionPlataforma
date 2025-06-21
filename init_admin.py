from app import create_app, db
from app.models import User

def init_admin():
    app = create_app()
    with app.app_context():
        # Verificar si ya existe un administrador
        admin = User.query.filter_by(is_admin=True).first()
        if admin:
            print(f"Ya existe un administrador: {admin.username}")
            return
        
        # Crear usuario administrador
        admin = User(
            username='admin',
            email='admin@salfarent.com',
            is_admin=True
        )
        admin.set_password('admin123')
        
        db.session.add(admin)
        db.session.commit()
        
        print("Usuario administrador creado exitosamente:")
        print(f"Usuario: admin")
        print(f"Contraseña: admin123")
        print("¡IMPORTANTE! Cambia la contraseña después del primer inicio de sesión.")

if __name__ == '__main__':
    init_admin() 