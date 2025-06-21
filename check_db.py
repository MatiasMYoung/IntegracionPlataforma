from app import create_app, db
from app.models import Vehicle

def check_database():
    app = create_app()
    with app.app_context():
        # Obtener todos los vehículos
        vehicles = Vehicle.query.all()
        
        print("\n=== Vehículos en la base de datos ===")
        print(f"Total de registros: {len(vehicles)}")
        
        print("\nVehículos de pasajeros:")
        for v in vehicles:
            if v.category == 'vehiculo':
                print(f"- {v.name} {v.model} ({v.year}) - ${v.price_per_day}/día")
        
        print("\nMaquinaria:")
        for v in vehicles:
            if v.category == 'maquinaria':
                print(f"- {v.name} {v.model} ({v.year}) - ${v.price_per_day}/día")

if __name__ == '__main__':
    check_database() 