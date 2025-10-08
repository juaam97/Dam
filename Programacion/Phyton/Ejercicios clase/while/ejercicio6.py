#Haz un programa que permita calcular la suma de dos números. Pedirá dos números al usuario y mostrará su suma,
#volviendo a repetir hasta que ambos números introducidos sean 0.

Numerouno = int(input("Dame el primer numero"))
Numerodos = int(input("Dame un segundo numero"))


while not (Numerouno == 0 and Numerodos == 0) :
    print (Numerouno + Numerodos)
    Numerouno = int(input("Dame el primer numero"))
    Numerodos = int(input("Dame un segundo numero"))
