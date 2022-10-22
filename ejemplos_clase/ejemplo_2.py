# Condicionales [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos con if anidados (elif) y compuestos

# Uso de if anidados (elif)
# Verificar en que rango está z
# mayor o igual 50
# mayor o igual 30
# mayor o igual 10
# menor a 10
z = 25

if z >= 50:
    print("z es mayor o igual a 50")
elif z >= 30:
    print("z es mayor o igual a 30")
elif z >= 10:
    print("z es mayor o igual a 10")
elif z < 10:
    print("z es menor 10")
else:
    print("no se encuentro ningún rango válido")

# Condicionales compuestos
numero_1 = 10
numero_2 = 30
numero_3 = -20

# Calcular el producto entre dos números enteros
# si ambos son positivos (mayores a cero)
if numero_1 > 0 and numero_2 > 0:
    producto = numero_1 * numero_2
    print(f'El producto entre {numero_1} y {numero_2} es {producto}')


# Calcular el producto entre dos números enteros
# si al menos uno de los dos es positivo (mayor a cero)
if numero_1 > 0 or numero_2 > 0:
    producto = numero_1 * numero_2
    print(f'El producto entre {numero_1} y {numero_2} es {producto}')

# Calcular la suma de dos números si almenos uno de ellos
# es mayor o igual a cero
if numero_1 >= 0 or numero_3 >= 0:
    suma = numero_1 + numero_3
    print(f'La suma entre {numero_1} y {numero_2} es {producto}')

# Calcular el producto entre dos números enteros que ambos sean positivos
# y ambos menores a 100
if (numero_1 > 0 and numero_2 > 0) and (numero_1 < 100 and numero_2 < 100):
    producto = numero_1 * numero_2
    print(f'El producto entre {numero_1} y {numero_2} es {producto}')

print("terminamos!")
