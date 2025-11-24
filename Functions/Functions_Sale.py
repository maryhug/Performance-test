from Functions.Functions_Files import save_inventory, save_sales
from datetime import datetime
import Details

"""Registra una nueva venta"""
def record_sale():
    print("\n--- REGISTER NEW SALE ---")

    if not Details.inventory:
        print("Error: There are no products in inventory. Please add products first.")
        return

    # Verificar si hay productos con stock
    available_products = {code: book for code, book in Details.inventory.items() if book['stock'] > 0}

    if not available_products:
        print("Error: No products are currently in stock.")
        return

    try:
        # Obtener información del customer
        customer = input("Client name: ").strip()
        if not customer:
            print("Error: The customer name cannot be empty.")
            return

        print("\nCustomer types:")
        print("1. Regular (0% discount)")
        print("2. VIP (10% discount)")
        print("3. Wholesaler (15% discount)")

        type_option = input("Select customer type (1-3): ").strip()

        customer_type_map = {
            "1": "regular",
            "2": "vip",
            "3": "wholesaler"
        }

        if type_option not in customer_type_map:
            print("Error: Invalid client type.")
            return

        customer_type = customer_type_map[type_option]

        # Mostrar productos disponibles
        print("\nAvailable products:")
        for code, book in available_products.items():
            print(f"  {code}: {book['title']} - ${book['price']:.2f} ({book['stock']} available)")

        # Obtener producto
        product_code = input("\nEnter the product code: ").strip().upper()

        if product_code not in Details.inventory:
            print("Error: Product not found.")
            return

        book = Details.inventory[product_code]

        if book['stock'] == 0:
            print("Error: This product is currently out of stock.")
            return

        # Obtener quantity
        try:
            quantity = int(input("Quantity to sell: "))
        except ValueError:
            print("Error: Please enter a valid integer for the quantity.")
            return

        if quantity <= 0:
            print("Error: The amount must be greater than 0.")
            return

        if quantity > book['stock']:
            print(f"Error: Insufficient stock. There are only {book['stock']} units available.")
            return

        # Calcular prices
        discount_percentage = Details.customer_discounts[customer_type]
        unit_price = book['price']
        subtotal = unit_price * quantity
        discount_amount = subtotal * (discount_percentage / 100)
        total = subtotal - discount_amount

        # Actualizar stock
        book['stock'] -= quantity

        # Registrar venta
        sale = {
            "customer": customer,
            "customer_type": customer_type,
            "code_product": product_code,
            "name_book": book['title'],
            "author": book['author'],
            "quantity": quantity,
            "price_unitario": unit_price,
            "discount_percentage”": discount_percentage,
            "total": total,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        Details.sales.append(sale)

        # Guardar tanto inventario como ventas
        saved_inventory = save_inventory()
        saved_sales = save_sales()

        # Mostrar recibo
        print(f"\n{Details.small}")
        print("RECIBO DE VENTA")
        print(Details.small)
        print(f"customer: {customer} ({customer_type.upper()})")
        print(f"Producto: {book['title']}")
        print(f"quantity: {quantity}")
        print(f"unit_price: ${unit_price:.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount_percentage ({discount_percentage}%): -${discount_amount:.2f}")
        print(f"TOTAL: ${total:.2f}")
        print(f"Date: {sale['date']}")
        print(Details.small)

        if saved_inventory and saved_sales:
            print("Sale successfully registered and saved!")
        else:
            print("Sale registered but there were problems saving to the files.")

    except KeyboardInterrupt:
        print("\n\nOperation canceled by the user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

"""Muestra todas las ventas realizadas"""
def show_sales_history():
    print(f"\n{Details.decorator}")
    print("SALES HISTORY")
    print(Details.decorator)

    if not Details.sales:
        print("No sales have been recorded yet.")
        return

    total_income = 0
    for i, venta in enumerate(Details.sales, 1):
        print(f"\Sale #{i}")
        print(f"  Customer: {venta['customer']} ({venta['customer_type']})")
        print(f"  Producto: {venta['name_book']}")
        print(f"  Quantity: {venta['quantity']}")
        print(f"  Total: ${venta['total']:.2f}")
        print(f"  Date: {venta['date']}")
        total_income += venta['total']

    print(f"\n{Details.decorator}")
    print(f"Total Revenue: ${total_income:.2f}")
    print(Details.decorator)