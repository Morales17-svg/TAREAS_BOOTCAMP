class Prenda:
    def __init__(self, nombre, precio, cantidad, talla):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.talla = talla  # Atributo adicional para la talla

    def mostrar_info(self):
        print(f"{self.nombre} - Precio: ${self.precio} - Cantidad disponible: {self.cantidad} - Talla: {self.talla}")

# Definición del inventario predefinido
def cargar_inventario():
    inventario = [
        Prenda("Camisa de Hombre", 25000, 50, "M"),
        Prenda("Pantalon de Hombre", 30000, 30, "L"),
        Prenda("Falda de Mujer", 28000, 15, "S"),
        Prenda("Blusa de Mujer", 22000, 40, "M"),
        Prenda("Vestido de Mujer", 45000, 10, "L")
    ]
    return inventario

class Carrito:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, prenda):
        if prenda.cantidad > 0:
            if prenda.nombre in self.productos:
                self.productos[prenda.nombre]['cantidad'] += 1
            else:
                self.productos[prenda.nombre] = {'prenda': prenda, 'cantidad': 1}
            prenda.cantidad -= 1  # Reduce la cantidad disponible
        else:
            print(f"No hay suficiente stock de {prenda.nombre}.")

    def mostrar_resumen(self):
        total_general = 0
        print("\nResumen de tu compra:")
        for item, info in self.productos.items():
            cantidad = info['cantidad']
            precio_total = info['prenda'].precio * cantidad
            total_general += precio_total
            print(f"{item} - Cantidad: {cantidad} - Total: ${precio_total:.2f} - Talla: {info['prenda'].talla}")
        print(f"\nLa suma total de compra es: ${total_general:.2f}")

    def guardar_carrito(self, archivo):
        with open(archivo, 'w') as f:
            for info in self.productos.values():
                prenda = info['prenda']
                f.write(f"Prenda: {prenda.nombre}, Precio: {prenda.precio}, Cantidad comprada: {info['cantidad']}, Talla de la prenda: {prenda.talla}\n")
