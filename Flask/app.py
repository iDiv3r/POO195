from flask import Flask, request

app = Flask(__name__)

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


@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis, esa url no existe'


if __name__ == '__main__':
    app.run(port=3000,debug=True)