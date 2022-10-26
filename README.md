# Chuck Norris

Aplicación de ejemplo de programación back end con Django y MySQL.

## Tabla de contenidos

- [Instalación](#instalación)
- [Ejecución](#ejecución)

## Instalación

1. Ir al directorio del proyecto:

   ```bash
   cd chuck_norris
   ```

   Se debe observar la siguiente estructura de carpetas:

   ```bash
   chuck_norris
   ├── chuck_norris
   │   ├── asgi.py
   │   ├── settings.py
   │   ├── urls.py
   │   ├── wsgi.py
   │   └── __init__.py
   ├── facts
   │   ├── admin.py
   │   ├── apps.py
   │   ├── models.py
   │   ├── tests.py
   │   ├── views.py
   │   ├── __init__.py
   │   └── migrations/
   ├── .gitignore
   ├── manage.py
   ├── README.md
   └── requirements.txt
   ```

2. Luego, debemos instalar `virtualenv` para crear un entorno virtual.

   ```bash
   # Se actualiza pip a la última versión
   python3 -m pip install --upgrade pip
   # Se instala virtualenv
   pip install virtualenv
   ```

   Una vez instalado, se crea un entorno virtual, dentro del directorio del proyecto:

   ```bash
   virtualenv env
   ```

   Si recibe el siguiente mensaje de error al ejecutar el comando anterior:

   ```cmd
   "virtualenv" no se reconoce como un comando interno o externo,
   programa o archivo por lotes ejecutable.
   ```

   O bien, si recibe el siguiente mensaje de error:

   ```ps1
   virtualenv: The term 'virtualenv' is not recognized as a name of a cmdlet, function, script file, or executable program.
   Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
   ```

   Entonces debe ejecutar el comando:

   ```cmd
   python3 -m virtualenv env
   ```

   Para activar el entorno virtual, se debe ir al directorio del proyecto y ejecutar el comando:

   En linux:

   ```bash
   source env/bin/activate
   ```

   En windows:

   ```ps1
   env\Scripts\activate.bat
   ```

   Una vez activado, el nombre del actual ambiente aparece a la izquierda de la consola:

   En linux:

   ```bash
   (env) usuario@equipo:~/chuck_norris$
   ```

   En windows:

   ```cmd
   (env) C:\chuck_norris>
   ```

   Para salir del entorno virtual, se debe ejecutar el comando:

   ```bash
   deactivate
   ```

   > **Nota:** Este paso es opcional, pero sirve para no tener que instalar los paquetes en la instancia del usuario.

3. Ahora es momento de instalar los paquetes necesarios para el proceso:

   ```bash
   pip install -r requirements.txt
   ```

   > **Nota:** Si está usando el entorno virtual, debe asegurarse de activarlo previamente.

## Ejecución

En primer lugar, debemos efectuar las migraciones:

```bash
python3 manage.py migrate
```

Para lanzar la aplicación, ejecutaremos el siguiente comando:

```bash
python3 manage.py runserver
```
