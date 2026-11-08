from database.conexion import obtener_conexion

def registrar_prestamo(libro_id, socio_id, fecha):

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO prestamos(
        libro_id,
        socio_id,
        fecha_prestamo,
        estado
    )
    VALUES (?, ?, ?, ?)
    """, (
        libro_id,
        socio_id,
        fecha,
        "ACTIVO"
    ))

    cursor.execute("""
    UPDATE libros
    SET disponible = 0
    WHERE id = ?
    """, (libro_id,))

    conn.commit()
    conn.close()


def listar_prestamos():

    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        p.id,
        l.titulo,
        s.nombre,
        s.apellido,
        p.fecha_prestamo,
        p.estado
    FROM prestamos p
    JOIN libros l ON p.libro_id = l.id
    JOIN socios s ON p.socio_id = s.id
    """)

    prestamos = cursor.fetchall()

    conn.close()

    return prestamos