# Creamos dos objetos Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
# se hizo la clase persona con el constructor para que reciba el nombre y la edad para que funcione el archivo.

ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)

# Accedemos a sus atributos
print(ana.nombre)  # Imprime: Ana García
print(juan.edad)   # Imprime: 35