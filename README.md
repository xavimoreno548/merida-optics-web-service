# Óptica Mérida Web Service
## Resumen.

Esta aplicación web (Servicios REST), es el API del proyecto Óptica Mérida, el cual esta implemetado en Python Flask, a continuación, se muestran
todas las dependencias necesarias para ejecutar el proyecto en una máquina local.

## Dependencias.

Las dependencias escenciales de la aplicación se muestran a continuacion, es necesario instalar cada uno con Python Package Index (PIP).
| Requerimiento | Descripción | Versión|
|-|-|-|
| Python | Lenguaje de programación orientado a objetos | 3.8.6|
| SQLAlchemy | Mapeador de objetos relacional | 1.3|
| Flask | Microframework de desarrollo web para python| 1.1.2|

## Comandos de ejecución.

Con el fin de facilitar la ejecución del proyecto, se proveen los comandos a usar para instalar todos los requerimientos, para el caso exclusivo del API se recomienda
usar un sistema Linux, preferiblemente Debian, Ubuntu o derivados.

### Python

Para instalar una version personalizada que no chocque con la versión del sistema, adjuntamos una guia para agregar Python, y VirtualEnv: [Instalar Python](https://help.dreamhost.com/hc/es/articles/115000702772-Instalar-una-versi%C3%B3n-personalizada-de-Python-3)

### SQLAlchemy

El ORM [SQLAlchemy](https://docs.sqlalchemy.org/en/13/orm/) puede instalarse una vez tenga PIP dentro de su máquina, corriendo el siguiente comando desde
una terminal Linux:

~~~
$ pip install SQLAlchemy
~~~

### Flask

De igual manera [Flask](https://flask.palletsprojects.com/en/1.1.x/) solo necesita de una instalación por linea de comandos como la anterior:

~~~
$ pip install Flask
~~~

### Base de datos

En el directorio /DataBaseCrud/Backup/ encontramos en script optica_merida_backup.sql, este puede ser ejecutado en un entorno mysql, ya sea a traves de un cliente grafico o en una terminal.

## Dev Server.

Para poner en marcha el servidor es necesario tener instaladas todas las dependencias, abrir una terminal y posicionarse en la raiz del proyecto, luego ejecutar los siguientes comandos.

~~~
$ cd Api
~~~
~~~
$ flask run -h localhost
~~~

Esto levantará por defecto un servidor web en el puero 5000, si desea cambiar el puerto y el host, ingrese el siguiente comando, agregando en los elementos en corchetes los respectivos valores.

~~~
$ flask run -h [host] -p [port]
