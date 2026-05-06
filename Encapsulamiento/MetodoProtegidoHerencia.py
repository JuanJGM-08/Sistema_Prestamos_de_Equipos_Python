class Forma:
    def __init__(self):
        self._tipo = "Forma genérica"

    def calcular_área(self):
        """Método público que utiliza un método protegido."""
        return self._obtener_área()

    def _obtener_área(self):
        """Método protegido que las subclases deben sobrescribir."""
        raise NotImplementedError("Las subclases deben implementar este método")

    def _validar_dimensiones(self, valor):
        """Método protegido útil para las subclases."""
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Las dimensiones deben ser números positivos")
        return True

class Círculo(Forma):
    def __init__(self, radio):
        super().__init__()
        self._tipo = "Círculo"
        self._validar_dimensiones(radio)  # Usando el método protegido de la clase base
        self._radio = radio

    def _obtener_área(self):
        """Implementación del método protegido de la clase base."""
        import math
        return math.pi * self._radio ** 2

class Rectángulo(Forma):
    def __init__(self, ancho, alto):
        super().__init__()
        self._tipo = "Rectángulo"
        self._validar_dimensiones(ancho)  # Usando el método protegido de la clase base
        self._validar_dimensiones(alto)
        self._ancho = ancho
        self._alto = alto

    def _obtener_área(self):
        """Implementación del método protegido de la clase base."""
        return self._ancho * self._alto

mi_circulo = Círculo(5)
print(f"Figura: {mi_circulo._tipo}")
print(f"Área del círculo: {mi_circulo.calcular_área():.2f}")


mi_rect = Rectángulo(10, 5)
print(f"\nFigura: {mi_rect._tipo}")
print(f"Área del rectángulo: {mi_rect.calcular_área()}")
# error = Rectángulo(-2, 5)    