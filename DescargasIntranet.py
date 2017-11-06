#!/usr/bin/python
import requests


#DescargasIntranet
#Este script que estara ubicado en la maquina de la intranet tendra las siguientes funcionalidades:
#1. Se encargara de generar una conexion desde la intranet a la pasarela
#2. Podra enviar informacion desde la intranet a la pasarela para tener la informacion actualizada
#del estado de la descarga
#3. Podra comunicarse con la pasarela para saber si hay descargas pendientes o no
#4. De existir utilizara transmission con el magnet link e iniciara la descarga
# Protocolo
# SEND INFODOWNLOAD (<id-download>:<Download-status>)
# REQUEST INFODOWNLOAD

url = "https://proyectoredestorresvargas.herokuapp.com/consultar/21"
response = requests.get(url)
 
if response.status_code == 200:
   results = response.content
   print results
else:
   print "Error code %s" % response.status_code