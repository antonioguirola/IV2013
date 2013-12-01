#!/usr/bin/ruby

# ¿Se pueden crear estructuras de datos mixtas en Ruby? 
# Crear un array de hashes de arrays e imprimirlo.

array={
	:'hola'=>:'que tal',
	:'pues'=>:'muy bien'
}

superArray={
	:'clave1'=>2452,
	:'clave2'=>array
}

puts superArray.to_s
