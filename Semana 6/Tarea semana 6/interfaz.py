# interfaz.py
from tienda import Carrito, cargar_inventario

def main():
    carrito = Carrito()

    # Cargar el inventario desde el archivo
    inventario = cargar_inventario("inventario.txt")

    print("¡Bienvenido a la tienda de ropa!")
    print("A continuación, encontrarás una lista de productos disponibles:\n")

    while True:
        # Mostrar el inventario de productos con número de artículo
        for index, prenda in enumerate(inventario):
            print(f"{index}. {prenda.nombre} - Precio: ${prenda.precio} - Cantidad disponible: {prenda.cantidad}")

        # Preguntar al usuario qué prenda desea agregar
        seleccion = input("\nIngresa el número del producto que deseas agregar al carrito (o escribe 'salir' para finalizar): ")
        
        # Opción para salir
        if seleccion.lower() == 'salir':
            break

        # Comprobar si la entrada es un número válido
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if 0 <= seleccion <= 4 < len(inventario):
                carrito.agregar_producto(inventario[seleccion])
                print(f"¡Has agregado {inventario[seleccion].nombre} al carrito!")
            else:
                print("Selección no válida. Por favor, elige un número de producto que aparezca en la lista.")
        else:
            print("Por favor, ingresa un número válido.")

    # Mostrar resumen final
    carrito.mostrar_resumen()

    # Guardar el carrito en un archivo separado
    carrito.guardar_carrito("carrito.txt")

if __name__ == "__main__":
    main()
