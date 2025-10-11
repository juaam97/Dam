numero = 5

i = 1

while i <= numero:
    if i == 1 or i == numero:
        print("*" + "#" * (numero - 2) + "*" )
    else:
        print("*" * numero)
    i = i + 1
