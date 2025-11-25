# ============= FUNCIONES DE REPORTES =============

import Details as data  # Importa el módulo Details con alias 'data' para mayor claridad

""" Muestra los 3 productos más vendidos """


def best_selling_products():
    # Imprime encabezado del reporte
    print(f"\n{data.small}")
    print("TOP 3 BEST-SELLING PRODUCTS")
    print(data.small)

    # Verifica si hay datos de ventas disponibles
    if not data.sales:
        print("No sales data available.")
        return

    # ========== CONTAR CANTIDADES VENDIDAS ==========
    # Diccionario para acumular las cantidades vendidas de cada producto
    product_sales = {}

    # Itera sobre todas las ventas registradas
    for sale in data.sales:
        # Extrae el nombre del libro de la venta actual
        product_name = sale['name_book']
        # Extrae la cantidad vendida
        quantity = sale['quantity']

        # Si el producto ya está en el diccionario, suma la cantidad
        if product_name in product_sales:
            product_sales[product_name] += quantity
        else:
            # Si es la primera vez que aparece, inicializa con la cantidad
            product_sales[product_name] = quantity

    # ========== ORDENAR PRODUCTOS ==========
    # sorted() ordena el diccionario por valor (cantidad vendida)
    # key=lambda x: x[1] indica que ordene por el segundo elemento de la tupla (cantidad)
    # reverse=True ordena de mayor a menor (descendente)
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

    # ========== MOSTRAR TOP 3 ==========
    # Verifica que haya productos vendidos
    if not sorted_products:
        print("No products sold yet.")
        return

    # enumerate() agrega un contador automático empezando en 1
    # [:3] toma solo los primeros 3 elementos de la lista
    for i, (book, quantity) in enumerate(sorted_products[:3], 1):
        print(f"{i}. {book} - {quantity} units sold")

    print(data.small)


""" Muestra las ventas agrupadas por marca """


def sales_by_author():
    # Imprime encabezado del reporte
    print(f"\n{data.small}")
    print("SALES BY AUTHOR")
    print(data.small)

    # Verifica si hay ventas disponibles
    if not data.sales:
        print("No sales data available.")
        return

    # ========== AGRUPAR VENTAS POR AUTOR ==========
    # Diccionario para acumular el total de ventas por autor
    sales_author = {}

    # Itera sobre cada venta
    for sale in data.sales:
        # Extrae el autor del libro vendido
        author = sale['author']
        # Extrae el monto total de esa venta
        total = sale['total']

        # Acumula el total de ventas para cada autor
        if author in sales_author:
            sales_author[author] += total
        else:
            # Inicializa si es la primera venta del autor
            sales_author[author] = total

    # ========== MOSTRAR RESULTADOS ==========
    # Verifica que haya datos de autores
    if not sales_author:
        print("No author data available.")
        return

    # sorted() ordena alfabéticamente por nombre de autor (clave del diccionario)
    # .items() devuelve pares (autor, total)
    for author, total in sorted(sales_author.items()):
        # Formatea el total con 2 decimales
        print(f"{author}: ${total:.2f}")

    print(data.small)


""" Muestra el rendimiento del inventario basado en ventas """


def inventory_performance():
    # Imprime encabezado decorado
    print(f"\n{data.decorator}")
    print("INVENTORY PERFORMANCE")
    print(data.decorator)

    # Verifica que haya inventario disponible
    if not data.inventory:
        print("No inventory data available.")
        return

    # ========== CALCULAR TOTAL VENDIDO POR PRODUCTO ==========
    # Diccionario para acumular unidades vendidas por código de producto
    sold_by_book = {}

    # Recorre todas las ventas
    for sale in data.sales:
        # Extrae el código del producto
        code = sale['code_product']
        # Extrae la cantidad vendida
        quantity = sale['quantity']

        # Acumula las cantidades vendidas por código
        if code in sold_by_book:
            sold_by_book[code] += quantity
        else:
            sold_by_book[code] = quantity

    # ========== CALCULAR MÉTRICAS GLOBALES ==========
    # Variables para acumular valores totales
    total_inventory_value = 0  # Valor total del inventario actual
    total_revenue_generated = 0  # Ingresos totales generados por ventas

    # ========== ANALIZAR CADA PRODUCTO ==========
    # Itera sobre cada libro en el inventario
    for code, book in data.inventory.items():
        # Obtiene unidades vendidas (0 si no hay ventas de este producto)
        # .get(code, 0) retorna 0 si el código no existe en el diccionario
        sold = sold_by_book.get(code, 0)

        # Calcula ingresos: unidades vendidas × precio unitario
        income = sold * book['price']

        # Calcula valor del inventario: stock actual × precio unitario
        inventory_value = book['stock'] * book['price']

        # Acumula valores globales
        total_inventory_value += inventory_value
        total_revenue_generated += income

        # ========== MOSTRAR INFORMACIÓN DEL PRODUCTO ==========
        print(f"\n{book['title']} ({code}):")
        print(f"  Current stock: {book['stock']} units")
        print(f"  Units sold: {sold}")
        print(f"  Total revenue: ${income:.2f}")
        print(f"  Inventory value: ${inventory_value:.2f}")

        # ========== INDICADOR DE RENDIMIENTO ==========
        # Evalúa el estado del producto y da recomendaciones
        if sold == 0:
            # Producto sin ventas
            print(f" No sales yet")
        elif book['stock'] < 5:
            # Stock crítico - necesita reabastecimiento
            print(f" Low stock - Consider reordering")
        else:
            # Estado normal
            print(f" Good")

    # ========== RESUMEN GENERAL ==========
    print(f"\n{data.decorator}")
    print(f"Total inventory value: ${total_inventory_value:.2f}")
    print(f"Total revenue generated: ${total_revenue_generated:.2f}")
    print(data.decorator)