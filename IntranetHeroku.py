#!/usr/bin/python
import requests
#Intranetheroku
#Este script que estara en heroku tendra las siguientes funcionalidades:
#1. Permitira obtener informacion que este almacenado en la base de datos de heroku, como el estado de las
# descargas y de la maquina en la intranet
#2. Podra obtener una lista de los magnets links de las descargas que aun no han sido iniciadas.
# Protocolo
# SEND DOWNLOAD <magnet-link>

#print("nombre\n")
nombre = input()
#print("magnetlink\n")
magnetlink = input()
estado= "pendiente"
ms= nombre+","+magnetlink+","+estado
url="https://proyectoredestorresvargas.herokuapp.com/descargar/"+ms
response = requests.get(url)
print(response)