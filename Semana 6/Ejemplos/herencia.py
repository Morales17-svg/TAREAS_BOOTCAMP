# Definiendo una clase padre vacía
class ClasePadre:
    pass

# Definiendo una clase hija que hereda de ClasePadre
class ClaseHija(ClasePadre):
    pass

# Definiendo la clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad  # Atributo edad

    # Método para mostrar la información de la persona
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, edad: {self.edad}")

# Definiendo la clase Estudiante que hereda de Persona
class Estudiante(Persona):
    
    def __init__(self, nombre, edad, clave, sexo, carrera, universidad):
        # Llamando al constructor de la clase base (Persona)
        super().__init__(nombre, edad)
        self.clave = clave  # Atributo clave (añadido para mayor realismo, pero no usado aquí)
        self.sexo = sexo  # Atributo sexo (añadido para mayor realismo, pero no usado aquí)
        self.carrera = carrera  # Atributo carrera
        self.universidad = universidad  # Atributo universidad

    # Sobrescribiendo el método mostrar_info para agregar la información adicional del estudiante
    def mostrar_info(self):
        super().mostrar_info()  # Llamando al método mostrar_info de la clase base (Persona)
        # Mostrando la información adicional del estudiante
        print(f"Clave {self.clave}, Sexo {self.sexo}, Carrera: {self.carrera}, Universidad: {self.universidad}")

# Creando un objeto de la clase Estudiante
estudiante = Estudiante("Pablo", 20, "12345", "M", "Ingeniería Informática", "Universidad Americanaa")

# Llamando al método mostrar_info del objeto estudiante
estudiante.mostrar_info()
