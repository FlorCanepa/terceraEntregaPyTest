Funcionalidades:
Herencia de HTML.
Tres clases en models: Author, Book, Publisher.
Formularios para insertar datos en todas las clases.
Formulario para buscar libros en la base de datos.


Instrucciones


clonar el repositorio

Crea un entorno virtual:

python -m venv env
Activa el entorno virtual:
En Windows:
.\env\Scripts\activate
En macOS/Linux:
source env/bin/activate
Instala las dependencias:
pip install django
Realiza las migraciones:
Primero ejecutar:
python manage.py makemigrations
Luego ejecutar:
python manage.py migrate

Opcional crear el superusuario!
usar python manage.py createsuperuser


Inicia el servidor:
python manage.py runserver
Navega a http://localhost:8000 para acceder a la aplicación.

