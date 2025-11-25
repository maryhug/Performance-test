# ============= FUNCIONES DE GESTIÓN DE ARCHIVOS =============

import json  # Módulo para trabajar con archivos JSON (JavaScript Object Notation)
import os  # Módulo para operaciones del sistema operativo (crear carpetas, verificar archivos)
import Details  # Módulo personalizado que contiene variables globales del proyecto

"""Crea el directorio "Data" si no existe"""


def secure_data_directory():
    # makedirs() crea el directorio "./Datos"
    # exist_ok=True evita error si el directorio ya existe
    os.makedirs("./Datos", exist_ok=True)


"""Carga los Datos de inventario y sales desde archivos JSON"""


def load_data():
    # Primero asegura que exista el directorio de datos
    secure_data_directory()

    # ========== CARGAR INVENTARIO ==========
    # Verifica si existe el archivo de inventario
    if os.path.exists(Details.ARCHIVE_INVENTORY):
        try:
            # Abre el archivo en modo lectura con codificación UTF-8
            # 'with' asegura que el archivo se cierre automáticamente
            with open(Details.ARCHIVE_INVENTORY, "r", encoding="utf-8") as file:
                # json.load() convierte el JSON del archivo a diccionario de Python
                Details.inventory = json.load(file)
            # Muestra cuántos libros se cargaron
            print(f"Loaded {len(Details.inventory)} book since {Details.ARCHIVE_INVENTORY}")

        except json.JSONDecodeError as e:
            # Captura errores si el JSON está mal formateado
            print(f"Error: Invalid JSON format in inventory file: {e}")
            Details.inventory = {}  # Inicializa inventario vacío

        except Exception as e:
            # Captura cualquier otro error al cargar
            print(f"Error loading inventory: {e}")
            Details.inventory = {}

    else:
        # Si no existe el archivo, crea un inventario inicial
        print(f"File {Details.ARCHIVE_INVENTORY} not found. Creating initial inventory...")
        Details.inventory = create_initial_inventory()
        save_inventory()  # Guarda el inventario inicial en archivo

    # ========== CARGAR VENTAS ==========
    # Verifica si existe el archivo de ventas
    if os.path.exists(Details.SALES_ARCHIVE):
        try:
            # Abre y carga el archivo de ventas
            with open(Details.SALES_ARCHIVE, "r", encoding="utf-8") as file:
                Details.sales = json.load(file)
            # Muestra cuántas ventas se cargaron
            print(f"Loaded {len(Details.sales)} sales since {Details.SALES_ARCHIVE}")

        except json.JSONDecodeError as e:
            # Error si el JSON de ventas está corrupto
            print(f"Error: Invalid JSON format in sales file: {e}")
            Details.sales = []  # Inicializa lista vacía

        except Exception as e:
            # Captura otros errores
            print(f"Error loading sales: {e}")
            Details.sales = []

    else:
        # Si no existe el archivo de ventas, crea uno nuevo vacío
        print(f"File {Details.SALES_ARCHIVE} Not found. Starting with empty history.")
        Details.sales = []  # Inicializa lista vacía de ventas
        save_sales()  # Crea el archivo de ventas vacío


"""Guarda el inventario en archivo JSON"""


def save_inventory():
    # Asegura que exista el directorio antes de guardar
    secure_data_directory()
    try:
        # Abre el archivo en modo escritura
        with open(Details.ARCHIVE_INVENTORY, "w", encoding="utf-8") as file:
            # json.dump() convierte el diccionario de Python a formato JSON
            # indent=4: formatea el JSON con indentación de 4 espacios (más legible)
            # ensure_ascii=False: permite caracteres especiales (tildes, ñ, etc.)
            json.dump(Details.inventory, file, indent=4, ensure_ascii=False)
        return True  # Retorna True si se guardó exitosamente

    except Exception as e:
        # Captura errores al guardar
        print(f"Error saving inventory: {e}")
        return False  # Retorna False si hubo error


"""Guarda las sales en archivo JSON"""


def save_sales():
    # Similar a save_inventory() pero para ventas
    secure_data_directory()
    try:
        # Abre archivo de ventas en modo escritura
        with open(Details.SALES_ARCHIVE, "w", encoding="utf-8") as file:
            # Guarda la lista de ventas en formato JSON
            json.dump(Details.sales, file, indent=4, ensure_ascii=False)
        return True

    except Exception as e:
        print(f"Error saving sales: {e}")
        return False


"""Crea y retorna el inventario inicial con 5 productos"""


def create_initial_inventory():
    # Retorna un diccionario predefinido con 5 libros de ejemplo
    # Cada libro tiene: título, autor, categoría, precio y stock
    return {
        "P001": {
            "title": "Don Quijote de la Manchatitulo",
            "author": "Miguel de Cervantes Saavedra",
            "category": "Novela",
            "price": 89560,  # Precio como número entero
            "stock": 10  # Cantidad disponible
        },
        "P002": {
            "title": "Cien años de soledad",
            "author": "Gabriel Garcia Marquez",
            "category": "Realismo mágico",
            "price": 6000,
            "stock": 89
        },
        "P003": {
            "title": "El principito",
            "author": "Antoine de Saint-Exupéry",
            "category": "Literatura infantil",
            "price": 894500,
            "stock": 78
        },
        "P004": {
            "title": "La Odisea",
            "author": "Homero",
            "category": "Epico",
            "price": 894500,
            "stock": 89
        },
        "P005": {
            "title": "Harry Potter",
            "author": "J. K. Rowling",
            "category": "Literatura fantástica",
            "price": 894500,
            "stock": 9
        }
    }