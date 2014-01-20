### Ejercicio 1)

Para este ejercicio voy a usar la máquina virtual creada en Azure que ya utilicé en el tema anterior.

El primer paso es configurar la conexión SSH con la máquina anfitriona mediante `ssh-copy-id -i ~/.ssh/id_rsa.pub azureuser@iv-ubuntu-1310.cloudapp.net`. Una vez configurado accedemos a la MV e instalamos Chef:

```sh
ssh azureuser@iv-ubuntu-1310.cloudapp.net
sudo apt-get install ruby1.9.1 ruby1.9.1-dev rubygems
sudo gem install ohai chef
```

### Ejercicio 2)

Creamos la carpeta chef y generamos la configuración:

![captura](capturas/tema6/ej2-1.png)

