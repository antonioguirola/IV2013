#!/usr/bin/ruby

# Almacenar un array en formato JSON en un fichero cuyo nombre se pase por línea de órdenes.

# Ejemplo de URL que devuelve JSON: http://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=false

require 'net/http'

url = ARGV[0]
name= ARGV[1]
respuesta = Net::HTTP.get  url, '/'
fname =  "#{name}.json"
if ( File.writable?(fname) ) 
    salida = File.new fname, "w"        
    salida.puts( respuesta )
else
    puts("No puedo escribir en #{fname}")
end

