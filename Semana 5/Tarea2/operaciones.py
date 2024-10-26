# operaciones.py

productos = []  # Lista global para almacenar los productos

def agregar_producto():
    nombre = input("Introduce el nombre del producto: ").lower()
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad del producto: "))
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
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"] == nombre.lower():
            print("\n¿Qué deseas actualizar?")
            print("1: Nombre")
            print("2: Precio")
            print("3: Cantidad")
            print("4: Todos los atributos")
            
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nuevo_nombre = input("Introduce el nuevo nombre: ").lower()
                producto["nombre"] = nuevo_nombre
                print("Nombre actualizado correctamente.")
            elif opcion == "2":
                try:
                    nuevo_precio = float(input("Introduce el nuevo precio: "))
                    producto["precio"] = nuevo_precio
                    print("Precio actualizado correctamente.")
                except ValueError:
                    print("Precio no válido.")
            elif opcion == "3":
                try:
                    nueva_cantidad = int(input("Introduce la nueva cantidad: "))
                    producto["cantidad"] = nueva_cantidad
                    print("Cantidad actualizada correctamente.")
                except ValueError:
                    print("Cantidad no válida.")
            elif opcion == "4":
                nuevo_nombre = input("Introduce el nuevo nombre: ")
                try:
                    nuevo_precio = float(input("Introduce el nuevo precio: "))
                    nueva_cantidad = int(input("Introduce la nueva cantidad: "))
                    producto["nombre"] = nuevo_nombre
                    producto["precio"] = nuevo_precio
                    producto["cantidad"] = nueva_cantidad
                    print("Todos los atributos actualizados correctamente.")
                except ValueError:
                    print("Precio o cantidad no válidos.")
            else:
                print("Opción no válida.")
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

def guardar_datos():
    with open("productos.txt", "w") as f:
        for producto in productos:
            f.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente.")
