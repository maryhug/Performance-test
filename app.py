from Functions.Functions_Files import load_data
from Functions.Functions_Inventory import add_product, update_product, remove_product, show_all_products
from Functions.Functions_Sale import record_sale, show_sales_history
from Functions.Functions_Report import best_selling_products, inventory_performance, sales_by_author

"""
    Muestra el menú principal
"""
def show_menu():
    print("\n" + "=" * 50)
    print("NATIONAL BOOKSTORE DIGITAL AREA - ROBUST SYSTEM")
    print("=" * 50)
    print("1. Show all books")
    print("2. Add new book")
    print("3. Update book")
    print("4. Delete book")
    print("5. Record sale")
    print("6. Show sales history")
    print("7. Top 3 best-selling books")
    print("8. Sales by brand")
    print("9. Inventory performance")
    print("0. Exit")
    print("=" * 50)

"""Función principal - ejecuta el programa"""
def main():
    print("Loading data from files...")

    # Cargar Datos desde archivos al iniciar
    try:
        load_data()
    except Exception as e:
        print(f"Error during initialization: {e}")
        print("Starting with empty data...")

    while True:
        show_menu()

        try:
            option = input("\nSelect an option: ").strip()

            if option == "1":
                show_all_products()
            elif option == "2":
                add_product()
            elif option == "3":
                update_product()
            elif option == "4":
                remove_product()
            elif option == "5":
                record_sale()
            elif option == "6":
                show_sales_history()
            elif option == "7":
                best_selling_products()
            elif option == "8":
                sales_by_author()
            elif option == "9":
                inventory_performance()
            elif option == "0":
                print("\n¡Thank you for using the system. See you later!")
                break
            else:
                print("Error: Invalid option. Please select a number from 0 to 9.")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by the user.")
            print("¡Thank you for using the system. See you later!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Please try again.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
