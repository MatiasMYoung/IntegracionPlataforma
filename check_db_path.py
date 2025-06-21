from app import create_app
import os

def check_db_path():
    app = create_app()
    print("\n=== Configuración de la base de datos ===")
    print(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    
    # Obtener la ruta absoluta del archivo de la base de datos
    db_path = app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')
    print(f"\nRuta absoluta de la base de datos: {os.path.abspath(db_path)}")
    print(f"¿Existe el archivo?: {os.path.exists(db_path)}")
    
    if os.path.exists(db_path):
        print(f"Tamaño del archivo: {os.path.getsize(db_path)} bytes")
        print(f"Última modificación: {os.path.getmtime(db_path)}")

if __name__ == '__main__':
    check_db_path() 