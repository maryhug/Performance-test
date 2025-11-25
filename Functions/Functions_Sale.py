from Functions.Functions_Files import save_inventory, save_sales  # Importa funciones de guardado
from datetime import datetime  # Módulo para trabajar con fechas y horas
import Details  # Módulo con variables globales del sistema

"""Registra una nueva venta"""


def record_sale():
    print("\n--- REGISTER NEW SALE ---")

    # ========== VALIDACIONES INICIALES ==========
    # Verifica que exista inventario
    if not Details.inventory:
        print("Error: There are no products in inventory. Please add products first.")
        return

    # Filtra solo los productos que tienen stock disponible
    # Usa comprensión de diccionario para crear un nuevo diccionario
    available_products = {code: book for code, book in Details.inventory.items() if book['stock'] > 0}

    # Verifica que haya productos con stock
    if not available_products:
        print("Error: No products are currently in stock.")
        return

    try:
        # ========== OBTENER INFORMACIÓN DEL CLIENTE ==========
        # Solicita el nombre del cliente y elimina espacios en blanco
        customer = input("Client name: ").strip()
        # Valida que no esté vacío
        if not customer:
            print("Error: The customer name cannot be empty.")
            return

        # ========== SELECCIONAR TIPO DE CLIENTE ==========
        # Muestra menú con tipos de cliente y sus descuentos
        print("\nCustomer types:")
        print("1. Regular (0% discount)")
        print("2. VIP (10% discount)")
        print("3. Wholesaler (15% discount)")

        type_option = input("Select customer type (1-3): ").strip()

        # Diccionario que mapea opciones numéricas a tipos de cliente
        customer_type_map = {
            "1": "regular",
            "2": "vip",
            "3": "wholesaler"
        }

        # Valida que la opción sea válida
        if type_option not in customer_type_map:
            print("Error: Invalid client type.")
            return

        # Obtiene el tipo de cliente basado en la selección
        customer_type = customer_type_map[type_option]

        # ========== MOSTRAR PRODUCTOS DISPONIBLES ==========
        print("\nAvailable products:")
        # Itera sobre productos con stock
        for code, book in available_products.items():
            # Muestra código, título, precio y stock disponible
            print(f"  {code}: {book['title']} - ${book['price']:.2f} ({book['stock']} available)")

        # ========== SELECCIONAR PRODUCTO ==========
        # Solicita el código del producto y lo convierte a mayúsculas
        product_code = input("\nEnter the product code: ").strip().upper()

        # Verifica que el producto exista en el inventario
        if product_code not in Details.inventory:
            print("Error: Product not found.")
            return

        # Obtiene referencia al libro seleccionado
        book = Details.inventory[product_code]

        # Doble verificación de stock (aunque ya se filtró antes)
        if book['stock'] == 0:
            print("Error: This product is currently out of stock.")
            return

        # ========== OBTENER CANTIDAD A VENDER ==========
        try:
            # Intenta convertir la entrada a entero
            quantity = int(input("Quantity to sell: "))
        except ValueError:
            # Captura error si no es un número válido
            print("Error: Please enter a valid integer for the quantity.")
            return

        # Valida que la cantidad sea positiva
        if quantity <= 0:
            print("Error: The amount must be greater than 0.")
            return

        # Verifica que haya suficiente stock
        if quantity > book['stock']:
            print(f"Error: Insufficient stock. There are only {book['stock']} units available.")
            return

        # ========== CALCULAR PRECIOS Y DESCUENTOS ==========
        # Obtiene el porcentaje de descuento según tipo de cliente
        discount_percentage = Details.customer_discounts[customer_type]
        # Precio unitario del producto
        unit_price = book['price']
        # Subtotal sin descuento
        subtotal = unit_price * quantity
        # Monto del descuento en dinero
        discount_amount = subtotal * (discount_percentage / 100)
        # Total final después del descuento
        total = subtotal - discount_amount

        # ========== ACTUALIZAR INVENTARIO ==========
        # Reduce el stock del producto vendido
        book['stock'] -= quantity

        # ========== REGISTRAR LA VENTA ==========
        # Crea un diccionario con toda la información de la venta
        sale = {
            "customer": customer,  # Nombre del cliente
            "customer_type": customer_type,  # Tipo de cliente
            "code_product": product_code,  # Código del producto
            "name_book": book['title'],  # Título del libro
            "author": book['author'],  # Autor del libro
            "quantity": quantity,  # Cantidad vendida
            "price_unitario": unit_price,  # Precio unitario
            "discount_percentage": discount_percentage,  # Porcentaje de descuento aplicado
            "total": total,  # Total pagado
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha y hora actual
        }

        # Agrega la venta a la lista de ventas
        Details.sales.append(sale)

        # ========== GUARDAR DATOS ==========
        # Guarda tanto el inventario actualizado como las ventas
        saved_inventory = save_inventory()
        saved_sales = save_sales()

        # ========== MOSTRAR RECIBO ==========
        print(f"\n{Details.small}")
        print("RECIBO DE VENTA")
        print(Details.small)
        print(f"customer: {customer} ({customer_type.upper()})")
        print(f"Producto: {book['title']}")
        print(f"quantity: {quantity}")
        print(f"unit_price: ${unit_price:.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        # Muestra el descuento aplicado
        print(f"Discount_percentage ({discount_percentage}%): -${discount_amount:.2f}")
        print(f"TOTAL: ${total:.2f}")
        print(f"Date: {sale['date']}")
        print(Details.small)

        # Verifica que ambos archivos se guardaron correctamente
        if saved_inventory and saved_sales:
            print("Sale successfully registered and saved!")
        else:
            print("Sale registered but there were problems saving to the files.")

    except KeyboardInterrupt:
        # Captura si el usuario presiona Ctrl+C
        print("\n\nOperation canceled by the user.")
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Unexpected error: {e}")


"""Muestra todas las ventas realizadas"""


def show_sales_history():
    # Imprime encabezado decorado
    print(f"\n{Details.decorator}")
    print("SALES HISTORY")
    print(Details.decorator)

    # Verifica si hay ventas registradas
    if not Details.sales:
        print("No sales have been recorded yet.")
        return

    # ========== MOSTRAR CADA VENTA ==========
    # Variable acumuladora para calcular ingresos totales
    total_income = 0

    # enumerate() agrega un contador automático comenzando en 1
    for i, venta in enumerate(Details.sales, 1):
        # Muestra información resumida de cada venta
        print(f"\nSale #{i}")
        print(f"  Customer: {venta['customer']} ({venta['customer_type']})")
        print(f"  Producto: {venta['name_book']}")
        print(f"  Quantity: {venta['quantity']}")
        print(f"  Total: ${venta['total']:.2f}")
        print(f"  Date: {venta['date']}")

        # Acumula el total de ingresos
        total_income += venta['total']

    # ========== MOSTRAR RESUMEN TOTAL ==========
    print(f"\n{Details.decorator}")
    print(f"Total Revenue: ${total_income:.2f}")
    print(Details.decorator)