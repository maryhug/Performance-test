# ============= FUNCIONES DE REPORTES =============

import Details as data

""" Muestra los 3 productos más vendidos """
def best_selling_products():
    print(f"\n{data.small}")
    print("TOP 3 BEST-SELLING PRODUCTS")
    print(data.small)

    if not data.sales:
        print("No sales data available.")
        return

    # Contar quantityes vendidas por producto
    product_sales = {}

    for sale in data.sales:
        product_name = sale['name_book']
        quantity = sale['quantity']

        if product_name in product_sales:
            product_sales[product_name] += quantity
        else:
            product_sales[product_name] = quantity

    # Ordenar por quantity (descendente)
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

    # Mostrar top 3
    if not sorted_products:
        print("No products sold yet.")
        return

    for i, (book, quantity) in enumerate(sorted_products[:3], 1):
        print(f"{i}. {book} - {quantity} units sold")

    print(data.small)

""" Muestra las ventas agrupadas por marca """
def sales_by_author():
    print(f"\n{data.small}")
    print("SALES BY AUTHOR")
    print(data.small)

    if not data.sales:
        print("No sales data available.")
        return

    # Agrupar ventas por marca
    sales_author = {}

    for sale in data.sales:
        author = sale['author']
        total = sale['total']

        if author in sales_author:
            sales_author[author] += total
        else:
            sales_author[author] = total

    # Mostrar resultados ordenados por nombre de marca
    if not sales_author:
        print("No author data available.")
        return

    for author, total in sorted(sales_author.items()):
        print(f"{author}: ${total:.2f}")

    print(data.small)

""" Muestra el rendimiento del inventario basado en ventas """
def inventory_performance():
    print(f"\n{data.decorator}")
    print("INVENTORY PERFORMANCE")
    print(data.decorator)

    if not data.inventory:
        print("No inventory data available.")
        return

    # Calcular total vendido por producto
    sold_by_book = {}

    for sale in data.sales:
        code = sale['code_product']
        quantity = sale['quantity']

        if code in sold_by_book:
            sold_by_book[code] += quantity
        else:
            sold_by_book[code] = quantity

    # Mostrar rendimiento
    total_inventory_value = 0
    total_revenue_generated = 0

    for code, book in data.inventory.items():
        sold = sold_by_book.get(code, 0)
        income = sold * book['price']
        inventory_value = book['stock'] * book['price']

        total_inventory_value += inventory_value
        total_revenue_generated += income

        print(f"\n{book['title']} ({code}):")
        print(f"  Current stock: {book['stock']} units")
        print(f"  Units sold: {sold}")
        print(f"  Total revenue: ${income:.2f}")
        print(f"  Inventory value: ${inventory_value:.2f}")

        # Indicador de rendimiento
        if sold == 0:
            print(f" No sales yet")
        elif book['stock'] < 5:
            print(f" Low stock - Consider reordering")
        else:
            print(f" Good")

    print(f"\n{data.decorator}")
    print(f"Total inventory value: ${total_inventory_value:.2f}")
    print(f"Total revenue generated: ${total_revenue_generated:.2f}")
    print(data.decorator)