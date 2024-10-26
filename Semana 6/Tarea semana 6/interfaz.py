from tienda import Carrito, cargar_inventario  # Importación adaptada

def main():
    carrito = Carrito()
    inventario = cargar_inventario()

    while True:
        print("\nInventario de Productos:")
        for index, prenda in enumerate(inventario):
            print(f"{index}. ", end="")
            # Aplicación de polimorfismo en mostrar_info() para cada prenda
            prenda.mostrar_info()
        
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
    
    carrito.mostrar_resumen()
    carrito.guardar_carrito("carrito_de_compras.txt")

if __name__ == "__main__":
    main()
