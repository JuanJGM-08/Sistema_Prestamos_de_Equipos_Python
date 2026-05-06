class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        # Validación: Si el precio es menor a 0, lanza un error
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio
print(Producto("Laptop", 1200))  # Esto funcionará
try:
    producto_invalido = Producto("Teléfono", -500)  # Esto lanzará un ValueError
except ValueError as e:
    print(f"Error: {e}")  # Imprime: Error: El precio no puede ser negativo