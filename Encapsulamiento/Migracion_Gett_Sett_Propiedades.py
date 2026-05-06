class ProductoV1:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Versión intermedia con getters y setters
class ProductoV2:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        self._nombre = valor

    def get_precio(self):
        return self._precio

    def set_precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor

class ProductoV3:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor
print("ProductoV1:")
p1 = ProductoV1("Camiseta", 20)
print(f"Nombre: {p1.nombre}, Precio: ${p1.precio}")

print("ProductoV2:")
p2 = ProductoV2("Pantalón", 30)
print(f"Nombre: {p2.get_nombre()}, Precio: ${p2.get_precio()}")

print("ProductoV3:")
p3 = ProductoV3("Zapatos", 50)
print(f"Nombre: {p3.nombre}, Precio: ${p3.precio}")

