**Ejercicio 1)**

Para realizar el ejercicio me he descargado la iso de [lubuntu 13.10](https://help.ubuntu.com/community/Lubuntu/GetLubuntu) por ejemplo.

Lo primero que tenemos que hacer es crear el directorio donde vayamos a montar la imagen, a continuación hay que utilizar la orden `sudo unshare -m <directorio>`, se usa la opción `-m` para indicar que estamos creando un espacio de nombres para unidades de montaje. El último paso es montar la imagen como se muestra en la captura:

![captura](https://dl.dropboxusercontent.com/s/x92pu2gifzqh5zx/ej1-1.png)

Para comprobar que es correcto abrimos otro terminal con un hostname diferente e intentamos acceder al contenido de la imagen:

![captura](https://dl.dropboxusercontent.com/s/qhciv9a2t1ha0mc/ej1-2.png?m)

De esta manera hemos comprobado que sólo es accesible desde el espacio de nombres creado al principio.
