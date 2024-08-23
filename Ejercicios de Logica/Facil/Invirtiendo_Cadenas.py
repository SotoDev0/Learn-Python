"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertir_cadena(text):
    new_text = text[::-1]
    return new_text


print(invertir_cadena("hola mundo"))