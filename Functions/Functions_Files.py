# ============= FUNCIONES DE GESTIÓN DE ARCHIVOS =============

import json
import os
import Details

"""Crea el directorio "Data" si no existe"""
def secure_data_directory():
    os.makedirs("../Datos", exist_ok=True)

"""Carga los Datos de inventario y sales desde archivos JSON"""
def load_data():
    secure_data_directory()

    # Cargar inventario
    if os.path.exists(Details.ARCHIVE_INVENTORY):
        try:
            with open(Details.ARCHIVE_INVENTORY, "r", encoding="utf-8") as file:
                Details.inventory = json.load(file)
            print(f"Loaded {len(Details.inventory)} book since {Details.ARCHIVE_INVENTORY}")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in inventory file: {e}")
            Details.inventory = {}
        except Exception as e:
            print(f"Error loading inventory: {e}")
            Details.inventory = {}
    else:
        print(f"File {Details.ARCHIVE_INVENTORY} not found. Creating initial inventory...")
        Details.inventory = create_initial_inventory()
        save_inventory()

    # Cargar sales
    if os.path.exists(Details.SALES_ARCHIVE):
        try:
            with open(Details.SALES_ARCHIVE, "r", encoding="utf-8") as file:
                Details.sales = json.load(file)
            print(f"Loaded {len(Details.sales)} sales since {Details.SALES_ARCHIVE}")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in sales file: {e}")
            Details.sales = []
        except Exception as e:
            print(f"Error loading sales: {e}")
            Details.sales = []
    else:
        print(f"File {Details.SALES_ARCHIVE} Not found. Starting with empty history.")
        Details.sales = []
        save_sales()

"""Guarda el inventario en archivo JSON"""
def save_inventory():
    secure_data_directory()
    try:
        with open(Details.ARCHIVE_INVENTORY, "w", encoding="utf-8") as file:
            json.dump(Details.inventory, file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving inventory: {e}")
        return False

"""Guarda las sales en archivo JSON"""
def save_sales():
    secure_data_directory()
    try:
        with open(Details.SALES_ARCHIVE, "w", encoding="utf-8") as file:
            json.dump(Details.sales, file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving sales: {e}")
        return False

"""Crea y retorna el inventario inicial con 5 productos"""
def create_initial_inventory():
    return {
        "P001": {
            "title": "Don Quijote de la Manchatitulo",
            "author": "Miguel de Cervantes Saavedra",
            "category": "Novela",
            "price": 89560,
            "stock": 10
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
