# Clase base Prenda con encapsulamiento
class Prenda:
    def __init__(self, nombre, precio, cantidad, talla):
        # Encapsulamiento de atributos para proteger el acceso directo
        self._nombre = nombre  
        self._precio = precio
        self._cantidad = cantidad
        self._talla = talla

    # Métodos para acceder y modificar los atributos encapsulados
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    @property
    def talla(self):  # Propiedad para acceder a la talla
        return self._talla

    # Método común para mostrar información, que permite polimorfismo en subclases
    def mostrar_info(self):
        print(f"{self._nombre} - Precio: ${self._precio} - Cantidad disponible: {self._cantidad} - Talla: {self._talla}")

# Subclases de prendas utilizando herencia
class Camisa(Prenda):  
    def __init__(self, precio, cantidad, talla):
        super().__init__("Camisa", precio, cantidad, talla)

class Pantalon(Prenda):  
    def __init__(self, precio, cantidad, talla):
        super().__init__("Pantalon", precio, cantidad, talla)

class Falda(Prenda):  
    def __init__(self, precio, cantidad, talla):
        super().__init__("Falda", precio, cantidad, talla)

class Blusa(Prenda):  
    def __init__(self, precio, cantidad, talla):
        super().__init__("Blusa", precio, cantidad, talla)

class Vestido(Prenda):  
    def __init__(self, precio, cantidad, talla):
        super().__init__("Vestido", precio, cantidad, talla)

# Función para cargar el inventario utilizando las subclases, permitiendo el polimorfismo
def cargar_inventario():
    return [
        Camisa(25000, 50, "M"),
        Pantalon(30000, 30, "L"),
        Falda(28000, 15, "S"),
        Blusa(22000, 40, "M"),
        Vestido(45000, 10, "L")
    ]

class Carrito:
    def __init__(self):
        self.productos = {}

    # Método para agregar productos al carrito con encapsulamiento y control de stock
    def agregar_producto(self, prenda):
        if prenda.cantidad > 0:
            if prenda.nombre in self.productos:
                self.productos[prenda.nombre]['cantidad'] += 1
            else:
                self.productos[prenda.nombre] = {'prenda': prenda, 'cantidad': 1}
            prenda.cantidad -= 1
        else:
            print(f"No hay suficiente stock de {prenda.nombre}.")

    # Método para mostrar el resumen de la compra
    def mostrar_resumen(self):
        total_general = 0
        print("\nResumen de tu compra:")
        for item, info in self.productos.items():
            cantidad = info['cantidad']
            precio_total = info['prenda'].precio * cantidad
            total_general += precio_total
            # Acceso controlado a la talla mediante el encapsulamiento
            print(f"{item} - Cantidad: {cantidad} - Total: ${precio_total:.2f} - Talla: {info['prenda'].talla}")
        print(f"\nLa suma total de compra es: ${total_general:.2f}")

    # Método para guardar el carrito en un archivo de texto
    def guardar_carrito(self, archivo):
        with open(archivo, 'w') as f:
            for info in self.productos.values():
                prenda = info['prenda']
                f.write(f"Prenda: {prenda.nombre}, Precio: {prenda.precio}, Cantidad comprada: {info['cantidad']}, Talla de la prenda: {prenda.talla}\n")
