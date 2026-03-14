import json
import pandas as pd
import os

ANCHO = 74

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def titulo(texto):
    print()
    print("=" * ANCHO)
    print(texto.center(ANCHO))
    print("=" * ANCHO)


def crear_json():

    datos = [
    {"Departamento": "Cauca", "Cantidad_Votantes_Hombres": 1200, "Cantidad_Votantes_Mujeres": 2400},
    {"Departamento": "Huila", "Cantidad_Votantes_Hombres": 4900, "Cantidad_Votantes_Mujeres": 3950},
    {"Departamento": "Antioquia", "Cantidad_Votantes_Hombres": 8500, "Cantidad_Votantes_Mujeres": 9100},
    {"Departamento": "Valle del Cauca", "Cantidad_Votantes_Hombres": 7200, "Cantidad_Votantes_Mujeres": 7600},
    {"Departamento": "Cundinamarca", "Cantidad_Votantes_Hombres": 6400, "Cantidad_Votantes_Mujeres": 7000},
    {"Departamento": "Tolima", "Cantidad_Votantes_Hombres": 3800, "Cantidad_Votantes_Mujeres": 4200},
    {"Departamento": "Nariño", "Cantidad_Votantes_Hombres": 3000, "Cantidad_Votantes_Mujeres": 3600},
    {"Departamento": "Meta", "Cantidad_Votantes_Hombres": 2500, "Cantidad_Votantes_Mujeres": 2900},
    {"Departamento": "Boyacá", "Cantidad_Votantes_Hombres": 4100, "Cantidad_Votantes_Mujeres": 4300},
    {"Departamento": "Santander", "Cantidad_Votantes_Hombres": 5200, "Cantidad_Votantes_Mujeres": 5400}
    ]

    with open("elecciones.json", "w", encoding="UTF-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

    print()
    print("El archivo elecciones.json se ha creado correctamente")
    print()
    input("PRESIONE ENTER PARA CONTINUAR")


def analizar_datos():

    df = pd.read_json("elecciones.json")

    df["Total"] = df["Cantidad_Votantes_Hombres"] + df["Cantidad_Votantes_Mujeres"]
    df["% Hombres"] = df["Cantidad_Votantes_Hombres"] / df["Total"]
    df["% Mujeres"] = df["Cantidad_Votantes_Mujeres"] / df["Total"]

    mujeres = df[df["Cantidad_Votantes_Mujeres"] > df["Cantidad_Votantes_Hombres"]]
    hombres = df[df["Cantidad_Votantes_Hombres"] > df["Cantidad_Votantes_Mujeres"]]

    mujeres.to_json(
        "mayoría_mujeres_departamento.json",
        orient="records",
        indent=4,
        force_ascii=False
    )

    return mujeres, hombres


def mostrar(df, encabezado):

    limpiar()
    titulo(encabezado)

    print(f"{'Departamento':<20}{'Hombres':<12}{'Mujeres':<12}{'Total':<10}{'%H':<10}{'%M':<10}")
    print("-" * ANCHO)

    for _, fila in df.iterrows():

        print(
        f"{fila['Departamento']:<20}"
        f"{fila['Cantidad_Votantes_Hombres']:<12}"
        f"{fila['Cantidad_Votantes_Mujeres']:<12}"
        f"{fila['Total']:<10}"
        f"{fila['% Hombres']:<10.2f}"
        f"{fila['% Mujeres']:<10.2f}"
        )

    print()
    input("PRESIONE ENTER PARA VOLVER AL MENÚ")


def menu():

    mujeres = None
    hombres = None

    while True:

        limpiar()
        titulo("ANÁLISIS DE VOTACIONES")

        print("1. Crear archivo elecciones.json")
        print("2. Crear archivo mayoría_mujeres_departamento.json")
        print("3. Mostrar departamentos con mayoría de mujeres")
        print("4. Mostrar departamentos con mayoría de hombres")
        print("5. Salir")

        print("-" * ANCHO)

        op = input("Seleccione una opción: ")

        if op == "1":
            crear_json()

        elif op == "2":
            mujeres, hombres = analizar_datos()
            print()
            print("El archivo mayoría_mujeres_departamento.json se ha creado correctamente")
            print()
            input("PRESIONE ENTER PARA CONTINUAR")

        elif op == "3":
            if mujeres is not None:
                mostrar(mujeres, "DEPARTAMENTOS CON MAYORÍA DE MUJERES")
            else:
                print()
                print("Primero debe crear el archivo mayoría_mujeres_departamento.json")
                print()
                input("PRESIONE ENTER PARA CONTINUAR")

        elif op == "4":
            if hombres is not None:
                mostrar(hombres, "DEPARTAMENTOS CON MAYORÍA DE HOMBRES")
            else:
                print()
                print("Primero debe crear el archivo mayoría_mujeres_departamento.json")
                print()
                input("PPRESIONE ENTER PARA CONTINUAR")

        elif op == "5":
            limpiar()
            print("PROGRAMA FINALIZADO")
            break

        else:
            print()
            print("OPCIÓN NO VÁLIDA")
            input("PRESIONE ENTER PARA CONTINUAR")

menu()