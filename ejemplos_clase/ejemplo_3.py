# Condicionales [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos varialbles de texto
texto_1 = 'a'
texto_2 = 'b'

# Verificar que texto es mayor alfabéticamente
if texto_1 > texto_2:
    print(f'{texto_1} es mayor que {texto_2}')
else:
    print(f'{texto_2} es mayor que {texto_1}')

texto_1 = 'ab'
texto_2 = 'aab'

if texto_1 > texto_2:
    print(f'{texto_1} es mayor que {texto_2}')
else:
    print(f'{texto_2} es mayor que {texto_1}')

if texto_1 == 'ab':
    print(f'texto_1({texto_1}) es igual a ab')


# Verificar que texto es mayor en caracteres (longitud)
if len(texto_1) > len(texto_2):
    print(f'{texto_1} es mayor que {texto_2}')
else:
    print(f'{texto_2} es mayor que {texto_1}')

print("terminamos!")