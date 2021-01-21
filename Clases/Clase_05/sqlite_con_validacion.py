import sqlite3

from sqlite3 import Error

def sql_connection():

    try:
        con = sqlite3.connect('Receta')

        print("La conexión fue exitosa a la base Receta")

    except Error:

        print(Error)

    finally:

        con.close()

sql_connection()
