from app import create_app, db
from app.models import Vehicle

def init_sample_data():
    app = create_app()
    with app.app_context():
        # Verificar si ya existen vehículos
        existing_vehicles = Vehicle.query.count()
        if existing_vehicles > 0:
            print(f"Ya existen {existing_vehicles} vehículos en la base de datos.")
            return
        
        # Crear vehículos de ejemplo
        vehicles_data = [
            # Vehículos
            {
                'name': 'Hyundai',
                'model': 'Grand i10',
                'year': 2022,
                'fuel_efficiency': 18.5,
                'price_per_day': 25000,
                'category': 'vehiculo',
                'description': 'Auto compacto ideal para ciudad, económico y fácil de manejar.',
                'image_url': 'hyundai_grand_i10.jpg',
                'available': True
            },
            {
                'name': 'Kia',
                'model': 'Rio',
                'year': 2021,
                'fuel_efficiency': 17.2,
                'price_per_day': 28000,
                'category': 'vehiculo',
                'description': 'Sedán compacto con excelente relación calidad-precio.',
                'image_url': 'kia_rio.jpg',
                'available': True
            },
            {
                'name': 'Fiat',
                'model': 'Cronos',
                'year': 2023,
                'fuel_efficiency': 16.8,
                'price_per_day': 32000,
                'category': 'vehiculo',
                'description': 'Sedán mediano con amplio espacio interior y confort.',
                'image_url': 'fiat_cronos.jpg',
                'available': True
            },
            {
                'name': 'Volkswagen',
                'model': 'Voyage',
                'year': 2022,
                'fuel_efficiency': 17.5,
                'price_per_day': 30000,
                'category': 'vehiculo',
                'description': 'Sedán confiable y económico para uso diario.',
                'image_url': 'volkswagen_voyage.jpg',
                'available': True
            },
            {
                'name': 'Hyundai',
                'model': 'i20',
                'year': 2023,
                'fuel_efficiency': 19.2,
                'price_per_day': 27000,
                'category': 'vehiculo',
                'description': 'Hatchback moderno con tecnología avanzada.',
                'image_url': 'hyundai_i20.jpg',
                'available': True
            },
            {
                'name': 'Suzuki',
                'model': 'Swift',
                'year': 2022,
                'fuel_efficiency': 18.8,
                'price_per_day': 26000,
                'category': 'vehiculo',
                'description': 'Hatchback deportivo y ágil para ciudad.',
                'image_url': 'suzuki_swift.jpg',
                'available': True
            },
            {
                'name': 'Ford',
                'model': 'Ranger',
                'year': 2021,
                'fuel_efficiency': 12.5,
                'price_per_day': 45000,
                'category': 'vehiculo',
                'description': 'Pickup robusta para trabajo y aventura.',
                'image_url': 'ford_ranger.jpg',
                'available': True
            },
            {
                'name': 'Hyundai',
                'model': 'H1',
                'year': 2022,
                'fuel_efficiency': 11.8,
                'price_per_day': 55000,
                'category': 'vehiculo',
                'description': 'Van espaciosa para grupos y transporte.',
                'image_url': 'hyundai_h1.jpg',
                'available': True
            },
            {
                'name': 'Mitsubishi',
                'model': 'L200',
                'year': 2021,
                'fuel_efficiency': 13.2,
                'price_per_day': 48000,
                'category': 'vehiculo',
                'description': 'Pickup todoterreno para trabajo pesado.',
                'image_url': 'mitsubishi_l200.jpg',
                'available': True
            },
            
            # Maquinaria
            {
                'name': 'Liebherr',
                'model': 'LTM 1100',
                'year': 2020,
                'fuel_efficiency': 8.5,
                'price_per_day': 180000,
                'category': 'maquinaria',
                'description': 'Grúa telescópica móvil de 100 toneladas.',
                'image_url': 'liebherr_ltm_1100.jpg',
                'available': True
            },
            {
                'name': 'MAN',
                'model': 'TGS',
                'year': 2021,
                'fuel_efficiency': 9.2,
                'price_per_day': 120000,
                'category': 'maquinaria',
                'description': 'Camión de carga pesada para construcción.',
                'image_url': 'man_tgs.jpg',
                'available': True
            },
            {
                'name': 'Volvo',
                'model': 'FH',
                'year': 2022,
                'fuel_efficiency': 10.1,
                'price_per_day': 140000,
                'category': 'maquinaria',
                'description': 'Tractocamión de alta tecnología y eficiencia.',
                'image_url': 'volvo_fh.jpg',
                'available': True
            },
            {
                'name': 'Mercedes-Benz',
                'model': 'Actros',
                'year': 2021,
                'fuel_efficiency': 9.8,
                'price_per_day': 150000,
                'category': 'maquinaria',
                'description': 'Camión de alta gama para transporte pesado.',
                'image_url': 'mercedes_benz_actros.jpg',
                'available': True
            },
            {
                'name': 'Mercedes-Benz',
                'model': 'Arocs',
                'year': 2022,
                'fuel_efficiency': 8.9,
                'price_per_day': 160000,
                'category': 'maquinaria',
                'description': 'Camión de construcción robusto y confiable.',
                'image_url': 'mercedes_benz_arocs.jpg',
                'available': True
            },
            {
                'name': 'Mercedes-Benz',
                'model': 'Sprinter',
                'year': 2023,
                'fuel_efficiency': 14.5,
                'price_per_day': 85000,
                'category': 'maquinaria',
                'description': 'Furgón comercial versátil para logística.',
                'image_url': 'mercedes_benz_sprinter.jpg',
                'available': True
            },
            {
                'name': 'Marcopolo',
                'model': 'Paradiso',
                'year': 2021,
                'fuel_efficiency': 7.8,
                'price_per_day': 95000,
                'category': 'maquinaria',
                'description': 'Bus de pasajeros de lujo para turismo.',
                'image_url': 'marcopolo_paradiso.jpg',
                'available': True
            },
            {
                'name': 'Volvo',
                'model': 'B8RLE',
                'year': 2022,
                'fuel_efficiency': 8.2,
                'price_per_day': 110000,
                'category': 'maquinaria',
                'description': 'Bus urbano de alta capacidad y eficiencia.',
                'image_url': 'volvo_b8rle.jpg',
                'available': True
            }
        ]
        
        # Agregar vehículos a la base de datos
        for vehicle_data in vehicles_data:
            vehicle = Vehicle(**vehicle_data)
            db.session.add(vehicle)
        
        db.session.commit()
        print(f"Se han creado {len(vehicles_data)} vehículos de ejemplo en la base de datos.")

if __name__ == '__main__':
    init_sample_data() 