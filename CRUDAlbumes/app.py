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
    
    try: 
        cursor = mysql.connection.cursor()
        cursor.execute('select * from albumes')
        datos = cursor.fetchall()
        
        return render_template('index.html', albums= datos)
    
    except Exception as e :
        print('e')

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

@app.route('/editarAlbum/<id>')
def editarAlbum(id):
    
    cursor = mysql.connection.cursor()
    cursor.execute('select * from albumes where id_album= %s',[id])
    datos = cursor.fetchone()
    
    return render_template('editar.html',album=datos)

@app.route('/actualizarAlbum',methods=['POST'])
def actualizarAlbum():
    
    txtid = request.form['txtId']
    txtTitulo = request.form['txtTitulo']
    txtArtista = request.form['txtArtista']
    txtYear = request.form['txtYear']
    
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('update albumes set titulo = %s, artista = %s, year = %s where id_album= %s',(txtTitulo,txtArtista,txtYear,txtid))
        mysql.connection.commit()
        
        flash('Album guardado correctamente')
                
        return redirect(url_for('index'))
        
    except Exception as e:
        print(e)


@app.route('/borrarAlbum',methods=['POST'])
def borrarAlbum():
    
    txtid = request.form['txtIdAlbum']
    
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('delete from albumes where id_album = %s',[txtid])
        mysql.connection.commit()
        
        flash('Album eliminado correctamente')
                
        return redirect(url_for('index'))
        
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(port=3000, debug=True)