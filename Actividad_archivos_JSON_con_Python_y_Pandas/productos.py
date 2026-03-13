import pandas as pd
import os
from tabulate import tabulate

#CONFIGURACIÓN GENERAL DEL SISTEMA

ARCHIVO_JSON = "productos.json"

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

#FUNCIÓN LIMPIAR PANTALLA

def limpiar_pantalla():

    os.system("cls" if os.name == "nt" else "clear")


#FUNCIÓN CARGAR DATOS DE JSON

def cargar_datos():

    try:

        datos = pd.read_json(ARCHIVO_JSON)

        return datos

    except:

        print()
        print("ERROR AL CARGAR EL ARCHIVO JSON")

        return pd.DataFrame()


#FUNCIÓN MOSTRAR INVENTARIO

def mostrar_productos(df):

    print()
    print("======================================")
    print("        INVENTARIO DE PRODUCTOS")
    print("======================================")

    print()

    print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))


# FUNCIÓN CALCULAR VALOR POR PRODUCTO

def calcular_valor_producto(df):

    df["Valor_Total"] = df["Precio"] * df["Cantidad"]

    print()
    print("======================================================")
    print("               VALOR TOTAL POR PRODUCTO")
    print("======================================================")

    print()

    print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))


#FUNCIÓN CALCULAR VALOR TOTAL INVENTARIO

def calcular_valor_inventario(df):

    df["Valor_Total"] = df["Precio"] * df["Cantidad"]

    total = df["Valor_Total"].sum()

    print()
    print("======================================================")
    print("               VALOR TOTAL DEL INVENTARIO")
    print("======================================================")

    print()

    print("VALOR TOTAL DEL INVENTARIO:", total)


# FUNCIÓN EXPORTAR PRODUCTOS CON BAJO STOCK

def exportar_bajo_stock(df):

    bajo_stock = df[df["Cantidad"] < 5]

    print()
    print("======================================")
    print("       PRODUCTOS CON BAJO STOCK")
    print("======================================")

    print()

    print(tabulate(bajo_stock, headers="keys", tablefmt="grid", showindex=False))

    bajo_stock.to_json(
        "productos_bajo_stock.json",
        orient="records",
        indent=4
    )

    print()
    print("ARCHIVO GENERADO: productos_bajo_stock.json")


#MENÚ PRINCIPAL DEL SISTEMA

def menu():

    df = cargar_datos()

    while True:

        print()
        print("=====================================")
        print(" SISTEMA DE INVENTARIO DE PRODUCTOS")
        print("=====================================")

        print()
        print("1. Mostrar productos")
        print("2. Calcular valor por producto")
        print("3. Calcular valor total del inventario")
        print("4. Exportar productos con bajo stock")
        print("5. Limpiar pantalla")
        print("6. Salir")

        print()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            mostrar_productos(df)

        elif opcion == "2":

            calcular_valor_producto(df)

        elif opcion == "3":

            calcular_valor_inventario(df)

        elif opcion == "4":

            exportar_bajo_stock(df)

        elif opcion == "5":

            limpiar_pantalla()

        elif opcion == "6":

            print()
            print("PROGRAMA FINALIZADO")
            break

        else:

            print()
            print("OPCIÓN NO VÁLIDA")


#EJECUCIÓN DEL SISTEMA

menu()