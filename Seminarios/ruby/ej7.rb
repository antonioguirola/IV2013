#!/usr/bin/ruby

=begin
 Crear una serie de funciones instanciadas con un URL que devuelvan 
 algún tipo de información sobre el mismo: fecha de última modificación, 
 por ejemplo. *Pista*: esa información está en la cabecera HTTP que devuelve
=end

# Ejemplos de uso: 
#ruby ej6.rb 'http://www.ugr.es' 'content-type'
#ruby ej6.rb 'http://www.ugr.es' 'Date'

require 'net/http'

url = ARGV[0]
field = ARGV[1]

response = nil
Net::HTTP.start(url, 80) {|http|
  response = http.head('/')
}

#p response['content-type']
p response[field]
