"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    longitud = len(s)
    
    if longitud % 2 == 0:
        # Si la longitud es par, generar solo números decrecientes en formato de cadena
        return [str(longitud - i) for i in range(longitud)]
    else:
        # Si la longitud es impar, generar letras con números decrecientes
        return [f"{letter}-{longitud - i}" for i, letter in enumerate(reversed(s))]

print(fn_hack_8(["a","b","c","d","e"]))  # Output: ["e-5","d-4","c-3","b-2","a-1"]
print(fn_hack_8(["a","b","c"]))          # Output: ["c-3","b-2","a-1"]
print(fn_hack_8(["a","b","c","d"]))     # Output: ["4","3","2","1"]
print(fn_hack_8(["a","b"]))             # Output: ["2","1"]
