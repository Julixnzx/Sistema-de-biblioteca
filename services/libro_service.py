from models.libro import Libro
from repositories.libro_repository import agregar_libro


def registrar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    anio = int(input("Año: "))

    libro = Libro(
        titulo,
        autor,
        isbn,
        anio
    )

    agregar_libro(libro)

    print("Libro registrado correctamente")