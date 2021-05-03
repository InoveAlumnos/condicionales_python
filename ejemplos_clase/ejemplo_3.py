# Condicionales [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos varialbles de texto
texto_1 = 'a'
texto_2 = 'b'

# Verificar que texto es mayor alfabéticamente
if texto_1 > texto_2:
    print('{} es mayor que {}'.format(texto_1, texto_2))
else:
    print('{} es mayor que {}'.format(texto_2, texto_1))

texto_1 = 'ab'
texto_2 = 'aab'

if texto_1 > texto_2:
    print('{} es mayor que {}'.format(texto_1, texto_2))
else:
    print('{} es mayor que {}'.format(texto_2, texto_1))

if texto_1 == 'ab':
    print('texto_1({}) es igual a ab'.format(texto_1))


# Verificar que texto es mayor en caracteres (longitud)
if len(texto_1) > len(texto_2):
    print('{} es mayor que {}'.format(texto_1, texto_2))
else:
    print('{} es mayor que {}'.format(texto_2, texto_1))

print("terminamos!")