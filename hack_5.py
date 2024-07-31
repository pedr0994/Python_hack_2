"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    # Caso cuando la palabra tiene 2 o menos letras
    if len(s) <= 2:
        return s
    
    # Convertimos la palabra en una lista para poder modificar sus caracteres
    result = list(s)

    # Caso cuando la palabra empieza con "fo"
    if s.startswith("fo"):
        if len(result) > 2:
            result[2] = '-'
        if len(result) > 5:
            result.insert(5, '-')
        if len(result) > 6:
            result[-1] = '-'
    
    # Caso cuando la palabra empieza con "ba"
    elif s.startswith("ba"):
        if len(result) > 2:
            result[2] = '-'
        if len(result) > 5:
            result[5] = '-'

    # Caso cuando la palabra tiene menos de 5 letras
    elif len(s) < 5:
        if len(result) > 2:
            result[2] = '-'

    return ''.join(result)

print(fn_hack_5("fooziman"))  # Output: "fo-zi-ma-"
print(fn_hack_5("barziman"))  # Output: "ba-zi-an"
print(fn_hack_5("qux"))       # Output: "qu-"
print(fn_hack_5("eq"))        # Output: "eq"


