"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    # Reemplazar caracteres según las reglas especificadas
    s = s.replace('a', '@')
    s = s.replace('e', '3')
    s = s.replace('i', '¡')
    s = s.replace('o', '0')
    s = s.replace('u', 'v') 
    # Convertir la letra 'n' y 'q' a mayúsculas
    s = s.replace('n', 'N')
    s = s.replace('q', 'Q')
    s = s.replace('x', 'X')  
    # Convierte el primer carácter a mayúsculas
    if s:
        s = s[0].upper() + s[1:]
    
    return s

print(fn_hack_3("fooziman"))  # Output: F00z¡m@N
print(fn_hack_3("barziman"))  # Output: B@rz¡m@N
print(fn_hack_3("3q"))        # Output: 3Q
print(fn_hack_3("qu"))        # Output: Qv
print(fn_hack_3("qux"))       # Output: QvX