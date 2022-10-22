# Condicionales [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos de condicionales
x = 5
y = 2

# Verificar si "x" es mayor a "y"
if x > y:
    print(f'x = {x} es mayor a y = {y}')
else:
    print(f'y = {y} es mayor a x = {x}')

# Realizar la misma operación negando la condición
if not(x > y):
    print(f'x = {x} no es mayor a y = {y}')
else:
    print(f'y = {y} no es mayor a x = {x}')


# Verificar si "x" es par
if (x % 2) == 0:
    print('x es par')
else:
    print('x es impar')


# Verificar si "y" es nu número positivo
if y > 0:
    print('y es positivo')
elif y < 0:
    print('y es negativo')
else:
    print('y es 0')

# Operadores de comparación
copia_x = x

if x == copia_x:
    print('x es igual a copia_x')

if y != copia_x:
    print('y es distinto a copia_x')

print("terminamos!")
