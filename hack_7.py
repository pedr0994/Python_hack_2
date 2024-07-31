"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    # Verificar si la lista tiene un solo elemento
    if len(s) == 1:
        return s
    # Lista para almacenar el resultado transformado
    result = []
    # Recorrer cada índice de la lista de entrada
    for i in range(len(s)):
        # Si el índice es par, agregar el número secuencial como cadena
        if i % 2 == 0:
            result.append(str(i + 1))
         # Si el índice es impar, agregar el número secuencial como entero
        else:
            result.append(i + 1)
    
    return result

print(fn_hack_7(["a","b","c","d","e"])) # Output: ["1",2,"3",4,"5"])
print(fn_hack_7([0])) # Output: [0])
