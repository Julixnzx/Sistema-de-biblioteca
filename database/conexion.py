import sqlite3
import os

def obtener_conexion():
    # Creamos la base de datos en la carpeta raíz del proyecto
    ruta_db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "biblioteca.db")
    
    conn = sqlite3.connect(ruta_db)
    cursor = conn.cursor()
    
    # Creamos la tabla de socios si es la primera vez que se ejecuta
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS socios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            dni TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    return conn