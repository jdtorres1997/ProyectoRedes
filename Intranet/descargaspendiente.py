#!/usr/bin/python
import requests

url="https://proyectoredestorresvargas.herokuapp.com/pendiente"
response = requests.get(url)
print(response.content)