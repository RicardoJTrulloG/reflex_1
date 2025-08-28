import sqlite3

def connect_db():
    # Conexión a base de datos
    con = sqlite3.connect("reflex_db_1.db")
    return con

    #cur = con.cursor() # Nos sirve para realizar peticiones a la db
    #cur.execute("CREATE TABLE usuarios(nombre  VARCHAR(20), email VARCHAR(20), genero VARCHAR(20))")

#connect_db()