#Construye un programa que dado un número me pinte 
# un cuadrado con tantos * por fila como ese número.  Por ejemplo, para número = 4

numero = 4

i = 1

while i <= numero:
    if i == 1 or i == numero:
        print("*" * numero)
    else:
        print("*" + " " * (numero - 2) + "*" )
    i = i + 1
