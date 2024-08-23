"""
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero  NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero  NO
 *   estén presentes en str1.
"""


def delete_char(str1,str2):
    # Crear conjuntos de caracteres únicos
    out1 = ''.join([x for x in str1 if x not in str2])
    out2 = ''.join([x for x in str2 if x not in str1])

    return out1, out2

print(delete_char("hola", "adios"))

