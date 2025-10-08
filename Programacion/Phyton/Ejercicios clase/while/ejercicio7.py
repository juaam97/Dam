import random

aleatorio = random.randint(1, 10)

Numero = int(input("Dime un numero"))

while Numero != aleatorio :
    Numero = int(input("Dime otro numero"))
print("Lo has adivinado", aleatorio)
