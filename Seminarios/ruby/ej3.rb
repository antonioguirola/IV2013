#!/usr/bin/ruby

# Recorrer una estructura compleja exhaustivamente, imprimiendo todos los datos.


array={
	:'hola'=>:'que tal',
	:'pues'=>:'muy bien',
	:'numero'=>263262
}


array.keys().each do |key|
	puts array[key]
end