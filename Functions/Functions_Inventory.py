import Details
from Functions.Functions_Files import save_inventory

# ============================================================================
# FUNCIONES AUXILIARES DE VALIDACIÓN
# ============================================================================

"""Función auxiliar para obtener entrada flotante válida"""
def get_valid_float(message, minimum_value=0):
    # Bucle infinito hasta obtener un valor válido
    while True:
        try:
            # Intenta convertir la entrada del usuario a float
            value = float(input(message))
            # Verifica que el valor sea mayor o igual al mínimo permitido
            if value < minimum_value:
                print(f"Error: The value must be at least {minimum_value}")
                continue
            # Si todo está correcto, retorna el valor
            return value
        except ValueError:
            # Captura errores si el usuario no ingresa un número válido
            print("Error: Please enter a valid number.")

"""Función auxiliar para obtener entrada entera válida"""
def get_valid_int(message, minimum_value=0):
    # Similar a get_valid_float pero para números enteros
    while True:
        try:
            # Convierte la entrada a entero
            value = int(input(message))
            # Verifica el valor mínimo
            if value < minimum_value:
                print(f"Error: The value must be at least {minimum_value}")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")

"""Función auxiliar para obtener entrada de texto no vacía"""
def get_input_not_empty(message):
    # Asegura que el usuario ingrese algo y no deje el campo vacío
    while True:
        # strip() elimina espacios en blanco al inicio y final
        value = input(message).strip()
        # Verifica que haya contenido después de eliminar espacios
        if value:
            return value
        print("Error: This field cannot be empty.")

# ============================================================================
# FUNCIONES PRINCIPALES DEL SISTEMA DE INVENTARIO
# ============================================================================

"""Muestra todos los productos en el inventario"""
def show_all_products():
    # Imprime un encabezado decorado
    print(f"\n{Details.decorator}")
    print("CURRENT INVENTORY")
    print(Details.decorator)

    # Verifica si el inventario está vacío
    if not Details.inventory:
        print("There are no products in stock.")
        return

    # Itera sobre cada libro en el diccionario de inventario
    # items() devuelve pares clave-valor (código, información del libro)
    for code, book in Details.inventory.items():
        # Imprime toda la información del libro
        print(f"\nCódigo: {code}")
        print(f"  Title: {book['title']}")
        print(f"  Author: {book['author']}")
        print(f"  Category: {book['category']}")
        # Formatea el precio con 2 decimales
        print(f"  price: ${book['price']:.2f}")
        print(f"  Stock: {book['stock']} units")
    print(Details.decorator)

"""Agrega un nuevo book al inventario"""
def add_product():
    print("\n--- ADD NEW BOOK ---")

    try:
        # Solicita el código del libro y lo convierte a mayúsculas
        code = get_input_not_empty("Book code (e.g., P006): ").upper()

        # Verifica que el código no exista ya en el inventario
        if code in Details.inventory:
            print("Error: This code already exists!")
            return

        # Solicita todos los datos del libro usando las funciones de validación
        title = get_input_not_empty("Book name: ")
        author = get_input_not_empty("Author: ")
        category = get_input_not_empty("Category: ")
        price = get_valid_float("price: $", minimum_value=0)
        stock = get_valid_int("Quantity stock: ", minimum_value=0)

        # Crea un nuevo diccionario con la información del libro
        # y lo agrega al inventario usando el código como clave
        Details.inventory[code] = {
            "title": title,
            "author": author,
            "category": category,
            "price": price,
            "stock": stock
        }

        # Intenta guardar el inventario en un archivo
        if save_inventory():
            print(f"Book '{title}' added and saved successfully!")
        else:
            print("Book added but could not be saved to the file.")

    except KeyboardInterrupt:
        # Captura si el usuario presiona Ctrl+C
        print("\n\nOperation canceled by the user.")
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Unexpected error: {e}")

"""Actualiza un book existente"""
def update_product():
    print("\n--- UPDATE BOOK ---")

    # Verifica que haya libros en el inventario
    if not Details.inventory:
        print("There are no book in inventory to update.")
        return

    # Solicita el código del libro a actualizar
    code = input("Enter the code for the book to be updated: ").strip().upper()

    # Verifica que el código exista
    if code not in Details.inventory:
        print("Error: Product not found.")
        return

    # Obtiene referencia al libro a actualizar
    book = Details.inventory[code]
    print(f"\nCurrent product: {book['title']}")
    print("Leave blank to keep the current value")

    try:
        # Permite actualizar el nombre (si se deja en blanco, mantiene el actual)
        new_name = input(f"New name [{book['title']}]: ").strip()
        if new_name:
            book['title'] = new_name

        # Permite actualizar el precio
        new_price = input(f"New price [${book['price']:.2f}]: ").strip()
        if new_price:
            price = float(new_price)
            # Valida que el precio sea positivo
            if price > 0:
                book['price'] = price
            else:
                print("Warning: The price must be positive. Keeping current value.")

        # Permite actualizar el stock
        new_stock = input(f"New stock [{book['stock']}]: ").strip()
        if new_stock:
            stock = int(new_stock)
            # Valida que el stock no sea negativo
            if stock >= 0:
                book['stock'] = stock
            else:
                print("Warning: Stock cannot be negative. Maintaining current value.")

        # Guarda los cambios
        if save_inventory():
            print("Book successfully updated and saved!")
        else:
            print("Book updated but could not be saved to the file.")

    except ValueError:
        # Error si el usuario ingresa un tipo de dato incorrecto
        print("Error: Invalid input. Update canceled.")
    except KeyboardInterrupt:
        print("\n\nOperation canceled by the user.")

"""Elimina un libro del inventario"""
def remove_product():
    print("\n--- DELETE BOOK ---")

    # Verifica que haya libros para eliminar
    if not Details.inventory:
        print("There are no books in inventory to delete.")
        return

    # Solicita el código del libro a eliminar
    code = input("Enter the code of the book to be removed:  ").strip().upper()

    # Verifica que el código exista
    if code not in Details.inventory:
        print("Error: Book not found.")
        return

    # Guarda el título para mostrarlo en el mensaje de confirmación
    title_book = Details.inventory[code]['title']
    # Solicita confirmación antes de eliminar
    confirmation = input(f"Are you sure you want to delete '{title_book}'? (yes/no): ").lower()

    # Si el usuario confirma, elimina el libro
    if confirmation in ['yes', 'y', 'yeah']:
        # Elimina la entrada del diccionario usando del
        del Details.inventory[code]
        # Guarda los cambios
        if save_inventory():
            print(f"Book '{title_book}' deleted and saved successfully!")
        else:
            print("Book deleted but could not be saved to the archive.")
    else:
        print("Deletion canceled.")