import pandas as pd
import os

#CONFIGURACIÓN GENERAL DEL SISTEMA

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

#URL DEL ARCHIVO JSON

url = "https://raw.githubusercontent.com/CesarMCuellarCha/archivosCSV/refs/heads/main/SENA.matriculados.json"

#CARGA DE INFORMACIÓN DESDE INTERNET

print("=" * 35)
print("CARGANDO INFORMACIÓN DESDE INTERNET")
print("=" * 35)

df = pd.read_json(url)

print()
print("Total de registros cargados:", len(df))

#FUNCIONES DEL SISTEMA

def limpiar_pantalla():

    os.system("cls" if os.name == "nt" else "clear")

#OPCIÓN 1 - CONSULTAR APRENDICES DEL PROGRAMA ADSO

def consultar_aprendices_adso():

    print()
    print("=" * 70)
    print("CONSULTA DE APRENDICES DEL PROGRAMA ANÁLISIS Y DESARROLLO DE SOFTWARE")
    print("=" * 70)

    filtro_adso = df[
        df["PROGRAMA"].str.contains(
            "ANALISIS Y DESARROLLO DE SOFTWARE",
            case=False,
            na=False
        )
    ]

    print()
    print("Cantidad total de aprendices ADSO:", len(filtro_adso))

    tabla_adso = filtro_adso[
        [
            "FICHA",
            "PROGRAMA",
            "NOMBRE",
            "PRIMER_APELLIDO",
            "SEGUNDO_APELLIDO",
            "ESTADO_APRENDIZ"
        ]
    ].head(50)

    print()
    print("=" * 111)
    print("                                     PRIMEROS 50 APRENDICES DEL PROGRAMA ADSO                                     ")
    print("=" * 111)

    print(tabla_adso.to_string(index=False))

#OPCIÓN 2 - CONSULTAR APRENDICES DE LA FICHA 3312932

def consultar_ficha_3312932():

    print()
    print("=" * 113)
    print("                                     CONSULTA DE APRENDICES DE LA FICHA 3312932                                     ")
    print("=" * 113)

    filtro_adso = df[
        df["PROGRAMA"].str.contains(
            "ANALISIS Y DESARROLLO DE SOFTWARE",
            case=False,
            na=False
        )
    ]

    ficha_3312932 = filtro_adso[
        filtro_adso["FICHA"] == 3312932
    ]

    print()
    print("Cantidad de aprendices en la ficha 3312932:", len(ficha_3312932))

    tabla_ficha = ficha_3312932[
        [
            "FICHA",
            "PROGRAMA",
            "NOMBRE",
            "PRIMER_APELLIDO",
            "SEGUNDO_APELLIDO",
            "ESTADO_APRENDIZ"
        ]
    ]

    print()
    print(tabla_ficha.to_string(index=False))

#OPCIÓN 3 - CONSULTAR APRENDICES EN ESTADO EN TRÁNSITO

def consultar_aprendices_transito():

    print()
    print("=" * 70)
    print("              CONSULTA DE APRENDICES EN ESTADO EN TRÁNSITO              ")
    print("=" * 70)

    filtro_transito = df[
        (df["CODIGO_PROGRAMA"] == 228118) &
        (df["ESTADO_APRENDIZ"] == "En transito")
    ]

    cantidad = len(filtro_transito)

    print()
    print("Cantidad de aprendices en estado en tránsito :", cantidad)

    tabla_transito = filtro_transito[
        [
            "FICHA",
            "PROGRAMA",
            "NOMBRE",
            "PRIMER_APELLIDO",
            "SEGUNDO_APELLIDO",
            "ESTADO_APRENDIZ"
        ]
    ]

    print()

    if tabla_transito.empty:

        print("======================================================================")
        print("        NO EXISTEN APRENDICES EN ESTADO EN TRÁNSITO EN ESTE MOMENTO")
        print("======================================================================")

    else:

        print(tabla_transito.to_string(index=False))

#OPCIÓN 4 - EXPORTAR ARCHIVO JSON

def exportar_archivo_json():

    print()
    print("=" * 70)
    print("EXPORTACIÓN DE DATOS A ARCHIVO JSON")
    print("=" * 70)

    filtro_adso = df[
        df["PROGRAMA"].str.contains(
            "ANALISIS Y DESARROLLO DE SOFTWARE",
            case=False,
            na=False
        )
    ]

    filtro_adso.to_json(

        "ADSO-CTPI.json",

        orient="records",

        indent=4,

        force_ascii=False

    )

    print()
    print("Archivo generado correctamente: ADSO-CTPI.json")

# MENU PRINCIPAL DEL SISTEMA

while True:

    print()
    print("=" * 46)
    print("SISTEMA DE CONSULTA DE APRENDICES SENA")
    print("=" * 46)

    print("1. Consultar aprendices del programa ADSO")
    print("2. Consultar aprendices de la ficha 3312932")
    print("3. Consultar aprendices en estado: En tránsito")
    print("4. Exportar archivo ADSO-CTPI.json")
    print("5. Limpiar pantalla")
    print("6. Salir del sistema")

    print("=" * 46)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        consultar_aprendices_adso()

    elif opcion == "2":

        consultar_ficha_3312932()

    elif opcion == "3":

        consultar_aprendices_transito()

    elif opcion == "4":

        exportar_archivo_json()

    elif opcion == "5":

        limpiar_pantalla()

    elif opcion == "6":

        print()
        print("=" * 70)
        print("PROGRAMA FINALIZADO")
        print("=" * 70)

        break

    else:

        print()
        print("Opción no valida. Intente nuevamente.")