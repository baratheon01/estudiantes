import sqlite3

conexion = sqlite3.connect('ejemplo.db')

# Creamos el cursor
cursor = conexion.cursor()


#CREANDO LA BASE DE DATOS
#cursor.execute("CREATE TABLE estudiantes ('id' INTEGER PRIMARY KEY AUTOINCREMENT ,'nombre' VARCHAR(100), 'apellido' VARCHAR(100), 'cedula' INTEGER, 'telefono' INTEGER)")
#FUNCION DE INSERTAR
#cursor.execute("INSERT INTO estudiantes VALUES('1','Daniel', 'Rodriguez', 1020387456, 2345656)")
#FUNCION DE SELECCIONAR
#cursor.execute("SELECT * FROM estudiantes")
#print(cursor)
#es = cursor.fetchone()
#es = cursor.fetchall()
#print(es)
#FUNCION actualizar
#cursor.execute("UPDATE estudiantes SET nombre='Simon' where id='1'")
#FUNCION DELETE
#cursor.execute("DELETE FROM estudiantes")
# Guardamos los cambios haciendo un commit
conexion.commit()

conexion.close()