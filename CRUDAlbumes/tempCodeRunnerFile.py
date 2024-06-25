 try: 
        cursor = mysql.connection.cursor()
        cursor.execute('select * from albumes')
        datos = cursor.fetchall()
        
        return render_template('index.html', albums= datos)
    
    except Exception as e :
        print('e')