#!/usr/bin/python


#MonitoreoIntranet
#Programa que gestiona la informacion de la maquina de la intranet, cuenta con las siguentes funcionalidades:
#1 Utiliza el programa RESTMonitoring para consultar información relacionada el funcionamiento de la maquina sobre la que se
# ejecuta, dentro de la intranet.
#2 Envia los datos de la maquina consultada a la pasarela en Heroku para mantener actualizada dicha informacion.
#Protocolo de comunicación:
#SEND INFOPC (<item-name>:<item-information>) 
