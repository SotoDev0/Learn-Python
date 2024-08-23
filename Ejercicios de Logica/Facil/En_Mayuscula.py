"""
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * No se pueden utilizar operaciones del lenguaje que
 * lo resuelvan directamente.
"""

def mayuscula(string):
    resultado = []
    new_string = string.split(" ")
    for palabra in new_string:
        palabra = palabra[0].upper() + palabra[1:]
        resultado.append(palabra)

    return " ".join(resultado)


print(mayuscula("hola a todos"))