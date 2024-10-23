# tienda.py
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"{self.nombre} - Precio: ${self.precio} - Cantidad disponible: {self.cantidad}")

def cargar_inventario(archivo):
    inventario = []
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            datos = linea.strip().split(',')
            nombre = datos[0]
            precio = float(datos[1])
            cantidad = int(datos[2])
            prenda = Prenda(nombre, precio, cantidad)
            inventario.append(prenda)
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
            print(f"{item} - Cantidad: {cantidad} - Total: ${precio_total:.2f}")
    
        print(f" La suma total de compra es: ${total_general}")

    def guardar_carrito(self, archivo):
        with open(archivo, 'w') as f:
            for info in self.productos.values():
                prenda = info['prenda']
                f.write(f"{prenda.nombre},{prenda.precio},{info['cantidad']}\n")
