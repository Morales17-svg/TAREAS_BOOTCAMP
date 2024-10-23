
class Prenda: # Creamos la clase prenda
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre        # Creando atributos
        self.precio = precio        # Creando atributos
        self.cantidad = cantidad    # Creando atributos

    def mostrar_info(self):
        print(f"El nombre de la prenda es {self.nombre}, tiene un precio de {self.precio} y hay disponibles {self.cantidad}")


class Ropa_Hombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)      # Llamamos al constructor de la clase padre
        self.talla = talla      # Atributo especifico de la clase Rompa_Hombre

    def mostrar_info(self):
        super().mostrar_info()      # Llama al metodo de la clase padre
        print(f"Talla: {self.talla}")


class Ropa_Mujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")


class Inventario():
    def __init__(self):
        self.prendas = []   # Lista para almacenar las prendas

    def agregar_prendas(self, prenda):
        self.prendas.append(prenda)     # Agrega las prendas a la lista

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()   # Muestra la información de cada prenda


# Crear instancia de Ropa de hombre y ropa de mujer
camisa = Ropa_Hombre("Camisa de Hombre", 25000, 50, "M")
falda = Ropa_Mujer("Falda de Mujer", 30000, 15, "S")

# Crear inventario  y agregar las prendas
inventario = Inventario()
inventario.agregar_prendas(camisa)
inventario.agregar_prendas(falda)

# Mostrar inventario
inventario.mostrar_inventario()