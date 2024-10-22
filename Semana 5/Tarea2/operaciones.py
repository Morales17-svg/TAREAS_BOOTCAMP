def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            print("\n¿Qué deseas actualizar?")
            print("1: Nombre")
            print("2: Precio")
            print("3: Cantidad")
            print("4: Todos los atributos")
            
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nuevo_nombre = input("Introduce el nuevo nombre: ")
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
