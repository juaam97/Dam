#Para evaluar si una persona es elegible para votar en las elecciones locales: 
# Para ello debe ser mayor de 18 y ciudadano del país 

Edad = int(input("Cual es tu edad?: "))
Ciudadano = input("Vives en españa?: ").upper()

if Edad > 18 and Ciudadano == "SI":
    print("Usted puede votar")
else:
    print("No puedes votar")
print("fin")
