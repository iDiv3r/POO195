from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'


app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = ''

app.config['MYSQL_DB'] = 'bdFlask'

app.secret_key= 'llave'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardarAlbum',methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        
        print (request.form)
        
        # Tomar los datos que vienen de POST
        txtTitulo = request.form['txtTitulo']
        txtArtista = request.form['txtArtista']
        txtYear = request.form['txtYear']
        
        try: 
            # Enviar datos a la Base de Datos 
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO albumes(titulo, artista, year ) values (%s,%s,%s)', (txtTitulo,txtArtista,txtYear))
            mysql.connection.commit()
            
            
            flash('Album guardado correctamente')
                
            return redirect(url_for('index'))
        
        except:
            print('error')
        



if __name__ == '__main__':
    app.run(port=3000, debug=True)