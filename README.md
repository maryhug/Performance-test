# 📚 Sistema de Gestión de Librería Nacional

Sistema robusto de inventario y ventas para librerías desarrollado en Python. Gestiona inventario de libros, registra ventas con descuentos por tipo de cliente, y genera reportes analíticos detallados.

---

## 🎯 Características Principales

### Gestión de Inventario
- ✅ Agregar nuevos libros con información completa (título, autor, categoría, precio, stock)
- ✅ Actualizar información de libros existentes
- ✅ Eliminar libros del inventario
- ✅ Visualizar inventario completo con detalles

### Sistema de Ventas
- 💰 Registro de ventas con validación de stock
- 👥 Sistema de descuentos por tipo de cliente:
  - **Regular**: 0% descuento
  - **VIP**: 10% descuento
  - **Mayorista**: 15% descuento
- 🧾 Generación automática de recibos
- 📊 Historial completo de ventas con totales

### Reportes y Análisis
- 🏆 Top 3 libros más vendidos
- 👨‍💼 Ventas agrupadas por autor
- 📈 Análisis de rendimiento de inventario
- 💵 Cálculo de ingresos totales y valor de inventario

### Persistencia de Datos
- 💾 Guardado automático en formato JSON
- 🔄 Carga de datos al iniciar el sistema
- 🛡️ Manejo robusto de errores y datos corruptos

---

## 📋 Requisitos del Sistema

- **Python**: 3.7 o superior
- **Sistema Operativo**: Windows, macOS, Linux
- **Librerías estándar**: `json`, `os`, `datetime` (incluidas en Python)

**No requiere instalación de dependencias externas** ✨

---

## 🚀 Instalación

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/tu-usuario/sistema-libreria.git
cd sistema-libreria
```

### 2. Verificar estructura de carpetas

```
sistema-libreria/
│
├── main.py                          # Archivo principal
├── Details.py                       # Configuración y variables globales
│
├── Functions/
│   ├── Functions_Files.py          # Gestión de archivos JSON
│   ├── Functions_Inventory.py      # CRUD de inventario
│   ├── Functions_Sale.py           # Gestión de ventas
│   └── Functions_Report.py         # Generación de reportes
│
└── Datos/                           # Carpeta de datos (se crea automáticamente)
    ├── inventory.json               # Inventario persistente
    └── sales.json                   # Historial de ventas
```

### 3. Ejecutar el programa

```bash
python main.py
```

---

## 💻 Uso del Sistema

### Menú Principal

Al iniciar el programa, verás el siguiente menú:

```
==================================================
NATIONAL BOOKSTORE DIGITAL AREA - ROBUST SYSTEM
==================================================
1. Show all books
2. Add new book
3. Update book
4. Delete book
5. Record sale
6. Show sales history
7. Top 3 best-selling books
8. Sales by brand
9. Inventory performance
0. Exit
==================================================
```

### Ejemplos de Uso

#### 📖 Agregar un nuevo libro

```
Select an option: 2

--- ADD NEW BOOK ---
Book code (e.g., P006): P006
Book name: Cien Años de Soledad
Author: Gabriel García Márquez
Category: Realismo Mágico
price: $45000
Quantity stock: 20

Book 'Cien Años de Soledad' added and saved successfully!
```

#### 🛒 Registrar una venta

```
Select an option: 5

--- REGISTER NEW SALE ---
Client name: María González

Customer types:
1. Regular (0% discount)
2. VIP (10% discount)
3. Wholesaler (15% discount)

Select customer type (1-3): 2

Available products:
  P001: Don Quijote - $89560.00 (10 available)
  P002: Cien años de soledad - $6000.00 (89 available)

Enter the product code: P002
Quantity to sell: 3

==================================================
RECIBO DE VENTA
==================================================
customer: María González (VIP)
Producto: Cien años de soledad
quantity: 3
unit_price: $6000.00
Subtotal: $18000.00
Discount_percentage (10%): -$1800.00
TOTAL: $16200.00
Date: 2024-11-25 14:30:45
==================================================
Sale successfully registered and saved!
```

#### 📊 Ver reportes

```
Select an option: 7

==================================================
TOP 3 BEST-SELLING PRODUCTS
==================================================
1. Cien años de soledad - 45 units sold
2. El principito - 32 units sold
3. Don Quijote - 28 units sold
==================================================
```

---

## 🗂️ Estructura del Código

### Módulos Principales

#### `main.py`
- Punto de entrada del programa
- Menú interactivo de consola
- Control de flujo principal
- Manejo de errores global

#### `Details.py`
- Variables globales del sistema
- Configuración de descuentos
- Rutas de archivos
- Constantes de presentación

#### `Functions/Functions_Files.py`
Funciones de persistencia:
- `load_data()`: Carga inventario y ventas desde JSON
- `save_inventory()`: Guarda inventario en archivo
- `save_sales()`: Guarda ventas en archivo
- `create_initial_inventory()`: Crea inventario inicial con 5 libros

#### `Functions/Functions_Inventory.py`
Funciones CRUD de inventario:
- `show_all_products()`: Muestra todo el inventario
- `add_product()`: Agrega nuevo libro
- `update_product()`: Actualiza libro existente
- `remove_product()`: Elimina libro del inventario
- `get_valid_float()`, `get_valid_int()`, `get_input_not_empty()`: Validaciones

#### `Functions/Functions_Sale.py`
Funciones de ventas:
- `record_sale()`: Registra nueva venta con validaciones
- `show_sales_history()`: Muestra historial completo

#### `Functions/Functions_Report.py`
Funciones de reportes:
- `best_selling_products()`: Top 3 productos más vendidos
- `sales_by_author()`: Ventas agrupadas por autor
- `inventory_performance()`: Análisis detallado de rendimiento

---

## 📊 Estructuras de Datos

### Inventario (Dictionary)
```python
{
    "P001": {
        "title": "Don Quijote de la Mancha",
        "author": "Miguel de Cervantes",
        "category": "Novela",
        "price": 89560,
        "stock": 10
    }
}
```

### Ventas (List of Dictionaries)
```python
[
    {
        "customer": "María González",
        "customer_type": "vip",
        "code_product": "P002",
        "name_book": "Cien años de soledad",
        "author": "Gabriel García Márquez",
        "quantity": 3,
        "price_unitario": 6000,
        "discount_percentage": 10,
        "total": 16200.0,
        "date": "2024-11-25 14:30:45"
    }
]
```

### Descuentos (Dictionary)
```python
{
    "regular": 0,
    "vip": 10,
    "wholesaler": 15
}
```

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| **Python 3.x** | Lenguaje principal |
| **JSON** | Formato de almacenamiento |
| **datetime** | Registro de timestamps |
| **os** | Gestión de archivos y directorios |

---

## 🔒 Validaciones Implementadas

### Validaciones de Entrada
- ✅ Campos no vacíos (nombres, códigos)
- ✅ Números válidos (enteros y decimales)
- ✅ Valores mínimos (precios > 0, stock ≥ 0)
- ✅ Códigos únicos al agregar productos

### Validaciones de Negocio
- ✅ Verificación de stock antes de vender
- ✅ Prevención de cantidades negativas
- ✅ Validación de códigos de producto existentes
- ✅ Confirmación antes de eliminar

### Manejo de Errores
- ✅ Captura de `ValueError` en conversiones
- ✅ Captura de `KeyboardInterrupt` (Ctrl+C)
- ✅ Manejo de archivos JSON corruptos
- ✅ Recuperación ante errores de I/O

---

## 📁 Archivos de Datos

### `Datos/inventory.json`
Almacena el inventario completo de libros con formato JSON indentado.

### `Datos/sales.json`
Registra todas las ventas realizadas con información completa.

**Nota**: Estos archivos se crean automáticamente si no existen.

---

## 🎨 Características de Diseño

### Principios Aplicados
- **Modularidad**: Funciones separadas por responsabilidad
- **DRY** (Don't Repeat Yourself): Funciones reutilizables de validación
- **Separación de Concerns**: UI separada de lógica de negocio
- **Robustez**: Manejo extensivo de excepciones

### Patrones de Programación
- Variables globales compartidas
- Validación en cascada
- Menu-driven CLI
- Persistencia JSON

---

## 🚨 Solución de Problemas

### El programa no inicia
```bash
# Verifica la versión de Python
python --version

# Debe ser 3.7 o superior
```

### Error al cargar datos
- Verifica que la carpeta `Datos/` exista
- Si los archivos JSON están corruptos, elimínalos (se recrearán automáticamente)

### Error al guardar datos
- Verifica permisos de escritura en la carpeta `Datos/`
- Asegúrate de tener espacio en disco

---

## 🔮 Futuras Mejoras

- [ ] Interfaz gráfica (GUI) con Tkinter o PyQt
- [ ] Base de datos SQL en lugar de JSON
- [ ] Sistema de usuarios con autenticación
- [ ] Exportación de reportes a PDF/Excel
- [ ] Gráficos y visualizaciones
- [ ] Sistema de búsqueda avanzada
- [ ] Notificaciones de stock bajo
- [ ] Historial de cambios de precios

---

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 📧 Contacto

**Autor**: [Tu Nombre]  
**Email**: tu.email@ejemplo.com  
**GitHub**: [@tu-usuario](https://github.com/tu-usuario)

---

## ⭐ Agradecimientos

- Desarrollado como proyecto educativo para aprender Python
- Inspirado en sistemas reales de gestión de inventario
- Gracias a la comunidad de Python por la documentación

---

## 📸 Capturas de Pantalla

### Menú Principal
```
==================================================
NATIONAL BOOKSTORE DIGITAL AREA - ROBUST SYSTEM
==================================================
```

### Inventario
```
======================================================================
CURRENT INVENTORY
======================================================================

Código: P001
  Title: Don Quijote de la Mancha
  Author: Miguel de Cervantes Saavedra
  Category: Novela
  price: $89560.00
  Stock: 10 units
```

### Recibo de Venta
```
==================================================
RECIBO DE VENTA
==================================================
customer: María González (VIP)
Producto: Cien años de soledad
quantity: 3
unit_price: $6000.00
Subtotal: $18000.00
Discount_percentage (10%): -$1800.00
TOTAL: $16200.00
Date: 2024-11-25 14:30:45
==================================================
```

---

**¡Gracias por usar el Sistema de Gestión de Librería Nacional!** 📚✨
