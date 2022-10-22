# Condicionales [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos condicionales y operador incrementar

# Primero debo inicializar la variable
# que utilizaremsos para guardar el puntaje
# y aumentar con cada respuesta correcta
puntaje = 0

# Prigunta Nº1
print("Pregunta Nº1")
# \n es para "salto de línea (como si fuera un enter)"
respuesta = int(input("¿Cuánto es 5x2?\n"))

if respuesta == 10:
    # Si la respuesta es correcta
    # aumentar puntaje
    print("¡Muy bien!")
    puntaje += 1
else:
    # Respuesta incorrecta
    print("¡Respuesta incorrecta!")


# Prigunta Nº2
print("Pregunta Nº2")
respuesta = int(input("¿Cuántas letras tiene la palabra python?\n"))

if respuesta == 5:
    # Si la respuesta es correcta
    # aumentar puntaje
    print("¡Muy bien!")
    puntaje += 1
else:
    # Respuesta incorrecta
    print("¡Respuesta incorrecta!")



# Prigunta Nº3 --> BONUS
print("Pregunta Nº3")
respuesta = str(input("¿Cuál es la capital de Irlanda?\n"))

# Transformar a el dato ingresado a minúsculas
# para evitar problemas como
# Dublin / dublin / DUBLIN
# y todo sea considerado igual
respuesta = respuesta.lower()

if respuesta == "dublin":
    # Si la respuesta es correcta
    # aumentar puntaje
    print("¡Muy bien!")
    puntaje += 3
else:
    # Respuesta incorrecta
    print("¡Respuesta incorrecta!")


print(f"Su puntaje final es: {puntaje}")