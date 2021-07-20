# Condicionales [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos varialbles de texto y condicionales compuestos
texto_1 = 'a'
texto_2 = 'b'

# Condicionales compuestos
# Si texto_1 es mayor a texto_2 e igual a "hola" o
# texto_1 tiene menos de 4 letras, entonces imprimir "Correcto!"

if (((texto_1 > texto_2) and texto_1 == 'hola') or
    (len(texto_1) < 4)):
    print('Correcto!')

print("terminamos!")
