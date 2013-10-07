**Ejercicio 1)**

El servidor que he seleccionado es un Dell PowerEdge T420 ([http://configure.euro.dell.com/dellstore/config.aspx?oc=pet420u&model_id=poweredge-t420&c=es&l=es&s=bsd&cs=esbsdt1]), cuyo precio base es de 2599,00€.

Como se especifica en el artículo se puede aplicar un coste de un máximo del 25% del precio base en concepto de amortización por productos informáticos, que es el equivalente a 4 años.

Para amortizar el equipo a 4 años los costes aplicables serían los siguientes:

2599*0,25 = 649,75€ / año

Para 7 años:

100/7=14,29
2599*0,1429 = 371,3971 € / año

Hay que tener en cuenta que en cualquiera de los casos hay que aplicar como coste el 100% del IVA.

Ejercicio 5)

Para ello sólo hay que ejecutar en el terminal "sudo apt-get install git"

Ejercicio 6)

Tras crear el repositorio en github (en mi caso se llama IV2013) se crea una carpeta con el mismo nombre en el disco duro y se usan las siguientes órdenes:

git clone https://github.com/antonioguirola/IV2013.git ---> Descarga el contenido del repositorio a la máquina local <br/>
nano README.md ---> Editamos el archivo <br/>
git add README.md ---> Añadimos al repo local el archivo README <br/>
git commit -m "Primer cambio" ---> Fijamos los cambios añadiendo un mensaje <br/>
git push origin master ---> Subimos los cambios al repositorio remoto <br/>

Ejercicio 7)

He creado tres grupos: buenos, malos y regulares; y les he asignado los procesos chrome, gedit y bash respectivamente.

Tras 5 minutos los usos mostrados son los siguientes: <br/>
cat buenos/cpuacct.usage --> 1141152648  <br/>
cat malos/cpuacct.usage  --> 113046023  <br/>
cat regulares/cpuacct.usage --> 142546251  <br/>

Como se puede observar el navegador web es el proceso que más ha consumido.
