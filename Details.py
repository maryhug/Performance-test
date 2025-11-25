# ============================================================================
# MÓDULO DE CONFIGURACIÓN Y VARIABLES GLOBALES DEL SISTEMA
# ============================================================================
# Este archivo (Details.py) centraliza todas las variables globales,
# constantes y configuraciones del sistema de gestión de librería

# ========== ESTRUCTURAS DE DATOS GLOBALES ==========

# Diccionario principal que almacena todo el inventario de libros
# Estructura: {código_producto: {título, autor, categoría, precio, stock}}
# Ejemplo: {"P001": {"title": "Don Quijote", "author": "Cervantes", ...}}
inventory = {}

# Lista que almacena el historial completo de ventas
# Cada elemento es un diccionario con información de una venta
# Estructura: [{customer, customer_type, code_product, name_book, author,
#              quantity, price_unitario, discount_percentage, total, date}, ...]
sales = []

# ========== CONFIGURACIÓN DE DESCUENTOS POR TIPO DE CLIENTE ==========

# Diccionario que mapea tipos de cliente a sus porcentajes de descuento
# Esta estructura permite fácil mantenimiento y extensión de tipos de cliente
# Clave: tipo de cliente (string)
# Valor: porcentaje de descuento (integer)
customer_discounts = {
    "regular": 0,        # Cliente regular: sin descuento (0%)
    "vip": 10,          # Cliente VIP: 10% de descuento
    "wholesaler": 15    # Mayorista: 15% de descuento
}
# Esta estructura facilita:
# - Agregar nuevos tipos de cliente sin modificar lógica
# - Cambiar porcentajes de descuento de forma centralizada
# - Acceso rápido mediante clave: customer_discounts["vip"] → 10

# ========== RUTAS DE ARCHIVOS (CONSTANTES DE CONFIGURACIÓN) ==========

# Ruta del archivo JSON donde se guarda el inventario
# Este archivo persiste los datos del inventario entre sesiones
ARCHIVE_INVENTORY = "Datos/inventory.json"

# Ruta del archivo JSON donde se guarda el historial de ventas
# Almacena todas las transacciones realizadas
SALES_ARCHIVE = "Datos/sales.json"

# Nota: Ambas rutas apuntan al directorio "Datos/" que debe existir
# Las funciones de Functions_Files.py se encargan de crear este directorio

# ========== CONSTANTES DE FORMATO Y PRESENTACIÓN ==========

# Línea decorativa larga (70 caracteres) para encabezados principales
# Se usa en reportes extensos como inventory_performance()
decorator = "=" * 70
# Ejemplo de uso: print(decorator) → "====================================..."

# Línea decorativa corta (50 caracteres) para secciones más pequeñas
# Se usa en recibos de venta y reportes simples
small = "=" * 50
# Ejemplo de uso: print(small) → "=================================="

# Estas constantes aseguran:
# - Consistencia visual en toda la aplicación
# - Fácil modificación del estilo de presentación
# - Código más limpio (evita repetir "=" * 70 en múltiples lugares)