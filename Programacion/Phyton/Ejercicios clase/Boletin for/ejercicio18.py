# Pedir un número al usuario
numero = int(input("Introduce un número: "))

# Calcular el factorial
factorial = 1
for i in range(2, numero + 1):
    factorial = factorial * i

# Mostrar el resultado
print("El factorial de", numero, "es", factorial)
