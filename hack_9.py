"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    count = 0
    for key, value in s.items():
        if count == 0:
            # Convertir la primera letra de la clave a mayúscula
            new_key = key.capitalize()
            # Convertir la primera letra del valor a mayúscula y eliminar la letra 'k'
            new_value = value.capitalize().replace('k', '')
            result[new_key] = new_value
        count += 1
    return result

print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))  # Output: {"Foo":"Fooziman"}