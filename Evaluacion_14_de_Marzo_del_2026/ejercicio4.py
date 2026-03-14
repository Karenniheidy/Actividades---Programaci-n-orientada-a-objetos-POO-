import pandas as pd
import os

ANCHO = 80

URL = "https://raw.githubusercontent.com/CesarMCuellarCha/archivosCSV/refs/heads/main/deportistas.json"

def limpiar():

    os.system("cls" if os.name == "nt" else "clear")


def encabezado(titulo):

    print()
    print("=" * ANCHO)
    print(titulo.center(ANCHO))
    print("=" * ANCHO)


def cargar_datos():

    df = pd.read_json(URL)

    return df


def exportar_deportistas_mujeres(df):

    mujeres = df[df["sexo"] == "Femenino"]

    mujeres.to_json(
        "deportistas_mujeres.json",
        orient="records",
        indent=4,
        force_ascii=False
    )

    print()
    print("El archivo deportistas_mujeres.json ha sido creado correctamente")
    print()
    input("PRESIONE ENTER PARA CONTINUAR")


def exportar_ciclismo_ruta(df):

    filtro = df[
        (df["deporte"] == "Ciclismo de ruta") &
        (df["edad"] >= 28) &
        (df["edad"] <= 35)
    ]

    filtro.to_json(
        "deportistas_ciclismo_ruta.json",
        orient="records",
        indent=4,
        force_ascii=False
    )

    print()
    print("El archivo deportistas_ciclismo_ruta.json ha sido creado correctamente")
    print()
    input("PRESIONE ENTER PARA CONTINUAR")


def promedio_edad_baloncesto(df):

    limpiar()

    encabezado("PROMEDIO DE EDAD - MUJERES EN BALONCESTO")

    mujeres_baloncesto = df[
        (df["sexo"] == "Femenino") &
        (df["deporte"] == "Baloncesto")
    ]

    if mujeres_baloncesto.empty:

        print()
        print("NO EXISTEN DEPORTISTAS MUJERES EN BALONCESTO")
        print()

    else:

        promedio = mujeres_baloncesto["edad"].mean()

        print()
        print("PROMEDIO DE EDAD :", round(promedio, 2))

    input("PRESIONE ENTER PARA VOLVER AL MENÚ")


def deportista_masculino_mayor(df):

    limpiar()

    encabezado("DEPORTISTA MASCULINO DE MAYOR EDAD")

    hombres = df[df["sexo"] == "Masculino"]

    mayor = hombres.sort_values(by="edad", ascending=False).iloc[0]

    print()

    print("NOMBRE        :", mayor["nombre"])
    print("DEPORTE       :", mayor["deporte"])
    print("EDAD          :", mayor["edad"])
    print("ESTATURA      :", mayor["estatura"])
    print("CIUDAD        :", mayor["ciudad_residencia"])

    input("PRESIONE ENTER PARA VOLVER AL MENÚ")


def exportar_estatura_mayor(df):

    altos = df[df["estatura"] > 1.85]

    altos.to_json(
        "deportistas_estatura_mayor_1.85.json",
        orient="records",
        indent=4,
        force_ascii=False
    )

    print()
    print("El archivo deportistas_estatura_mayor_1.85.json ha sido creado correctamente")
    print()
    input("PRESIONE ENTER PARA CONTINUAR")


def menu():

    df = cargar_datos()

    while True:

        limpiar()

        encabezado("ANALISIS DE DEPORTISTAS COLOMBIANOS")

        print("1. Crear archivo deportistas mujeres")
        print("2. Crear archivo ciclismo de ruta")
        print("3. Mostrar promedio de edad mujeres baloncesto")
        print("4. Mostrar deportistas masculino de mayor edad")
        print("5. Crear archivo estatura mayor a 1.85")
        print("6. Salir")

        print("-" * ANCHO)

        opcion = input("SELECCIONE UNA OPCION: ")

        if opcion == "1":

            exportar_deportistas_mujeres(df)

        elif opcion == "2":

            exportar_ciclismo_ruta(df)

        elif opcion == "3":

            promedio_edad_baloncesto(df)

        elif opcion == "4":

            deportista_masculino_mayor(df)

        elif opcion == "5":

            exportar_estatura_mayor(df)

        elif opcion == "6":

            limpiar()

            print("PROGRAMA FINALIZADO")

            break

        else:

            print()
            print("OPCION NO VALIDA")

            input("PRESIONE ENTER PARA CONTINUAR")

menu()