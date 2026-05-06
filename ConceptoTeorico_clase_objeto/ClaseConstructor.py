class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

ana = Persona("Ana García", 28)
print(f"Nombre: {ana.nombre}, Edad: {ana.edad}")
