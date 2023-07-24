# htbClientV4

**htbclientV4** es una herramienta que funciona como un cliente de terminal basado en el de [s4vitar](https://github.com/s4vitar) pero usando algunos elementos de la version 4 dela api de Hackthebox.

¿Cómo me autentico?
======
Lo primero que debemos hacer es dirigirnos a la nueva interfaz de [Hackthebox](https://www.hackthebox.com) , una vez iniciada la sesión , tendremos que dirigirnos a los ajustes de nuestro perfil.Crearemos un nuevo "JSON WEB TOKEN" (Los JSON WEB TOKEN tienen "fecha de caducidad" por así decirlo , por eso deberemos elegir 1 año de validez).De todas formas he creado un pequeño script en python que podeis usar si quereis renovarlo cada poco pero recomiendo hacerlo desde la web y añadir 1 año de validez , recordad verificar la validez del JWT si veis que no funciona la herramienta.

<p align="center">
<img src="Images/get_jwt.png"
        alt="First"
        style="float: left; margin-right: 10px;" />
</p>


Ahora deberemos obtener nuestro "API_TOKEN" de la interfaz antigua de Hackthebox [Link](https://www.hackthebox.com/login).Una vez iniciemos sesión pincharemos en nuestro perfil y deberemos pinchar en el apartado "settings".

<p align="center">
<img src="Images/localizar_settings.png"
        alt="Second"
        style="float: left; margin-right: 10px;" />
</p>

Una vez dentro nos dirigimos al apartado del API key y lo copiamos.

<p align="center">
<img src="Images/get_api_key.png"
        alt="Third"
        style="float: left; margin-right: 10px;" />
</p>

Ahora que ya tenemos el "JSON WEB TOKEN" y el "API TOKEN" debemos introducirlos en el código , simplemente al abrir el archivo se indica en las primeras líneas.

<p align="center">
<img src="Images/authentication_into_the_code.png"
        alt="Fourth"
        style="float: left; margin-right: 10px;" />
</p>

Esta utilidad cuenta con un modo de enumeración (**parámetro -e**) bastante rápido.

<p align="center">
<img src="Images/enumeration_mode_panel.png"
        alt="Fifth"
        style="float: left; margin-right: 10px;" />
</p>

Con el podremos listar las maquinas desplegadas en el laboratorio de Hackthebox.

<p align="center">
<img src="Images/spawned_machines_file.png"
        alt="6"
        style="float: left; margin-right: 10px;" />
</p>

Si queremos ver las máquinas activas tambien tenemos esa opción y las que se muestran en el panel de ayuda.

<p align="center">
<img src="Images/active_machines_file.png"
        alt="7"
        style="float: left; margin-right: 10px;" />
</p>

Tambien tenemos modos de búsqueda más personalizados , con el parámetro "-s" podemos buscar cualquier cosa "Nombre - Ip - Fechas..." , si queremos buscar las máquinas en base al identificador recomiendo usar el parámetro "-i" ya que es más preciso.

<p align="center">
<img src="Images/search_machines_file.png"
        alt="8"
        style="float: left; margin-right: 10px;" />
</p>

Si inspeccionamos un poco más el panel de ayuda nos daremos cuenta de que podemos parar/resetear/desplegar/enviar flag(algunos son VIP).

<p align="center">
<img src="Images/help_panel_spawned_machines.png"
        alt="9"
        style="float: left; margin-right: 10px;" />
</p>

<p align="center">
<img src="Images/control_machines_file.png"
        alt="9"
        style="float: left; margin-right: 10px;" />
</p>

Para enviar la flag usaremos el siguiente método:

* htbclientV4 -f Lame=9d59efd64df62d3bc326dcb4ffc597cf,10

* El número 10 representa la dificultad personal que le ponemos a la máquina una vez hecha.

* Esta herramienta no es tan completa como la de s4vitar pero en algunos aspectos es más rápida debido a la combinación de ambas versiones de la api de Hackthebox.

## Redes sociales de s4vitar y enlace a su academia
[S4vitar Youtube](https://www.youtube.com/s4vitar)
[S4vitar Instragram](https://www.instagram.com/s4vitarx/)
[S4vitar Twitter](https://twitter.com/S4vitar)
[S4vitar Linkedin](https://es.linkedin.com/in/s4vitar)
[S4vitar Academia](https://hack4u.io/)

