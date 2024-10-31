import os

productos = []  # Lista global para almacenar los productos

def cargar_datos():
    """Carga los productos desde el archivo productos.txt si existe."""
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as f:
            for linea in f:
                datos = linea.strip().split(', ')
                if len(datos) == 3:
                    try:
                        # Extraer nombre, precio y cantidad con etiquetas
                        nombre = datos[0].split(": ")[1]
                        precio = float(datos[1].split(": ")[1])
                        cantidad = int(datos[2].split(": ")[1])
                        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                    except (ValueError, IndexError):
                        print(f"Error en el formato de la línea: {linea}")
        print("Datos cargados correctamente desde productos.txt.")
    else:
        print("No se encontraron datos previos.")

def agregar_producto():
    nombre = input("Introduce el nombre del producto: ").strip().lower()
    while True:
        try:
            precio = float(input("Introduce el precio del producto: ").strip())
            break
        except ValueError:
            print("Precio no válido. Por favor, ingresa un valor numérico.")

    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: ").strip())
            break
        except ValueError:
            print("Cantidad no válida. Por favor, ingresa un número entero.")

    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print("Producto agregado correctamente.")

def ver_productos():
    if not productos:
        print("No hay productos en la lista.")
        return
    print("\nLista de Productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ").strip().lower()
    for producto in productos:
        if producto["nombre"] == nombre:
            print("\n¿Qué deseas actualizar?")
            print("1: Nombre")
            print("2: Precio")
            print("3: Cantidad")
            print("4: Todos los atributos")
            
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nuevo_nombre = input("Introduce el nuevo nombre: ").strip().lower()
                producto["nombre"] = nuevo_nombre
                print("Nombre actualizado correctamente.")
            elif opcion == "2":
                while True:
                    try:
                        nuevo_precio = float(input("Introduce el nuevo precio: ").strip())
                        producto["precio"] = nuevo_precio
                        print("Precio actualizado correctamente.")
                        break
                    except ValueError:
                        print("Precio no válido. Por favor, ingresa un valor numérico.")
            elif opcion == "3":
                while True:
                    try:
                        nueva_cantidad = int(input("Introduce la nueva cantidad: ").strip())
                        producto["cantidad"] = nueva_cantidad
                        print("Cantidad actualizada correctamente.")
                        break
                    except ValueError:
                        print("Cantidad no válida. Por favor, ingresa un número entero.")
            elif opcion == "4":
                nuevo_nombre = input("Introduce el nuevo nombre: ").strip().lower()
                while True:
                    try:
                        nuevo_precio = float(input("Introduce el nuevo precio: ").strip())
                        break
                    except ValueError:
                        print("Precio no válido. Por favor, ingresa un valor numérico.")
                
                while True:
                    try:
                        nueva_cantidad = int(input("Introduce la nueva cantidad: ").strip())
                        break
                    except ValueError:
                        print("Cantidad no válida. Por favor, ingresa un número entero.")
                
                producto["nombre"] = nuevo_nombre
                producto["precio"] = nuevo_precio
                producto["cantidad"] = nueva_cantidad
                print("Todos los atributos actualizados correctamente.")
            else:
                print("Opción no válida.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ").strip().lower()
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print("Producto eliminado correctamente.")
            return
    print("Producto no encontrado.")

def guardar_datos():
    with open("productos.txt", "w") as f:
        for producto in productos:
            f.write(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}\n")
    print("Datos guardados correctamente.")
