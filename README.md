# 🚗 Sistema de Renta de Vehículos y Maquinaria

Un sistema web completo desarrollado en Flask para la gestión de renta de vehículos y maquinaria pesada, con sistema de autenticación, autorización y gestión administrativa.

## 📋 Características

### 👥 Gestión de Usuarios
- **Registro e inicio de sesión** de usuarios
- **Sistema de roles**: Usuarios normales y Administradores
- **Perfil de usuario** con información personal
- **Gestión de contraseñas** segura

### 🚗 Gestión de Vehículos
- **Catálogo de vehículos** con imágenes y detalles
- **Filtros por categoría** (automóviles, camiones, buses)
- **Información detallada**: marca, modelo, año, precio por día
- **Estado de disponibilidad** en tiempo real

### 🏗️ Gestión de Maquinaria
- **Catálogo de maquinaria pesada** con especificaciones técnicas
- **Categorías**: excavadoras, grúas, camiones, buses
- **Información técnica** detallada
- **Estado de disponibilidad** y ubicación

### 📅 Sistema de Reservas
- **Reserva de vehículos y maquinaria** con fechas específicas
- **Estados de reserva**:
  - Pendiente
  - Confirmada
  - En curso
  - Completada
  - Cancelada
- **Seguimiento de fechas** de inicio y finalización
- **Historial de reservas** por usuario

### 🔧 Panel Administrativo
- **Gestión de usuarios** (crear, editar, eliminar)
- **Gestión de reservas** (confirmar, iniciar, completar, cancelar)
- **Notificaciones** automáticas a usuarios
- **Dashboard** con estadísticas

### 💰 Integración Financiera
- **Cálculo automático** de precios en pesos chilenos
- **Integración con API del Banco Central** para tipos de cambio
- **Formato de moneda** localizado

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.x, Flask
- **Base de Datos**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Autenticación**: Flask-Login
- **Formularios**: Flask-WTF
- **APIs**: Banco Central de Chile (mindicador.cl)

## 📦 Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/sistema-renta-vehiculos.git
cd sistema-renta-vehiculos
```

2. **Crear entorno virtual**
```bash
python -m venv venv
```

3. **Activar entorno virtual**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

5. **Configurar la base de datos**
```bash
python init_db.py
```

6. **Crear usuario administrador**
```bash
python init_admin.py
```

7. **Cargar datos de ejemplo (opcional)**
```bash
python init_sample_data.py
```

8. **Ejecutar la aplicación**
```bash
python run.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`

## 🔐 Credenciales por Defecto

### Administrador
- **Usuario**: admin
- **Contraseña**: admin123

### Usuario de Prueba
- **Usuario**: usuario@test.com
- **Contraseña**: password123

## 📁 Estructura del Proyecto

```
Integracion/
├── app/
│   ├── __init__.py          # Configuración de la aplicación Flask
│   ├── models.py            # Modelos de base de datos
│   ├── auth/                # Módulo de autenticación
│   │   ├── __init__.py
│   │   └── routes.py        # Rutas de autenticación
│   ├── main/                # Módulo principal
│   │   ├── __init__.py
│   │   └── routes.py        # Rutas principales
│   ├── static/              # Archivos estáticos
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── templates/           # Plantillas HTML
│   │   ├── auth/
│   │   └── ...
│   └── utils/               # Utilidades
│       ├── currency.py      # Funciones de moneda
│       └── mindicador.py    # Integración con API del Banco Central
├── instance/                # Base de datos SQLite
├── requirements.txt         # Dependencias del proyecto
├── run.py                  # Script de ejecución
├── init_db.py              # Inicialización de base de datos
├── init_admin.py           # Creación de usuario administrador
└── init_sample_data.py     # Carga de datos de ejemplo
```

## 🚀 Funcionalidades Principales

### Para Usuarios
1. **Registro e inicio de sesión**
2. **Explorar catálogo** de vehículos y maquinaria
3. **Realizar reservas** con fechas específicas
4. **Ver historial** de reservas propias
5. **Recibir notificaciones** sobre el estado de sus reservas

### Para Administradores
1. **Gestionar usuarios** del sistema
2. **Administrar reservas** (confirmar, iniciar, completar, cancelar)
3. **Ver estadísticas** del sistema
4. **Enviar notificaciones** a usuarios
5. **Gestionar inventario** de vehículos y maquinaria

## 🔧 Configuración

### Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-clave-secreta-aqui
FLASK_ENV=development
DATABASE_URL=sqlite:///instance/renta.db
```

### Configuración de Base de Datos
El sistema utiliza SQLite por defecto. Para cambiar a otra base de datos, modifica `config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:password@localhost/renta_db'
```

## 📊 API del Banco Central

El sistema integra automáticamente con la API del Banco Central de Chile para obtener tipos de cambio actualizados:

- **Endpoint**: https://mindicador.cl/api
- **Monedas soportadas**: USD, EUR, CLP
- **Actualización automática** de precios

## 🐛 Solución de Problemas

### Error de Importación de Werkzeug
Si encuentras el error `ImportError: cannot import name 'url_parse'`, actualiza la importación en `app/auth/routes.py`:

```python
# Cambiar de:
from werkzeug.urls import url_parse

# A:
from urllib.parse import urlparse as url_parse
```

### Base de Datos Bloqueada
Si la base de datos está bloqueada, elimina el archivo `instance/renta.db` y ejecuta:

```bash
python init_db.py
python init_admin.py
python init_sample_data.py
```

### Imágenes No Cargadas
Asegúrate de que las imágenes estén en la carpeta `app/static/img/` con los nombres correctos.

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Tu Nombre**
- Email: tu-email@ejemplo.com
- GitHub: [@tu-usuario](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- [Flask](https://flask.palletsprojects.com/) - Framework web
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM para Python
- [Banco Central de Chile](https://mindicador.cl/) - API de tipos de cambio
- [Bootstrap](https://getbootstrap.com/) - Framework CSS

## 📞 Soporte

Si tienes alguna pregunta o problema, por favor:

1. Revisa la sección de [Solución de Problemas](#-solución-de-problemas)
2. Busca en los [Issues](https://github.com/tu-usuario/sistema-renta-vehiculos/issues)
3. Crea un nuevo issue si no encuentras la solución

---

⭐ Si este proyecto te ha sido útil, ¡no olvides darle una estrella! 