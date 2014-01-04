#!/usr/bin/python

import time
import sys
import os

# Comprobar el numero de argumentos:
if len(sys.argv)!=4:
	print(u'Error. Uso: archivo_a_copiar ruta_dir_xfs ruta_dir_btrfs')
	sys.exit()

archivo=sys.argv[1]
ruta_dir_xfs=sys.argv[2]
ruta_dir_btrfs=sys.argv[3]

# Copiar de sistema local (ext4) a xfs y btrfs
start = time.time()
os.system("cp "+archivo+" "+ruta_dir_xfs+"/archivo")
end = time.time()
t = end - start
print('Copiar de ext4 a xfs: '+str(t)+' s')

start = time.time()
os.system("cp "+archivo+" "+ruta_dir_btrfs+"/archivo")
end = time.time()
t = end - start
print('Copiar de ext4 a btrfs: '+str(t)+' s')

# Copiar xfs a si mismo
start = time.time()
os.system("cp "+ruta_dir_xfs+"/archivo "+ruta_dir_xfs+"/copia")
end = time.time()
t = end - start
print('Copiar de xfs a xfs: '+str(t)+' s')

# Copiar btrfs a si mismo
start = time.time()
os.system("cp "+ruta_dir_btrfs+"/archivo "+ruta_dir_btrfs+"/copia")
end = time.time()
t = end - start
print('Copiar de btrfs a btrfs: '+str(t)+' s')

# Copiar xfs a btrfs
start = time.time()
os.system("cp "+ruta_dir_xfs+"/archivo "+ruta_dir_btrfs+"/copia_desde_xfs")
end = time.time()
t = end - start
print('Copiar de xfs a btrfs: '+str(t)+' s')

# Copiar btrfs a xfs
start = time.time()
os.system("cp "+ruta_dir_btrfs+"/archivo "+ruta_dir_xfs+"/copia_desde_btrfs")
end = time.time()
t = end - start
print('Copiar de btrfs a xfs: '+str(t)+' s')