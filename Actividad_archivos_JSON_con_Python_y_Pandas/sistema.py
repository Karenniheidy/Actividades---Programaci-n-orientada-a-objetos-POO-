import pandas as pd
import os
import json
from tabulate import tabulate

#CONFIGURACIÓN GENERAL DEL SISTEMA

ARCHIVO_JSON = "datos.json"

#FUNCIÓN LIMPIAR PANTALLA

def limpiar_pantalla():

    os.system("cls" if os.name == "nt" else "clear")

#FUNCIÓN CREAR ARCHIVO JSON SI NO EXISTE

def verificar_archivo():

    if not os.path.exists(ARCHIVO_JSON):

        datos_iniciales = [

            { "Nombre": "David Isaac", "Edad": 40, "Ciudad": "Manizales" },
            { "Nombre": "María de los Ángeles",  "Edad": 28, "Ciudad": "Medellín" }

        ]

        with open(ARCHIVO_JSON, "w", encoding="UTF-8") as archivo:

            json.dump(datos_iniciales, archivo, indent=4, ensure_ascii=False)

#FUNCIÓN CARGAR DATOS

def cargar_datos():

    verificar_archivo()

    df = pd.read_json(ARCHIVO_JSON)

    return df

#FUNCIÓN GUARDAR DATOS

def guardar_datos(df):

    df.to_json(

        ARCHIVO_JSON,

        orient="records",

        indent=4,

        force_ascii=False

    )

#FUNCIÓN MOSTRAR REGISTROS

def mostrar_registros(df):

    print()

    print("=============================================")
    print("              LISTA DE REGISTROS")
    print("=============================================")

    print()

    print(tabulate(df, headers="keys", tablefmt="grid", showindex=False, stralign="left", numalign="left"))

#FUNCIÓN AGREGAR NUEVO REGISTRO

def agregar_registro(df):

    print()

    print("==========================")
    print("  AGREGAR NUEVO REGISTRO")
    print("==========================")

    nombre  = input("Nombre  : ")
    edad    = int(input("Edad    : "))
    ciudad  = input("Ciudad  : ")

    nuevo_registro = pd.DataFrame([

        {
            "Nombre": nombre,
            "Edad": edad,
            "Ciudad": ciudad
        }

    ])

    df = pd.concat([df, nuevo_registro], ignore_index=True)

    guardar_datos(df)

    print()
    print("REGISTRO AGREGADO CORRECTAMENTE")

    return df

#FUNCIÓN REPORTE ESTADÍSTICO

def reporte_estadistico(df):

    print()
    print("==============================================")
    print("        REPORTE ESTADÍSTICO DEL SISTEMA")
    print("==============================================")

    print("----------------------------------------------")
    print("       INFORMACIÓN GENERAL DE REGISTROS")
    print("----------------------------------------------")

    total_registros = len(df)
    ciudades_unicas = df["Ciudad"].nunique()
    edad_promedio = df["Edad"].mean()
    edad_minima = df["Edad"].min()
    edad_maxima = df["Edad"].max()

    print("Total de registros        :", total_registros)
    print("Ciudades registradas      :", ciudades_unicas)
    print("Edad promedio             :", round(edad_promedio,2))
    print("Edad mínima               :", edad_minima)
    print("Edad máxima               :", edad_maxima)

    print("----------------------------------------------")
    print("      DISTRIBUCIÓN DE PERSONAS POR CIUDAD")
    print("----------------------------------------------")

    ciudades = df["Ciudad"].value_counts().reset_index()
    ciudades.columns = ["Ciudad", "Cantidad"]

    print()
    print(tabulate(ciudades, headers="keys", tablefmt="grid", showindex=False, stralign="left", numalign="left"))

#FUNCIÓN EXPORTAR ARCHIVOS

def exportar_archivos(df):

    df.to_csv(

        "reporte_registros.csv",

        index=False

    )

    df.to_json(

        "reporte_registros.json",

        orient="records",

        indent=4,

        force_ascii=False

    )

    print()

    print("ARCHIVOS EXPORTADOS CORRECTAMENTE")
    print("reporte_registros.csv")
    print("reporte_registros.json")

#MENÚ PRINCIPAL DEL SISTEMA

def menu_principal():

    df = cargar_datos()

    while True:

        print()
        print("======================================")
        print("SISTEMA DE REGISTROS CON JSON Y PANDAS")
        print("======================================")

        print()
        print("1. Mostrar registros")
        print("2. Agregar nuevo registro")
        print("3. Generar reporte estadístico")
        print("4. Exportar resultados a CSV y JSON")
        print("5. Limpiar pantalla")
        print("6. Salir")

        print()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            mostrar_registros(df)

        elif opcion == "2":

            df = agregar_registro(df)

        elif opcion == "3":

            reporte_estadistico(df)

        elif opcion == "4":

            exportar_archivos(df)

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

menu_principal()