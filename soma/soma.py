class Soma:

    @staticmethod
    def soma_numeros(numeros):
        resultado = 0
        for numero in numeros:
            resultado = resultado + numero
        return resultado

numeros = [1, 2 ,3, 4]
resultado = Soma.soma_numeros(numeros)
print(resultado)
