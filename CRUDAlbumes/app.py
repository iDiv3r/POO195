from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'


app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = ''

app.config['MYSQL_DB'] = 'bdFlask'


mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardarAlbum',methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        titulo = request.form['txtTitulo']
        artista = request.form['txtArtista']
        year = request.form['txtYear']
        
        print(titulo, artista, year)
        return 'Datos recibidos'

if __name__ == '__main__':
    app.run(port=3000, debug=True)