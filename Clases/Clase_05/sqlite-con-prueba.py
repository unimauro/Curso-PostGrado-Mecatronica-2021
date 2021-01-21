import sqlite3
from sqlite3 import Error

def sql_connection():    
    try:
        con = sqlite3.connect ('Empresa.db')
        return con            
    except Error:        
        print(Error)

def sql_tabla(con):
    cursorObj = con.cursor()    
    ## id integer
    ## nombre text
    ## dni integer
    ## salario real
    ## ingreso text
    cursorObj.execute("CREATE TABLE empleados (id integer PRIMARY KEY, nombre text, dni integer, salario real, ingreso text)")
    con.commit()

con = sql_connection()
#sql_tabla(con)
con.close()
