
##Sesión 11/11

###Ejercicio 1)

![captura](https://dl.dropboxusercontent.com/s/9w799clyb5qafto/ej1-1.png)

### Ejercicio 2)

He instalado un contenedor Ubuntu mediante `sudo lxc-create -t ubuntu -n caja1`. Una vez ha terminado la instalación hay que arrancarlo con `sudo lxc-start caja1`, comprobamos que esté funcionando:

![captura](https://dl.dropboxusercontent.com/s/vp5h68b9g6sira0/ej2-1.png)

Y por último vemos los puentes de red activos `sudo brctl show`:

![captura](https://dl.dropboxusercontent.com/s/c5mxvgy08tn8r22/ej2-2.png)

Como se observa se ha creado un puente de red hacia el contenedor llamado *lxcbr0*.
