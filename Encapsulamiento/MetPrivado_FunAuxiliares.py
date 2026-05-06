class Ejemplo1:
    def método_público(self, datos):
         # Función auxiliar definida dentro del método
        def función_auxiliar(x):
            return x * 2

        resultado = [función_auxiliar(x) for x in datos]
        return resultado

class Ejemplo2:
    def método_público(self, datos):
        resultado = [self.__función_auxiliar(x) for x in datos]
        return resultado

    def __función_auxiliar(self, x):
        return x * 2

lista = [1, 2, 3, 4, 5]

e1 = Ejemplo1()
print(f"Ejemplo 1 (Función interna): {e1.método_público(lista)}")

e2 = Ejemplo2()
print(f"Ejemplo 2 (Método privado):   {e2.método_público(lista)}")