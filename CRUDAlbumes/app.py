from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os
import urllib.request

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'


app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = ''

app.config['MYSQL_DB'] = 'bdFlask'

app.secret_key= 'llave'


carpetaImagenes = 'static/images'

app.config['UPLOAD_FOLDER'] = carpetaImagenes


mysql = MySQL(app)



@app.route('/')
def index():
    
    try: 
        cursor = mysql.connection.cursor()
        cursor.execute('select * from albumes')
        datos = cursor.fetchall()
        
        print(datos)
        
        return render_template('index.html', albums= datos)
    
    except Exception as e :
        print('e')

@app.route('/guardarAlbum',methods=['POST'])
def guardarAlbum():
    if request.method == 'POST':
        
        img  = request.files['Imagen']
        
        if 'Imagen' not in request.files or img.filename == '':
            
            flash('Imagen no válida')
            return redirect(url_for(index))
        
        elif img :
            
            nombreArchivo = secure_filename(img.filename)
            
            
            # Tomar los datos que vienen de POST
            txtTitulo = request.form['txtTitulo']
            txtArtista = request.form['txtArtista']
            txtYear = request.form['txtYear']
            
            try: 
                
                img.save(os.path.join(app.config['UPLOAD_FOLDER'],nombreArchivo))
                
                # print('nombre del archivo de la imagen ', nombreArchivo)
                
                # Enviar datos a la Base de Datos 
                cursor = mysql.connection.cursor()
                cursor.execute('INSERT INTO albumes(titulo, artista, year, urlImg ) values (%s,%s,%s,%s)', (txtTitulo,txtArtista,txtYear, nombreArchivo))
                mysql.connection.commit()
                
                
                flash('Album guardado correctamente')
                    
                return redirect(url_for('index'))
            
            except:
                print('error Catch')
                
        else:
            print('Error If')

@app.route('/editarAlbum/<id>')
def editarAlbum(id):
    
    cursor = mysql.connection.cursor()
    cursor.execute('select * from albumes where id_album= %s',[id])
    datos = cursor.fetchone()
    
    return render_template('editar.html',album=datos)

@app.route('/actualizarAlbum',methods=['POST'])
def actualizarAlbum():
    
    
    img  = request.files['Imagen']
    
    if 'Imagen' not in request.files or img.filename == '':
    
        flash('Imagen no válida')
        return redirect(url_for(index))

    elif img:
        nombreArchivo = secure_filename(img.filename)
        
        img.save(os.path.join(app.config['UPLOAD_FOLDER'],nombreArchivo))
        
        txtid = request.form['txtId']
        txtTitulo = request.form['txtTitulo']
        txtArtista = request.form['txtArtista']
        txtYear = request.form['txtYear']

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('update albumes set titulo = %s, artista = %s, year = %s, urlImg = %s where id_album= %s',(txtTitulo,txtArtista,txtYear,nombreArchivo,txtid))
            mysql.connection.commit()
            
            flash('Album actualizado correctamente')
            
            return redirect(url_for('index'))
            
        except Exception as e:
            print(e, 'error ')


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