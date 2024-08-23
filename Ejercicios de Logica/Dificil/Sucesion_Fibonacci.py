"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en
 * la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    inicio = 0
    siguiente = 1
    suma = 0

    for x in range(1,51):
        print(inicio)
        suma = inicio + siguiente
        inicio = siguiente
        siguiente = suma
        
fibonacci()