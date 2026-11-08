from database.conexion import obtener_conexion


def agregar_libro(libro):
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO libros(titulo, autor, isbn, anio)
    VALUES (?, ?, ?, ?)
    """, (
        libro.titulo,
        libro.autor,
        libro.isbn,
        libro.anio
    ))

    conn.commit()
    conn.close()


def listar_libros():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM libros")

    libros = cursor.fetchall()

    conn.close()

    return libros