# ============= FUNCIONES DE INVENTARIO =============

from Functions.Functions_Files import save_inventory
import Details

"""Función auxiliar para obtener entrada flotante válida"""
def get_valid_float(message, minimum_value=0):
    while True:
        try:
            value = float(input(message))
            if value < minimum_value:
                print(f"Error: The value must be at least {minimum_value}")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

"""Función auxiliar para obtener entrada entera válida"""
def get_valid_int(message, minimum_value=0):
    while True:
        try:
            value = int(input(message))
            if value < minimum_value:
                print(f"Error: The value must be at least {minimum_value}")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")

"""Función auxiliar para obtener entrada de texto no vacía"""
def get_input_not_empty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Error: This field cannot be empty.")

"""Muestra todos los productos en el inventario"""
def show_all_products():
    print(f"\n{Details.decorator}")
    print("CURRENT INVENTORY")
    print(Details.decorator)

    if not Details.inventory:
        print("There are no products in stock.")
        return


    for code, book in Details.inventory.items():
        print(f"\nCódigo: {code}")
        print(f"  Title: {book['title']}")
        print(f"  Author: {book['author']}")
        print(f"  Category: {book['category']}")
        print(f"  price: ${book['price']:.2f}")
        print(f"  Stock: {book['stock']} units")
    print(Details.decorator)

"""Agrega un nuevo book al inventario"""
def add_product():
    print("\n--- ADD NEW BOOK ---")

    try:
        code = get_input_not_empty("Book code (e.g., P006): ").upper()

        if code in Details.inventory:
            print("Error: This code already exists!")
            return

        title = get_input_not_empty("Book name: ")
        author = get_input_not_empty("Author: ")
        category = get_input_not_empty("Category: ")
        price = get_valid_float("price: $", minimum_value=0)
        stock = get_valid_int("Quantity stock: ", minimum_value=0)

        Details.inventory[code] = {
            "title": title,
            "author": author,
            "category": category,
            "price": price,
            "stock": stock
        }

        if save_inventory():
            print(f"Book '{title}' added and saved successfully!")
        else:
            print("Book added but could not be saved to the file.")

    except KeyboardInterrupt:
        print("\n\nOperation canceled by the user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

"""Actualiza un book existente"""
def update_product():
    print("\n--- UPDATE BOOK ---")

    if not Details.inventory:
        print("There are no book in inventory to update.")
        return

    code = input("Enter the code for the book to be updated: ").strip().upper()

    if code not in Details.inventory:
        print("Error: Product not found.")
        return

    book = Details.inventory[code]
    print(f"\nCurrent product: {book['title']}")
    print("Leave blank to keep the current value")

    try:
        new_name = input(f"New name [{book['title']}]: ").strip()
        if new_name:
            book['title'] = new_name

        new_price = input(f"New price [${book['price']:.2f}]: ").strip()
        if new_price:
            price = float(new_price)
            if price > 0:
                book['price'] = price
            else:
                print("Warning: The price must be positive. Keeping current value.")

        new_stock = input(f"New stock [{book['stock']}]: ").strip()
        if new_stock:
            stock = int(new_stock)
            if stock >= 0:
                book['stock'] = stock
            else:
                print("Warning: Stock cannot be negative. Maintaining current value.")

        if save_inventory():
            print("Book successfully updated and saved!")
        else:
            print("Book updated but could not be saved to the file.")

    except ValueError:
        print("Error: Invalid input. Update canceled.")
    except KeyboardInterrupt:
        print("\n\nOperation canceled by the user.")

"""Elimina un libro del inventario"""
def remove_product():
    print("\n--- DELETE BOOK ---")

    if not Details.inventory:
        print("There are no books in inventory to delete.")
        return

    code = input("Enter the code of the book to be removed:  ").strip().upper()

    if code not in Details.inventory:
        print("Error: Book not found.")
        return

    title_book = Details.inventory[code]['title']
    confirmation = input(f"Are you sure you want to delete '{title_book}'? (yes/no): ").lower()

    if confirmation in ['yes', 'y', 'yeah']:
        del Details.inventory[code]
        if save_inventory():
            print(f"Book '{title_book}' deleted and saved successfully!")
        else:
            print("Book deleted but could not be saved to the archive.")
    else:
        print("Deletion canceled.")