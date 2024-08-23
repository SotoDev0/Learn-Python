"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""


def binario(n):
    if n == 0:
        return 0
    
    lista = []

    while n != 0:
        lista.append(n%2)
        n //= 2

    return lista[::-1]


print(binario(1204))
        
