# 📚 Sistema de Gestión de Biblioteca

Una aplicación orientada a la administración integral y automatizada de bibliotecas. Permite gestionar de manera eficiente el catálogo de libros, el registro de socios y el control completo del flujo de préstamos y devoluciones.

---

## 🚀 Características Principales

* **📖 Gestión de Catálogo (Libros):** Alta, modificación, consulta y búsqueda avanzada de ejemplares por título, autor o categoría.
* **👥 Registro de Socios:** Control detallado de usuarios, historial de actividades y estado de habilitación.
* **🔄 Control de Préstamos y Devoluciones:** Registro de entregas, cálculo automático de fechas de devolución y control de disponibilidad de stock.
* **💾 Persistencia de Datos:** Almacenamiento seguro y estructurado mediante base de datos local para mantener la integridad del sistema.

---

## 🛠️ Arquitectura y Tecnologías

* **Lenguaje:** Python 3
* **Arquitectura:** Modular por capas (`models`, `services`, `repositories`, `menus`, `database`)
* **Persistencia:** Base de datos relacional local / Manejo de archivos estructurados

---

## 📂 Estructura del Proyecto

```text
Sistema de Biblioteca/
├── database/        # Configuración e inicialización de la base de datos
├── menus/           # Interfaz de usuario en consola y menús de navegación
├── models/          # Clases y modelos de dominio (Libro, Socio, Préstamo)
├── output/          # Reportes generados y archivos de salida
├── repositories/    # Capa de acceso y manipulación de datos
├── services/        # Lógica de negocio y validaciones del sistema
├── index.html       # Landing page / Documentación visual para GitHub Pages
├── main.py          # Punto de entrada principal de la aplicación
└── main.exe         # Ejecutable independiente para Windows
