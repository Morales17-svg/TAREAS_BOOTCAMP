from operaciones import agregar_producto, ver_productos, actualizar_producto, eliminar_producto, guardar_datos, cargar_datos

def main():
    cargar_datos()  # Cargar datos desde el archivo al iniciar el programa
    while True:
        print("\n1: Agregar producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion.isdecimal():
            opcion = int(opcion)
            if opcion == 1:
                agregar_producto()
            elif opcion == 2:
                ver_productos()
            elif opcion == 3:
                actualizar_producto()
            elif opcion == 4:
                eliminar_producto()
            elif opcion == 5:
                guardar_datos()
                break
            else:
                print("Por favor, selecciona un número del 1 al 5")
        else:
            print("Por favor, selecciona un número del 1 al 5")

if __name__ == "__main__":
    main()
