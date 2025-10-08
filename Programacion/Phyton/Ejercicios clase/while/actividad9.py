passwordusuario = ("1234")

passwordintroducida =(input("Dime la password"))

while passwordintroducida != passwordusuario :
    print("password incorrecta")
    passwordintroducida =int(input("Dime la password"))
print("password correcta")