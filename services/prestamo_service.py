from datetime import date
from repositories.prestamo_repository import registrar_prestamo

def prestar_libro():

    libro_id = int(input("ID Libro: "))
    socio_id = int(input("ID Socio: "))

    fecha = date.today().strftime("%d/%m/%Y")

    registrar_prestamo(
        libro_id,
        socio_id,
        fecha
    )

    print("Préstamo registrado correctamente")