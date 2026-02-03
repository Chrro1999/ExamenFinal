Movies Manager — Backend API
Nombre: Christian Bolaños
Carrerra: Ingenieria Informatica

API REST construida con Django 4.2 y Django REST Framework para gestionar directores y películas.
Este es el backend de la aplicación Movies Manager, consumido por el frontend de React.


📋 Tabla de contenidos

Tecnologías
Estructura del proyecto
Instalación
Configuración
Modelos
Endpoints de la API
Filtros y búsqueda
Ejemplo de uso con Postman
Autenticación


🛠️ Tecnologías
TecnologíaVersiónFunciónPython3.11Lenguaje principalDjango4.2Framework web backendDjango REST Framework3.xConstrucción de la API RESTdjango-filter—Filtrado avanzado de datosdjango-cors-headers—Permite la comunicación con ReactSQLite—Base de datos (por defecto)

📂 Estructura del proyecto
examen-parcial-django-vistas-templates-y-modelos-Chrro1999/
│
├── examen2/                  # Configuración principal de Django
│   ├── __init__.py
│   ├── settings.py           # Configuración (CORS, REST_FRAMEWORK, etc.)
│   ├── urls.py               # Rutas principales
│   └── wsgi.py
│
├── movies/                   # App principal de películas
│   ├── __init__.py
│   ├── models.py             # Modelos: Director y Movie
│   ├── serializers.py        # Serializers para convertir datos a JSON
│   ├── views.py              # ViewSets (controladores de la API)
│   ├── urls.py               # Rutas de la API (/api/directors/, /api/movies/)
│   ├── admin.py              # Registro en el panel de administrador
│   └── migrations/           # Migraciones de la base de datos
│
├── db.sqlite3                # Base de datos SQLite
├── manage.py                 # Script de gestión de Django
└── requirements.txt          # Dependencias del proyecto

⚙️ Instalación
1. Clonar el repositorio
bashgit clone <URL_del_repositorio>
cd examen-parcial-django-vistas-templates-y-modelos-Chrro1999
2. Crear y activar el entorno virtual
bash# Crear venv
python -m venv venv

# Activar (Windows)
venv\Scripts\activate

# Activar (macOS / Linux)
source venv/bin/activate
3. Instalar dependencias
bashpip install -r requirements.txt
Si no existe requirements.txt, instala manualmente:
bashpip install django djangorestframework django-filter django-cors-headers
4. Aplicar migraciones
bashpython manage.py migrate
5. Crear superusuario (opcional — para el panel admin)
bashpython manage.py createsuperuser
6. Iniciar el servidor
bashpython manage.py runserver
El servidor estará disponible en:
👉 http://127.0.0.1:8000

📌 Configuración importante
CORS (settings.py)
Se permite la comunicación desde el frontend de React:
pythonCORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
]
REST Framework (settings.py)
La API responde solo en JSON (sin interfaz web de navegación):
pythonREST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

🗄️ Modelos
Director
CampoTipoDescripciónidAutoID único (generado automáticamente)nameCharFieldNombre del directornationalityCharFieldNacionalidadbirth_dateDateFieldFecha de nacimientobiographyTextFieldBiografíacreated_atDateTimeFieldFecha de creaciónupdated_atDateTimeFieldFecha de última modificación
Movie
CampoTipoDescripciónidAutoID únicotitleCharFieldTítulo de la películagenreCharFieldGénerodirectorForeignKey → DirectorDirector de la película (relación 1:N)release_yearPositiveIntegerFieldAño de estrenosynopsisTextFieldSinopsisduration_minutesPositiveIntegerFieldDuración en minutosratingDecimalFieldCalificación (ej: 8.5)created_atDateTimeFieldFecha de creaciónupdated_atDateTimeFieldFecha de última modificación

Relación: Un Director puede tener muchas películas (1:N). Si se elimina un director, sus películas se eliminan automáticamente (CASCADE).


🛣️ Endpoints de la API
Directores
MétodoEndpointDescripciónGET/api/directors/Listar todos los directoresPOST/api/directors/Crear un nuevo directorGET/api/directors/{id}/Ver detalle de un directorPUT/api/directors/{id}/Actualizar un director completoPATCH/api/directors/{id}/Actualizar campos específicosDELETE/api/directors/{id}/Eliminar un directorGET/api/directors/{id}/movies/Ver películas de un director
Películas
MétodoEndpointDescripciónGET/api/movies/Listar todas las películasPOST/api/movies/Crear una nueva películaGET/api/movies/{id}/Ver detalle de una películaPUT/api/movies/{id}/Actualizar una película completaPATCH/api/movies/{id}/Actualizar campos específicosDELETE/api/movies/{id}/Eliminar una película

🔍 Filtros y búsqueda
Búsqueda por texto
GET /api/directors/?search=Nolan
GET /api/movies/?search=Inception
Filtrado por campos
GET /api/movies/?genre=Acción
GET /api/movies/?director=1
GET /api/movies/?release_year=2010
Ordenamiento
GET /api/movies/?ordering=-rating        # De mayor a menor rating
GET /api/movies/?ordering=release_year   # De menor a mayor año
Paginación
La API retorna 10 resultados por página por defecto:
json{
    "count": 25,
    "next": "http://127.0.0.1:8000/api/movies/?page=2",
    "previous": null,
    "results": [...]
}
Para navegar entre páginas:
GET /api/movies/?page=2
