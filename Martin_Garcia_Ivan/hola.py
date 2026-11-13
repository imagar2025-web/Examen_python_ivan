# Programa original de la tintorería
# Cada encargo: [tipo, cliente, unidades, tarjeta_cliente]
encargos = [
    ["camisa", "Laura Gómez", 3, False],
    ["pantalon", "Sergio Martín", 2, True],
    ["edredon", "Rosa Díaz", 1, False],
    ["camisa", "Javier Soto", 8, True],
    ["edredon", "Pilar Vega", 2, True],
]

total = 0
for e in encargos:
    if e[0] == "camisa":
        precio = e[2] * 2.5
        if precio > 15:
            precio = 15
        if e[3]:
            precio = precio * 0.8
        print("CAMISA | " + e[1] + " | " + str(e[2]) + " uds. | " + str(round(precio, 2)) + " €")
    elif e[0] == "pantalon":
        precio = e[2] * 4.0
        if e[3]:
            precio = precio * 0.8
        print("PANTALON | " + e[1] + " | " + str(e[2]) + " uds. | " + str(round(precio, 2)) + " €")
    elif e[0] == "edredon":
        precio = e[2] * 12.0 + 3
        if e[3]:
            precio = precio * 0.8
        print("EDREDON | " + e[1] + " | " + str(e[2]) + " uds. | " + str(round(precio, 2)) + " €")
    total = total + precio

print("TOTAL TINTORERÍA: " + str(round(total, 2)) + " €")

# Contar encargos de más de 10 €: hay que repetir todos los cálculos
caros = 0
for e in encargos:
    if e[0] == "camisa":
        precio = e[2] * 2.5
        if precio > 15:
            precio = 15
    elif e[0] == "pantalon":
        precio = e[2] * 4.0
    elif e[0] == "edredon":
        precio = e[2] * 12.0 + 3
    if e[3]:
        precio = precio * 0.8
    if precio > 10:
        caros = caros + 1

print("Encargos de más de 10 €: " + str(caros))
