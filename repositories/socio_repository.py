from database.conexion import obtener_conexion

def agregar_socio(socio):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO socios(nombre, apellido, dni, telefono)
    VALUES (?, ?, ?, ?)
    """, (
        socio.nombre,
        socio.apellido,
        socio.dni,
        socio.telefono
    ))

    conn.commit()
    conn.close()


def listar_socios():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM socios")

    socios = cursor.fetchall()

    conn.close()

    return socios