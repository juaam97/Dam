n = int(input("Dime un numero"))
suma = 0
if n > 0 :
    for numveces in range(1,n) :
        suma = suma+numveces
    print (suma)
else :
    print ("Error")
