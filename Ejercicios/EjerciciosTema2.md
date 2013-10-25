
##Sesión 21/10

###Ejercicio 1)

Para realizar el ejercicio me he descargado la iso de [lubuntu 13.10](https://help.ubuntu.com/community/Lubuntu/GetLubuntu) por ejemplo.

Lo primero que tenemos que hacer es crear el directorio donde vayamos a montar la imagen, a continuación hay que utilizar la orden `sudo unshare -m <directorio>`, se usa la opción `-m` para indicar que estamos creando un espacio de nombres para unidades de montaje. El último paso es montar la imagen como se muestra en la captura:

![captura](https://dl.dropboxusercontent.com/s/x92pu2gifzqh5zx/ej1-1.png)

Para comprobar que es correcto abrimos otro terminal con un hostname diferente e intentamos acceder al contenido de la imagen:

![captura](https://dl.dropboxusercontent.com/s/qhciv9a2t1ha0mc/ej1-2.png?m)

De esta manera hemos comprobado que sólo es accesible desde el espacio de nombres creado al principio.

##Sesión 25/10

###Ejercicio 2)

*1.- Mostrar los puentes configurados en el sistema operativo*

Como muestra la siguiente captura no tengo configurado ningún puente en el sistema:

![captura](https://dl.dropboxusercontent.com/s/x1zvepj5bgrtnxu/ej2-1.png)

*2.- Crear un interfaz virtual y asignarlo al interfaz de la tarjeta wifi, si se tiene, o del fijo, si no se tiene.*

A la hora de asignar el puente a la red inalámbrica no me dejó en un principio, 
![captura](https://dl.dropboxusercontent.com/s/wpt3mo6emqo1g1y/ej2-2.png)

pero utilizando[esta solución](http://ubuntuforums.org/showthread.php?t=1681045) lo pude solucionar.

![captura](https://dl.dropboxusercontent.com/s/pi7kfijytih7g1b/ej2-3.png)


### Ejercicio 3)



