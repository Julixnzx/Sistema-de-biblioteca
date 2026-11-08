import sys
import os

if getattr(sys, 'frozen', False):
    ruta_raiz = sys._MEIPASS
else:
    ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

from services.socio_service import registrar_socio
from repositories.socio_repository import listar_socios

# ... (El resto del código con la función "def menu_socios():" abajo queda igual)