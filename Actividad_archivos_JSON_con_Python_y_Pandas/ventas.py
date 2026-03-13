import pandas as pd
import os
from tabulate import tabulate

ARCHIVO_JSON = "ventas.json"

#FUNCIÓN LIMPIAR PANTALLA

def limpiar_pantalla():

    os.system("cls" if os.name == "nt" else "clear")

#FUNCIÓN CARGAR DATOS

def cargar_datos():

    datos = pd.read_json(ARCHIVO_JSON)

    return datos

#FUNCIÓN TOTAL POR VENDEDOR

def total_por_vendedor(df):

    total = df.groupby("Vendedor")["Ventas"].sum().reset_index()

    print()
    print("============================")
    print("TOTAL DE VENTAS POR VENDEDOR")
    print("============================")
    print()

    print(tabulate(total, headers="keys", tablefmt="grid", showindex=False, stralign="left", numalign="left"))

#FUNCIÓN PROMEDIO MENSUAL

def promedio_mensual(df):

    promedio = df.groupby("Mes")["Ventas"].mean().reset_index()

    print()
    print("==========================")
    print("PROMEDIO MENSUAL DE VENTAS")
    print("==========================")
    print()

    print(tabulate(promedio, headers="keys", tablefmt="grid", showindex=False, stralign="left", numalign="left"))

#FUNCIÓN MEJOR VENDEDOR

def mejor_vendedor(df):

    total = df.groupby("Vendedor")["Ventas"].sum()

    mejor = total.idxmax()

    print()
    print("===============================")
    print("  VENDEDOR CON MAYORES VENTAS")
    print("===============================")
    print()

    print("Mejor vendedor:", mejor)

#FUNCIÓN EXPORTAR RANKING

def exportar_ranking(df):

    ranking = df.groupby("Vendedor")["Ventas"].sum()

    ranking = ranking.sort_values(ascending=False).reset_index()

    ranking.columns = ["Vendedor", "Total_Ventas"]

    ranking.to_json(
        "ranking_ventas.json",
        orient="records",
        indent=4
    )

    print()
    print("ARCHIVO GENERADO: ranking_ventas.json")

#MENÚ PRINCIPAL

def menu():

    df = cargar_datos()

    while True:

        print()
        print("===============================")
        print(" SISTEMA DE ANALISIS DE VENTAS")
        print("===============================")

        print()
        print("1. Total por vendedor")
        print("2. Promedio mensual")
        print("3. Vendedor con mayores ventas")
        print("4. Exportar ranking")
        print("5. Limpiar pantalla")
        print("6. Salir")

        print()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            total_por_vendedor(df)

        elif opcion == "2":

            promedio_mensual(df)

        elif opcion == "3":

            mejor_vendedor(df)

        elif opcion == "4":

            exportar_ranking(df)

        elif opcion == "5":

            limpiar_pantalla()

        elif opcion == "6":

            print()
            print("PROGRAMA FINALIZADO")
            break

        else:

            print()
            print("OPCIÓN NO VÁLIDA")

menu()