import pandas as pd
import os

archivo_csv = "inventario.csv"


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_encabezado(titulo):
    print()
    print("=" * 60)
    print(titulo.center(60))
    print("=" * 60)


def cargar_inventario():
    return pd.read_csv(archivo_csv)


def mostrar_inventario(df):
    limpiar_pantalla()
    mostrar_encabezado("INVENTARIO DE PRODUCTOS")

    print(f"{'Código':<10}{'Nombre':<25}{'Precio':<12}{'Cantidad':<10}")
    print("-" * 60)

    for _, fila in df.iterrows():
        print(f"{fila['Código']:<10}{fila['Nombre']:<25}{fila['Precio']:<12}{fila['Cantidad']:<10}")

    print()
    input("PRESIONE ENTER PARA VOLVER AL MENÚ")


def producto_mas_costoso(df):
    limpiar_pantalla()
    mostrar_encabezado("PRODUCTO MÁS COSTOSO")

    producto = df.loc[df["Precio"].idxmax()]

    print(f"Código   : {producto['Código']}")
    print(f"Nombre   : {producto['Nombre']}")
    print(f"Precio   : {producto['Precio']}")
    print(f"Cantidad : {producto['Cantidad']}")

    print()
    input("PRESIONE ENTER PARA VOLVER AL MENÚ")


def producto_mayor_cantidad(df):
    limpiar_pantalla()
    mostrar_encabezado("PRODUCTO CON MAYOR CANTIDAD")

    producto = df.loc[df["Cantidad"].idxmax()]

    print(f"Código   : {producto['Código']}")
    print(f"Nombre   : {producto['Nombre']}")
    print(f"Precio   : {producto['Precio']}")
    print(f"Cantidad : {producto['Cantidad']}")

    print()
    input("PRESIONE ENTER PARA VOLVER AL MENÚ")


def actualizar_inventario(df):
    limpiar_pantalla()

    ancho = 72

    print()
    print("=" * ancho)
    print("ACTUALIZANDO INVENTARIO".center(ancho))
    print("=" * ancho)

    df["valor_total"] = df["Precio"] * df["Cantidad"]

    print(f"{'Código':<10}{'Nombre':<25}{'Precio':<12}{'Cantidad':<10}{'Valor Total':<15}")
    print("-" * ancho)

    for _, fila in df.iterrows():
        print(f"{fila['Código']:<10}{fila['Nombre']:<25}{fila['Precio']:<12}{fila['Cantidad']:<10}{fila['valor_total']:<15}")

    df.to_csv("inventario_actualizado.csv", index=False)

    print()
    print("El archivo inventario_actualizado.csv se ha generado correctamente")

    print()
    input("PRESIONE ENTER PARA VOLVER AL MENÚ")

def menu():

    df = cargar_inventario()

    while True:

        limpiar_pantalla()
        mostrar_encabezado("MENÚ DE INVENTARIO")

        print("1. Mostrar inventario")
        print("2. Mostrar producto más costoso")
        print("3. Mostrar producto con mayor cantidad")
        print("4. Actualizar inventario y guardar CSV")
        print("5. Salir")

        print("-" * 60)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario(df)

        elif opcion == "2":
            producto_mas_costoso(df)

        elif opcion == "3":
            producto_mayor_cantidad(df)

        elif opcion == "4":
            actualizar_inventario(df)

        elif opcion == "5":
            limpiar_pantalla()
            print("PROGRAMA FINALIZADO")
            break

        else:
            print()
            print("OPCIÓN NO VÁLIDA")
            input("PRESIONE ENTER PARA CONTINUAR")

menu()