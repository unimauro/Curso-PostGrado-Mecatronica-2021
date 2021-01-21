import sqlite3

from sqlite3 import Error

def sql_conexion():

    try:
        con=sqlite3.connect("casa_domotica.db")

        return con

    except Error:

        print(Error)

def sql_tabla(con):

    cursorObj = con.cursor()

    ## id integer
    ## nombre text
    ## ubicacion text
    ## estado integer
    ## agregado text
    cursorObj.execute("CREATE TABLE dispositivos3(id integer PRIMARY KEY, nombre text, ubicacion text, estado integer, agregado text )")

    con.commit()

def sql_insert(con):

    cursorObj = con.cursor()
    cursorObj.execute("insert into dispositivos values (3, 'google tv', 'comedor', 1, '2021-01-13')")
    con.commit()

def sql_lectura(con):
    
    cursorObj = con.cursor()
    cursorObj.execute("select * from dispositivos")
    datos=cursorObj.fetchall()
    for i in datos:
        print(i)
    

def sql_cerrar(con):

    con.close()    


con = sql_conexion()

#sql_tabla(con)

sql_insert(con)

sql_lectura(con)

sql_cerrar(con)

