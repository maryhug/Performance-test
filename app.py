# ========== IMPORTACIONES ==========
# Importa la función para cargar datos desde archivos
from Functions.Functions_Files import load_data

# Importa todas las funciones relacionadas con gestión de inventario
from Functions.Functions_Inventory import add_product, update_product, remove_product, show_all_products

# Importa funciones de gestión de ventas
from Functions.Functions_Sale import record_sale, show_sales_history

# Importa funciones de generación de reportes y estadísticas
from Functions.Functions_Report import best_selling_products, inventory_performance, sales_by_author

"""
    Muestra el menú principal del sistema
"""


def show_menu():
    # Imprime encabezado con separador de 50 caracteres '='
    print("\n" + "=" * 50)
    print("NATIONAL BOOKSTORE DIGITAL AREA - ROBUST SYSTEM")
    print("=" * 50)

    # Lista todas las opciones disponibles del menú
    print("1. Show all books")  # Mostrar inventario completo
    print("2. Add new book")  # Agregar nuevo libro
    print("3. Update book")  # Actualizar información de libro
    print("4. Delete book")  # Eliminar libro del inventario
    print("5. Record sale")  # Registrar una nueva venta
    print("6. Show sales history")  # Ver historial de ventas
    print("7. Top 3 best-selling books")  # Reporte de más vendidos
    print("8. Sales by brand")  # Ventas agrupadas por autor/marca
    print("9. Inventory performance")  # Análisis de rendimiento
    print("0. Exit")  # Salir del programa
    print("=" * 50)


"""Función principal - punto de entrada del programa"""


def main():
    print("Loading data from files...")

    # ========== INICIALIZACIÓN DEL SISTEMA ==========
    # Intenta cargar los datos almacenados (inventario y ventas)
    try:
        load_data()  # Carga datos desde archivos JSON
    except Exception as e:
        # Si hay algún error al cargar, captura la excepción
        print(f"Error during initialization: {e}")
        print("Starting with empty data...")
        # El programa continúa con datos vacíos si falla la carga

    # ========== BUCLE PRINCIPAL DEL PROGRAMA ==========
    # Bucle infinito que mantiene el programa ejecutándose
    while True:
        # Muestra el menú en cada iteración
        show_menu()

        try:
            # ========== CAPTURA DE ENTRADA DEL USUARIO ==========
            # Solicita al usuario que seleccione una opción
            # .strip() elimina espacios en blanco al inicio y final
            option = input("\nSelect an option: ").strip()

            # ========== ESTRUCTURA DE CONTROL CONDICIONAL ==========
            # Evalúa la opción seleccionada y ejecuta la función correspondiente

            if option == "1":
                # Opción 1: Mostrar todos los libros en inventario
                show_all_products()

            elif option == "2":
                # Opción 2: Agregar un nuevo libro al inventario
                add_product()

            elif option == "3":
                # Opción 3: Actualizar información de un libro existente
                update_product()

            elif option == "4":
                # Opción 4: Eliminar un libro del inventario
                remove_product()

            elif option == "5":
                # Opción 5: Registrar una nueva venta
                record_sale()

            elif option == "6":
                # Opción 6: Mostrar historial completo de ventas
                show_sales_history()

            elif option == "7":
                # Opción 7: Generar reporte de los 3 libros más vendidos
                best_selling_products()

            elif option == "8":
                # Opción 8: Mostrar ventas agrupadas por autor
                sales_by_author()

            elif option == "9":
                # Opción 9: Análisis de rendimiento del inventario
                inventory_performance()

            elif option == "0":
                # Opción 0: Salir del programa
                print("\n¡Thank you for using the system. See you later!")
                break  # Rompe el bucle while, terminando el programa

            else:
                # Opción inválida: muestra mensaje de error
                print("Error: Invalid option. Please select a number from 0 to 9.")

        except KeyboardInterrupt:
            # ========== MANEJO DE INTERRUPCIÓN POR TECLADO ==========
            # Captura cuando el usuario presiona Ctrl+C
            print("\n\nProgram interrupted by the user.")
            print("¡Thank you for using the system. See you later!")
            break  # Sale del bucle y termina el programa

        except Exception as e:
            # ========== MANEJO DE ERRORES GENERALES ==========
            # Captura cualquier otro error inesperado durante la ejecución
            print(f"Unexpected error: {e}")
            print("Please try again.")
            # El programa NO termina, permite al usuario intentar nuevamente


# ========== PUNTO DE ENTRADA DEL PROGRAMA ==========
# Esta condición verifica si el script se está ejecutando directamente
# (no importado como módulo desde otro archivo)
if __name__ == "__main__":
    # Si se ejecuta directamente, llama a la función main()
    main()