Proyectiño es una aplicación desarrollada en Django que permite a los usuarios registrarse, iniciar sesión, y realizar diversas funciones según sus roles y permisos. Este proyecto es un ejemplo de cómo implementar autenticación de usuarios, manejo de sesiones y otras funcionalidades básicas en Django.
Características

Registro de Usuarios: Permite a los usuarios crear una cuenta.
Inicio de Sesión: Permite a los usuarios autenticarse.
Cierre de Sesión: Los usuarios pueden cerrar sesión de manera segura.
Mensajes Informativos: Mensajes dinámicos que desaparecen después de un tiempo.

Instalación

Clona el repositorio:

sh

git clone https://github.com/matdax2/Prueba4-main.git
cd Prueba4-main/proyectiño

Crea un entorno virtual y actívalo:

sh

python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

Instala las dependencias:

sh

pip install -r requirements.txt

Realiza las migraciones:

sh

python manage.py migrate

Inicia el servidor de desarrollo:

sh

python manage.py runserver

Uso

Accede a http://127.0.0.1:8000 en tu navegador.
Regístrate o inicia sesión para empezar a usar la aplicación.
