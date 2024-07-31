"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    # Verificar si la lista está vacía
    if not s:  
        return ["0"]
    # Lista para almacenar el resultado transformado
    result = []
    # Recorrer cada índice de la lista de entrada
    for i in range(len(s)):
        # Si el índice es par, agregar el número secuencial como cadena
        if i % 2 == 0:
            result.append(str(i + 1))
        # Si el índice es impar, agregar un guión
        else:
            result.append("-")
    
    return result

print(fn_hack_6(["a","b","c","d","e"]))   # Output: ["1","-","3","-","5"]
print(fn_hack_6([]))   # Output: ["0"]

