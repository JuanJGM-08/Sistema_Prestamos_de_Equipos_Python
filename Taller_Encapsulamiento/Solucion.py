class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        # Atributos privados según el taller
        self._titular = str(titular)
        
        # Validación del saldo inicial
        if saldo_inicial < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(saldo_inicial)

    # Propiedad titular: Solo lectura
    @property
    def titular(self):
        return self._titular

    # Propiedad saldo: Lectura y escritura con validación
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(nuevo_saldo)

    def depositar(self, cantidad):
        """Incrementa el saldo si la cantidad es positiva."""
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """Disminuye el saldo si hay suficiente dinero."""
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False

 # Función principal para probar la clase CuentaBancaria
if __name__ == "__main__":
    try:
        # Inicialización con titular y saldo (por defecto 0 si no se pone)
        cuenta = CuentaBancaria("Juan Giraldo", 1000)
        
        print(f"Cuenta de: {cuenta.titular}")
        print(f"Saldo actual: ${cuenta.saldo}")

        # Prueba de depósito
        print(f"\nIntentando depositar $500: {cuenta.depositar(500)}")
        
        # Prueba de retiro exitoso
        print(f"Intentando retirar $200: {cuenta.retirar(200)}")
        
        # Prueba de retiro fallido (sin fondos suficientes)
        print(f"Intentando retirar $2000: {cuenta.retirar(2000)}")
        
        print(f"Saldo final: ${cuenta.saldo}")

        # Intentar asignar un saldo negativo directamente (debería lanzar error)
        print("\nIntentando forzar saldo negativo...")
        cuenta.saldo = -100

    except ValueError as e:
        print(f"Error capturado: {e}")