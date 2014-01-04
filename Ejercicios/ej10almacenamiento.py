# -*- coding: utf-8 -*- 

from azure.storage import *

#Establecemos conexión:
blob_service = BlobService(account_name='ivstorage', account_key='VXBxWOH3bbrT6RTyFlSK2txZJ1Ak0uCNlxD25rAAyPWQOSQ77AYrtGlZLv/ZIg1cmGN0udwJHfk5xcwD03UmPw==')

#Creamos un nuevo contenedor público:
blob_service.create_container('contenedorejdiez',x_ms_blob_public_access='container')

#Imprimimos los blobs del contenedor:
print("Blobs en el contenedor recién creado")
blobs = blob_service.list_blobs('contenedorejdiez')
for blob in blobs:
	print(blob.name)
	print(blob.url)
print('----------------------------------------------------')

#Leemos este mismo script y lo subimos al contenedor creado:
scriptPython = open(r'ej10almacenamiento.py', 'r').read()
blob_service.put_blob('contenedorejdiez', 'scriptPython', scriptPython, x_ms_blob_type='BlockBlob')

#volvemos a imprimir el contenido del contenedor:
print("Blobs en el contenedor:")
blobs = blob_service.list_blobs('contenedorejdiez')
for blob in blobs:
	print(blob.name)
	print(blob.url)
print('----------------------------------------------------')