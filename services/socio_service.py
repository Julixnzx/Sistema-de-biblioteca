from database.conexion import obtener_conexion

def registrar_socio_db(nombre, dni):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO socios (nombre, dni) VALUES (?, ?)", (nombre, dni))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False

def listar_socios():
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, nombre, dni FROM socios")
    filas = cursor.fetchall()
    conn.close()
    
    # Formateamos los datos para que el menú los muestre lindos
    lista_socios = []
    for fila in filas:
        lista_socios.append(f"ID: {fila[0]} | Nombre: {fila[1]} | DNI: {fila[2]}")
        
    return lista_socios