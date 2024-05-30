from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
# "localhost:3308" (puerto de la base de datos)

app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = ''

app.config['MYSQL_DB'] = 'bdFlask'


mysql = MySQL(app)



# Ruta Básica 
@app.route('/')
def principal():
    return "Hola Mundo"  


# Ruta Doble 
@app.route('/usuario')
@app.route('/saludar')
def saludos():
    return "Hola Emiliano"

# Rutas con parametros 
@app.route('/hi/<nombre>')
def hi(nombre):
    return "Hola " + nombre

# Definicion de métodos HTTP
@app.route('/formulario',methods=['GET', 'POST'])
def formulario():
    if request.method == 'GET':
        return 'No es seguro enviar pass por GET'
    elif request.method == 'POST':
        return 'POST si es seguro para el envio de pass'

# Error Handler 
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis, esa url no existe'


@app.route('/pruebaConexion')
def pruebaConexion():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("Select 1")
        datos = cursor.fetchone()
        return jsonify({'status': 'Conexion exitosa', 'data': datos})
    
    except Exception as e:
        return jsonify({'status': 'Error en la conexion', 'error': str(e)})



if __name__ == '__main__':
    app.run(port=3000,debug=True)