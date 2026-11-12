def calcular_total(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(subtotal):
    if subtotal >= 200:
        return subtotal * 0.90
    return subtotal

casos = [(50, 3), (50, 4), (100, 3)]

for precio, cantidad in casos:
    subtotal = calcular_total(precio, cantidad)
    print("Precio:", precio, "| Cantidad:", cantidad)
    print("Subtotal: S/", subtotal)
    print("Total: S/", aplicar_descuento(subtotal))
    print()