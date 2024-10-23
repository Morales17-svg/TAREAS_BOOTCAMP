# Definiendo la clase Loro
class Loro:  # Como crear una clase que define un tipo de objeto
    pass     # La palabra clave 'pass' se usa aquí para indicar que la clase no tiene atributos o métodos definidos aún

# Creando un objeto de la clase Loro
obj = Loro()  # Se crea una instancia (objeto) de la clase Loro


# Definiendo la clase Estudiante
class Estudiante:  # Esta es la definición de una clase llamada Estudiante
    "Esta es la clase de estudiante con datos"  # Esta es una cadena de documentación que describe la clase

    # Definiendo un método dentro de la clase
    def aprender(self):  # Un método llamado 'aprender', que imprimirá un mensaje cuando se llame
        print("Bienvenidos a la clase de programación en Python del mentor Oscar")

# Creando una instancia (objeto) de la clase Estudiante
estud = Estudiante()  # Aquí se crea un objeto de la clase Estudiante y se almacena en la variable 'estud'

# Llamando al método 'aprender' del objeto 'estud'
estud.aprender()  # Este método imprime el mensaje definido en 'aprender'


# Definiendo la clase Persona
class Persona:  # Esta es la definición de una clase llamada Persona
    # Definiendo el método especial __init__ para inicializar el objeto con atributos
    def __init__(self, nombre, apellido, edad, pais, ciudad): 
        # Atributos del objeto Persona
        self.nombre = nombre  # Atributo nombre
        self.apellido = apellido  # Atributo apellido
        self.edad = edad  # Atributo edad
        self.pais = pais  # Atributo país
        self.ciudad = ciudad  # Atributo ciudad

# Creando una instancia (objeto) de la clase Persona
p = Persona("Pablo", "Morales", 20, "Paraguay", "Limpio")  # Se crea un objeto 'p' con valores iniciales para los atributos

# Mostrando los valores de los atributos de la persona
print(p.nombre)  # Imprime el nombre del objeto 'p'
print(p.apellido)  # Imprime el apellido del objeto 'p'
print(p.edad)  # Imprime la edad del objeto 'p'
print(p.pais)  # Imprime el país del objeto 'p'
print(p.ciudad)  # Imprime la ciudad del objeto 'p'


# Definiendo la clase Student (corregida con mayúscula según la convención)
class Student:  # Definición de la clase Student (estudiante)
    # Método __init__ para inicializar los atributos
    def __init__(self, nombre, curso):  # El constructor inicializa los atributos 'nombre' y 'curso'
        self.nombre = nombre  # Atributo nombre
        self.curso = curso  # Atributo curso

    # Método para mostrar los detalles del estudiante
    def show(self):  # Método 'show' que imprimirá los datos del estudiante
        print(f"El nombre es: {self.nombre} está en el curso {self.curso}")  # Muestra el nombre y el curso del estudiante

# Creando una instancia de la clase Student
stud = Student("Pablo", "2º año")  # Se crea un objeto 'stud' de la clase Student con nombre y curso

# Llamando al método 'show' del objeto 'stud'
stud.show()  # Esto imprime los detalles del objeto 'stud' llamando al método 'show'

# Definiendo la clase Person
class Person:
    # Método constructor que inicializa los atributos de la clase
    def __init__(self, nombre, apellido, año, ciudad):
        self.nombre = nombre  # Atributo 'nombre' de la persona
        self.apellido = apellido  # Atributo 'apellido' de la persona
        self.año = año  # Atributo 'año' que indica la edad de la persona
        self.ciudad = ciudad  # Atributo 'ciudad' donde vive la persona

    # Método para mostrar la información de la persona
    def person_info(self):
        # Usamos un f-string para retornar la información de forma legible
        return f"Me llamo {self.nombre}, mi apellido es {self.apellido}, tengo {self.año} años y vivo en la ciudad de {self.ciudad}"

# Creando una instancia (objeto) de la clase Person
p = Person("Pablo", "Morales", 20, "Limpio")  # Se pasan los valores iniciales

# Llamando al método person_info para mostrar la información
print(p.person_info())  # Imprime los detalles del objeto 'p'

