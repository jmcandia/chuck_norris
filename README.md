# Chuck Norris

Aplicación de ejemplo de programación back end con Django y MySQL.

## Tabla de contenidos

- [Prerequisitos](#prerequisitos)
  - [Instalación de MySQL](#instalación-de-mysql)
    - [En Windows](#en-windows)
    - [En macOS](#en-macos)
    - [En Linux](#en-linux)
- [Instalación](#instalación)
- [Ejecución](#ejecución)

## Prerequisitos

### Instalación de MySQL

Antes de ejecutar el proyecto, se debe instalar la base de datos [MySQL](https://www.mysql.com/). Para ello, debe seguir las instrucciones específicas para cada sistema operativo.

#### En Windows

Para instalar MySQL se deben seguir las [instrucciones oficiales](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install-windows-quick.html) del proveedor.

#### En macOS

Instalar el servidor y el cliente de MySQL:

```bash
brew install mysql
```

Si no desea instalar el servidor MySQL, puede utilizar mysql-client en su lugar:

```bash
brew install mysql-client
echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile
export PATH="/usr/local/opt/mysql-client/bin:$PATH"
```

#### En Linux

Es posible que tenga que instalar las cabeceras y bibliotecas de desarrollo de Python 3 y MySQL de la siguiente manera:

- Ubuntu/Debian

  Primero, se debe actualizar el sistema operativo:

  ```bash
  sudo apt update && sudo apt upgrade
  ```

  Luego, debemos instalar el servidor MySQL. Este proceso instala el servidor y el cliente:

  ```bash
  sudo apt install mysql-server
  ```

  Si solo se desea instalar el cliente para conectarse a una instancia remota de MySQL, se debe ejecutar este comando en lugar del anterior:

  ```bash
  sudo apt install mysql-client
  ```

  Por último, se realiza la instalación de las herramientas de desarrollo

  ```bash
  sudo apt install python3-dev default-libmysqlclient-dev build-essential
  ```

- Red Hat/CentOS

  Necesitarás actualizar el sistema escribiendo el siguiente comando:

  ```bash
  sudo yum update
  ```

  Una vez actualizado el sistema, es hora de instalar MySQL.

  ```bash
  sudo yum install mysql
  ```

  Por último, se realiza la instalación de las herramientas de desarrollo

  ```bash
  sudo yum install python3-devel mysql-devel
  ```

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

En primer lugar, debemos crear la base de datos MySQL. Para ello, vamos a usar el cliente MySQL desde la línea de comandos:

```bash
mysql -h localhost -u root -p
```

Una vez conectados, ejecutaremos el siguiente comando:

```mysql
mysql> create schema chuck_norris;
```

Luego de crear la base de datos, debemos modificar el archivo `chuck_norris/settings.py` para agregar la conexión a MySQL. No hay que olvidar reemplazar los valores `<nombre_base_datos>`, `<direccion_servidor>`, `<usuario_base_datos>` y `<contraseña_base_datos>` con los propios:

```python
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<nombre_base_datos>',
        'HOST': '<direccion_servidor>',
        'PORT': '3306',
        'USER': '<usuario_base_datos>',
        'PASSWORD': '<contraseña_base_datos>'
    }
}
```

Una vez configurada la conexión, se deben efectuar las migraciones:

```bash
python3 manage.py migrate
```

Para lanzar la aplicación, ejecutaremos el siguiente comando:

```bash
python3 manage.py runserver
```
