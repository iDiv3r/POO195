from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/numeroalcuadrado/<numero>')
def numeroalcuadrado(numero):
    
    numero2 = int(numero) * int(numero)
    
    return str(numero2)


@app.errorhandler(404)
def error(e):
    return "Error: Ruta no encontrada"    


if __name__ == '__main__':
    app.run(debug=True, port=3000)