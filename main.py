import sys
import os

# Bloque definitivo para que el .exe encuentre los módulos internos y no se cierre
if getattr(sys, 'frozen', False):
    ruta_raiz = sys._MEIPASS
else:
    ruta_raiz = os.path.dirname(os.path.abspath(__file__))

if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

# Importación limpia sin duplicar
from menus import menu_socios

def main():
    print("=== SISTEMA DE BIBLIOTECA ===")
    menu_socios.menu_socios()
    
    # ESTO EVITA QUE SE CIERRE SOLO AL TERMINAR:
    print("\n" + "="*29)
    input("Presiona ENTER para salir...")

if __name__ == "__main__":
    main()