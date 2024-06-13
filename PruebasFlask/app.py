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
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('registrosMedicos.html')

@app.route('/guardarMedico',methods=['POST'])
def guardarMedico():
    if request.method == 'POST':        
        
        print(request.form)
        
        txtRfc= request.form['txtRfc']
        txtNombre = request.form['txtNombre']
        txtCedula = request.form['txtCedula']
        txtCorreo = request.form['txtCorreo']
        txtPass = request.form['txtPass']
        txtRol = request.form['txtRol']
        
        try: 
            
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO medico(rfc,nombreCompleto,cedula,correo,password,rol) values (%s,%s,%s,%s,%s,%s)', (txtRfc,txtNombre,txtCedula,txtCorreo,txtPass,txtRol))
            mysql.connection.commit()
            
            
            flash('El médico fue guardado correctamente')
                
            return redirect(url_for('register'))
        
        except:
            flash('Error al guardar usuario')
                
            return redirect(url_for('register'))
        



if __name__ == '__main__':
    app.run(port=3000, debug=True)