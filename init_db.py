from app import create_app, db
from app.models import Vehicle

import random
import os

def init_db():
    app = create_app()
    with app.app_context():
        # Forzar la eliminación y recreación de todas las tablas
        db.drop_all()
        db.create_all()

        # Vehículos de pasajeros (versión económica)
        vehiculos = [
            Vehicle(
                name='Hyundai Grand i10',
                model='Active',
                year=random.randint(2020, 2024),
                fuel_efficiency=18.5,
                price_per_day=450.00,
                category='vehiculo',
                description='Compacto económico y eficiente, perfecto para la ciudad.',
                image_url='hyundai_grand_i10.jpg'
            ),
            Vehicle(
                name='Kia Rio',
                model='EX',
                year=random.randint(2020, 2024),
                fuel_efficiency=16.8,
                price_per_day=500.00,
                category='vehiculo',
                description='Sedán moderno con excelente equipamiento y confort.',
                image_url='kia_rio.jpg'
            ),
            Vehicle(
                name='Fiat Cronos',
                model='Precision',
                year=random.randint(2020, 2024),
                fuel_efficiency=15.2,
                price_per_day=480.00,
                category='vehiculo',
                description='Sedán espacioso con excelente relación precio-calidad.',
                image_url='fiat_cronos.jpg'
            ),
            Vehicle(
                name='Volkswagen Voyage',
                model='Highline',
                year=random.randint(2020, 2024),
                fuel_efficiency=14.8,
                price_per_day=520.00,
                category='vehiculo',
                description='Sedán confiable y robusto, ideal para viajes largos.',
                image_url='volkswagen_voyage.jpg'
            ),
            Vehicle(
                name='Hyundai i20',
                model='Elite',
                year=random.randint(2020, 2024),
                fuel_efficiency=17.2,
                price_per_day=470.00,
                category='vehiculo',
                description='Hatchback ágil y económico, perfecto para la ciudad.',
                image_url='hyundai_i20.jpg'
            ),
            Vehicle(
                name='Suzuki Swift',
                model='GLX',
                year=random.randint(2020, 2024),
                fuel_efficiency=18.5,
                price_per_day=460.00,
                category='vehiculo',
                description='Hatchback deportivo y eficiente, ideal para uso urbano.',
                image_url='suzuki_swift.jpg'
            )
        ]

        # Maquinaria (selección aleatoria de 10 unidades)
        maquinaria_options = [
            # Camionetas Pickup
            {
                'name': 'Toyota Hilux',
                'model': 'SRX',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 10.5,
                'price': 800.00,
                'description': 'Pickup robusta y confiable, ideal para trabajo pesado.',
                'image_url': 'toyota_hilux.jpg'
            },
            {
                'name': 'Ford Ranger',
                'model': 'Wildtrak',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 9.8,
                'price': 850.00,
                'description': 'Pickup versátil con gran capacidad de carga.',
                'image_url': 'ford_ranger.jpg'
            },
            {
                'name': 'Mitsubishi L200',
                'model': 'Triton',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 10.2,
                'price': 780.00,
                'description': 'Pickup resistente para todo tipo de terrenos.',
                'image_url': 'mitsubishi_l200.jpg'
            },
            # Furgones
            {
                'name': 'Mercedes-Benz Sprinter',
                'model': '515',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 8.5,
                'price': 1200.00,
                'description': 'Furgón de carga con amplio espacio interior.',
                'image_url': 'mercedes_benz_sprinter.jpg'
            },
            {
                'name': 'Hyundai H1',
                'model': 'Cargo',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 9.2,
                'price': 1100.00,
                'description': 'Furgón versátil para carga y pasajeros.',
                'image_url': 'hyundai_h1.jpg'
            },
            # Camiones
            {
                'name': 'Scania Serie R',
                'model': 'R500',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 6.5,
                'price': 2500.00,
                'description': 'Tractocamión de alto rendimiento para largas distancias.',
                'image_url': 'scania_serie_r.jpg'
            },
            {
                'name': 'Volvo FH',
                'model': 'FH16',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 6.8,
                'price': 2600.00,
                'description': 'Tractocamión premium con máxima eficiencia.',
                'image_url': 'volvo_fh.jpg'
            },
            {
                'name': 'Mercedes-Benz Actros',
                'model': '2545',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 7.0,
                'price': 2400.00,
                'description': 'Camión de carga pesada con tecnología avanzada.',
                'image_url': 'mercedes_benz_actros.jpg'
            },
            # Buses
            {
                'name': 'Marcopolo Paradiso',
                'model': 'G7',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 5.5,
                'price': 3000.00,
                'description': 'Bus de larga distancia con máximo confort.',
                'image_url': 'marcopolo_paradiso.jpg'
            },
            {
                'name': 'Volvo B8RLE',
                'model': 'City',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 6.0,
                'price': 2800.00,
                'description': 'Bus urbano con bajo consumo y alta eficiencia.',
                'image_url': 'volvo_b8rle.jpg'
            },
            # Maquinaria Especializada
            {
                'name': 'Liebherr',
                'model': 'LTM 1100',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 4.5,
                'price': 5000.00,
                'description': 'Grúa móvil de alta capacidad para proyectos especiales.',
                'image_url': 'liebherr_ltm_1100.jpg'
            },
            {
                'name': 'Mercedes-Benz Arocs',
                'model': '3245',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 5.8,
                'price': 3500.00,
                'description': 'Camión volquete para construcción y minería.',
                'image_url': 'mercedes_benz_arocs.jpg'
            },
            {
                'name': 'MAN TGS',
                'model': '35.510',
                'year': random.randint(2020, 2024),
                'fuel_efficiency': 6.2,
                'price': 3200.00,
                'description': 'Camión hormigonero para proyectos de construcción.',
                'image_url': 'man_tgs.jpg'
            }
        ]

        # Seleccionar 10 unidades de maquinaria aleatoriamente
        maquinaria_seleccionada = random.sample(maquinaria_options, 10)
        
        # Crear objetos Vehicle para la maquinaria seleccionada
        maquinaria = [
            Vehicle(
                name=item['name'],
                model=item['model'],
                year=item['year'],
                fuel_efficiency=item['fuel_efficiency'],
                price_per_day=item['price'],
                category='maquinaria',
                description=item['description'],
                image_url=item['image_url']
            ) for item in maquinaria_seleccionada
        ]

        # Agregar todos los vehículos a la base de datos
        for vehicle in vehiculos + maquinaria:
            db.session.add(vehicle)
        
        # Guardar cambios
        db.session.commit()
        print("Base de datos reinicializada con vehículos y maquinaria de ejemplo.")

if __name__ == '__main__':
    init_db() 