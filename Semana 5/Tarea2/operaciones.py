productos = []

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(", ")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("El archivo no existe. Iniciando con una lista vacía.")

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f'Producto: {producto["nombre"]} Precio: {producto["precio"]} Cantidad: {producto["cantidad"]}\n')
    print("Datos guardados correctamente.")

def agregar_producto():
    nombre = input("Introduce el nombre del producto: ")
    try:
        precio = float(input("Introduce el precio del producto: "))
        cantidad = int(input("Introduce la cantidad disponible: "))
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print("Producto agregado correctamente.")
    except ValueError:
        print("Precio o cantidad no válidos. Intenta de nuevo.")

def ver_productos():
    if productos:
        print("\nLista de productos:")
        for producto in productos:
            print(f'Nombre: {producto["nombre"]}, Precio: {producto["precio"]}, Cantidad: {producto["cantidad"]}')
    else:
        print("No hay productos en la lista.")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            try:
                nuevo_precio = float(input("Introduce el nuevo precio: "))
                nueva_cantidad = int(input("Introduce la nueva cantidad: "))
                producto["precio"] = nuevo_precio
                producto["cantidad"] = nueva_cantidad
                print("Producto actualizado correctamente.")
                return
            except ValueError:
                print("Precio o cantidad no válidos.")
                return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)
            print("Producto eliminado correctamente.")
            return
    print("Producto no encontrado.")
