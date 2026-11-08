from services.prestamo_service import prestar_libro
from repositories.prestamo_repository import listar_prestamos

def menu_prestamos():

    while True:

        print("\n=== PRÉSTAMOS ===")
        print("1. Registrar préstamo")
        print("2. Ver préstamos")
        print("3. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            prestar_libro()

        elif opcion == "2":

            prestamos = listar_prestamos()

            for prestamo in prestamos:
                print(prestamo)

        elif opcion == "3":
            break