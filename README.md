
![JaxiStore Logo](image.png)

## Descripción del Proyecto

Este proyecto realiza facturas a base de órdenes de compras de diversos clientes.

## Justificación del Proyecto

Se realizó esta aplicación web para que la proveedora de insumos veterinarios JaxiStore pueda realizar más fácilmente su venta de insumos con las órdenes de factura que llegan de distintos clientes que desean comprar.

## Cómo Comenzar la Instalación de la Aplicación Web

1. Instalar Python en su dispositivo.
2. Descargar el archivo de la aplicación web.
3. Abrirlo en Visual Studio Code.
4. Crear un entorno con el siguiente comando:
   ```shell
   python -m venv nombre_del_entorno
   ```
5. Activar el entorno:
   ```shell
   nombre_del_entorno\Scripts\activate
   ```
6. Una vez activado el entorno, instalar las dependencias del archivo `requirements.txt` con el siguiente comando:
   ```shell
   pip install -r requirements.txt
   ```
7. Realizar migraciones con el siguiente comando:
   ```shell
   python manage.py migrate
   ```
8. Crear un superusuario con el que podrán iniciar sesión con el siguiente comando:
   ```shell
   python manage.py createsuperuser
   ```
   Debe darle un nombre, un correo y una contraseña.
9. Levantar el servidor para poder utilizar la aplicación web con el siguiente comando:
   ```shell
   python manage.py runserver
   ```
10. Iniciar sesión con sus credenciales del superusuario anteriormente creado en el paso 8.

## ¡Gracias por usar JaxiStore!

Esperamos que esta aplicación web facilite enormemente la gestión de tus órdenes de compra y facturación. Si tienes alguna pregunta, sugerencia o necesitas asistencia, no dudes en ponerte en contacto con nosotros.

¡Nos encantaría saber tu opinión! Únete a nuestra comunidad y comparte tus experiencias. Juntos, podemos hacer de JaxiStore una herramienta aún mejor.

¡Gracias por confiar en JaxiStore y feliz facturación!

El equipo de JaxiStore