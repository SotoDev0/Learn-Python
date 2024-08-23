"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

for x in range(1,101):
    #Múltiplos de 3 y de 5
    if x % 5 == 0 and x % 3 == 0:
        print(f"{x} :fizzbuzz")
    #Múltiplos de 3 
    elif x % 3 == 0:
        print(f"{x} :fizz")
    # Múltiplos de 5
    elif x % 5 == 0:
        print(f"{x} :buzz")
    else:
        print(x)