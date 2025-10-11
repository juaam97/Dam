# Determine si un cliente es elegible para un descuento en una tienda. Para ser elegible, 
# el cliente debe haber gastado más de $100 o ser miembro del programa de lealtad. 

Dinerogastado = float(input("Cuanto dinero has gastado?: "))
Miembro = input("Eres miebro del programa de lealtad?: ").upper()

if Dinerogastado > 100 or Miembro == "SI":
    print("Tienes descuento")
else:
    print("No tienes descuento")
print("fin")