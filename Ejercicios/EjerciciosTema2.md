
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


##Sesión del 28/10

### Ejercicio 3)

*1.- Instalar un sistema base con debootstrap*

En mi caso he instalado un sistema Ubuntu de 32 bits:

![captura](https://dl.dropboxusercontent.com/s/ewnfc74scphgnvm/ej3-1.png)

*2.- Experimentar con la creación de un sistema Fedora dentro de Debian usando Rinse.*

Tras instalar el paquete Rinse he instalado he ejecutado la orden `sudo rinse --arch i386 --directory /home/antonio/jaulas/fedora --distribution fedora-core-10` para instalar un sistema Fedora:

![captura](https://dl.dropboxusercontent.com/s/chieahlb4oio21c/ej3-2.png)

##Sesión del 4/11

### Ejercicio 4)

Una vez descargada con debootstrap el sistema Debian (Ubuntu) en la máquina anfitriona hay que configurar la máquina anfintriona:

```sh
sudo apt-get install dchroot <br>
sudo mkdir /var/chroot	
sudo chroot /var/chroot	
sudo nano /etc/schroot/schroot.conf
```	

Y añadir al final del archivo:

```sh
[Ubuntu]
description=Ubuntu
location=/home/antonio/jaulas/antonio
priority=3
users=antonio
groups=sbuild
root-groups=root
```

A continuación hay que configurar el directorio proc, para ello, desde la máquina anfitriona:
```sh
sudo mount -o bind /proc /home/antonio/jaulas/ubuntu/proc/
sudo cp /etc/resolv.conf /home/antonio/jaulas/ubuntu/etc/resolv.conf
```

Una vez hecho esto podemos ir a la jaula y comprobar que efectivamente se ejecutan órdenes como por ejemplo *top*

![captura](https://dl.dropboxusercontent.com/s/xqwm7pq3yqc8a8a/ej4-1.png)


### Ejercicio 5)

Utilizo la misma jaula Ubuntu del ejercicio anterior para instalar el servidor nginx en ella, como se ha configurado el acceso a Internet se pueden instalar paquetes sin problemas, en primer lugar, como se indica [en la documentación oficial](http://wiki.nginx.org/Install) hay que añadir el repositorio en el archivo */etc/apt/sources.list*

Continua....







