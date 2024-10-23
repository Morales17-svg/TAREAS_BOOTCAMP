from tienda import Carrito, cargar_inventario

def main():
    carrito = Carrito()

    # Cargar el inventario predefinido
    inventario = cargar_inventario()

    while True:
        print("\nInventario de Productos:")
        for index, prenda in enumerate(inventario):
            print(f"{index}. ", end="")
            prenda.mostrar_info()
        
        # Preguntar al usuario qué prenda desea agregar
        seleccion = input("Ingresa el número del producto que deseas agregar al carrito (o 'salir' para finalizar): ")
        if seleccion.lower() == 'salir':
            break

        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 0 <= seleccion < len(inventario):
                carrito.agregar_producto(inventario[seleccion])
                print(f"Agregaste {inventario[seleccion].nombre} al carrito.")
            else:
                print("Selección no válida. Intenta de nuevo.")
        else:
            print("Por favor, ingresa un número válido.")
    
    # Mostrar resumen final
    carrito.mostrar_resumen()

    # Guardar el carrito en el archivo
    carrito.guardar_carrito("carrito_de_compras.txt")

if __name__ == "__main__":
    main()
