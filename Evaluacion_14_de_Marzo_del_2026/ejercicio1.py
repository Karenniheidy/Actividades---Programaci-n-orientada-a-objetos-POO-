import csv

archivo_csv = "inventario.csv"

productos = [
    ["P01", "Teclado mecánico", 1300000, 8],
    ["P02", "Mouse gamer", 600000, 12],
    ["P03", "Monitor 34 pulgadas", 1500000, 5],
    ["P04", "Audífonos inalámbricos", 1300000, 9],
    ["P05", "Disco SSD 1TB", 850000, 6]
]

with open(archivo_csv, "w", newline="", encoding="UTF-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Código", "Nombre", "Precio", "Cantidad"])
    escritor.writerows(productos)

print("================================")
print("LISTA DE PRODUCTOS EN INVENTARIO")
print("================================")

valor_total_inventario = 0

with open(archivo_csv, "r", encoding="UTF-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        Codigo = fila["Código"]
        Nombre = fila["Nombre"]
        Precio = float(fila["Precio"])
        Cantidad = int(fila["Cantidad"])

        subtotal = Precio * Cantidad
        valor_total_inventario += subtotal

        print("--------------------------------")
        print("Código:", Codigo)
        print("Nombre:", Nombre)
        print("Precio:", Precio)
        print("Cantidad:", Cantidad)
        print("Valor producto:", subtotal)
        print("--------------------------------")

print("======================================")
print("VALOR TOTAL DEL INVENTARIO:", valor_total_inventario)
print("======================================")