numero = 5

i = 1
while i <= numero:
    fila = "*"  # Empieza con el borde izquierdo

    j = 1
    while j <= numero - 2:
        # Si fila y columna son impares → '#', si no → '@'
        if (i + j) % 2 == 0:
            fila += "#"
        else:
            fila += "@"
        j += 1

    fila += "*"  # Borde derecho
    print(fila)
    i += 1