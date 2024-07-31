"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    # Eliminar la primera y última letra si la longitud del string es mayor o igual a 4 caracteres
    if len(s) >= 4:
        return s[1:-1]
    else:
        return s
    
print(fn_hack_4("fooziman"))   # Output: "oozima"
print(fn_hack_4("barziman"))   # Output: "arzima"
print(fn_hack_4("qux"))   # Output: "qux"
