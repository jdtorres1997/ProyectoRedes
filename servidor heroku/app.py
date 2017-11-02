from flask import Flask
import psycopg2
import urllib.parse as urlparse
import os

url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port
con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )
seriedes = 1
app = Flask(__name__)

@app.route('/')
def homepage():
	buffer = con.cursor()
	buffer.execute("""SELECT id,magnetlink FROM descargaspendientes""")
	row = buffer.fetchone()
	while row is not None:
		seriedes = row[0]
		row = buffer.fetchone()
	
	return """
    		<h1>Proyecto fundamentos de redes</h1>
		<p>Juan David torres cañon 1526750</p>
		<p>Juan Jose Vargas Vargas 1523382</p>
		<p>La base de datos cuenta con {datoserie} registros</p>
    		<img src="https://i0.wp.com/occidente.co/wp-content/uploads/2015/11/univalle-nov-201.jpg?fit=600%2C338">
    	""".format(datoserie=seriedes)

@app.route('/descargar/<link>')
def descargar(link):
	buffer=con.cursor()
	buffer.execute("""INSERT INTO descargaspendientes (nombre, magnetlink, fecha, estado, progreso) VALUES ('descarga', '"""+link+"""',  '2017/10/31', 'pendiente', 0)""")
	buffer.execute("""COMMIT""")
	buffer = con.cursor()
	buffer.execute("""SELECT id FROM descargaspendientes""")
	row = buffer.fetchone()
	while row is not None:
		seriedes = row[0]
		row = buffer.fetchone()
	
	return """
		<h1>Su descarga ha sido añadida a la lista</h1>
		<p>El codigo de su descarga es """+seriedes+""".</p>
		<p>El link ingresado es """+link+"""</p>
		
	"""
#.format(datoserie=seriedes)

@app.route('/consultar/<ide>')
def consultar(ide):
	buffer = con.cursor()
	buffer.execute("""SELECT magnetlink FROM descargaspendientes WHERE id='"""+ide+"""'""")
	row = buffer.fetchone()
	link1 = row[0]
	return """
		<h1>Consulta</h1>
		<p>El magnet link asociado a """+ide+""" es</p>
		<p>{zelda}</p>
	""".format(zelda=link1)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

