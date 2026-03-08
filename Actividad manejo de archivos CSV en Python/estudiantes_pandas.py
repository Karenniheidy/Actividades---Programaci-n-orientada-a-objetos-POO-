import pandas as pd

df = pd.read_csv("Estudiantes.csv")

def mostrar_tabla(datos, titulo):

    print()
    print("=========================================================================")
    print(                                   titulo)
    print("=========================================================================")

    print(f"{'Nombre':<20}{'Edad':<8}{'Sexo':<12}{'Programa':<25}{'Promedio':<10}")

    print("-------------------------------------------------------------------------")

    for _, fila in datos.iterrows():

        print(f"{fila['Nombre']:<20}{fila['Edad']:<8}{fila['Sexo']:<12}{fila['Programa']:<25}{fila['Promedio']:<10}")


def mostrar_primeros_registros():

    datos = df.head(10)

    mostrar_tabla(datos,"PRIMEROS 10 REGISTROS DE ESTUDIANTES")

def promedio_mayor_42():

    datos = df[df["Promedio"] > 4.2]

    mostrar_tabla(datos,"ESTUDIANTES CON PROMEDIO MAYOR A 4.2")

def estudiantes_por_sexo():

    sexo = input("Ingrese el sexo a consultar (Masculino / Femenino): ")

    datos = df[(df["Sexo"] == sexo) & (df["Edad"] > 21)]

    mostrar_tabla(datos,"ESTUDIANTES FILTRADOS POR SEXO Y EDAD")

def promedio_por_sexo():

    sexo = input("Ingrese el sexo a calcular: ")

    datos = df[df["Sexo"] == sexo]

    promedio = datos["Promedio"].mean()

    print()
    print("=========================================================================")
    print("                 PROMEDIO DEL PROMEDIO DE LOS ESTUDIANTES")
    print("=========================================================================")

    print("Sexo:", sexo)
    print("Promedio:", round(promedio,2))

def estudiante_mayor_edad():

    edad_max = df["Edad"].max()

    datos = df[df["Edad"] == edad_max]

    mostrar_tabla(datos,"ESTUDIANTE DE MAYOR EDAD")

def filtro_especial():

    datos = df[(df["Edad"] == 20) | (df["Promedio"] > 4.5)]

    mostrar_tabla(datos,"ESTUDIANTES CON EDAD = 20 O PROMEDIO > 4.5")

def generar_csv():

    datos = df[df["Promedio"] > 4.5]

    datos.to_csv("alto_rendimiento.csv", index=False)

    print()
    print("=========================================================================")
    print("                             ARCHIVO GENERADO")
    print("=========================================================================")
    print("El archivo alto_rendimiento.csv fue creado correctamente")


def menu():

    while True:

        print()
        print("=========================================================================")
        print("               SISTEMA DE ANALISIS ACADEMICO DE ESTUDIANTES")
        print("=========================================================================")

        print("1. Mostrar primeros 10 registros")
        print("2. Mostrar estudiantes con promedio > 4.2")
        print("3. Filtrar estudiantes por sexo y edad")
        print("4. Promedio del promedio por sexo")
        print("5. Mostrar estudiante de mayor edad")
        print("6. Mostrar edad = 20 o promedio > 4.5")
        print("7. Generar archivo alto_rendimiento.csv")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_primeros_registros()

        elif opcion == "2":
            promedio_mayor_42()

        elif opcion == "3":
            estudiantes_por_sexo()

        elif opcion == "4":
            promedio_por_sexo()

        elif opcion == "5":
            estudiante_mayor_edad()

        elif opcion == "6":
            filtro_especial()

        elif opcion == "7":
            generar_csv()

        elif opcion == "8":

            print()
            print("=========================================================================")
            print("                         EL SISTEMA HA FINALIZADO")
            print("=========================================================================")

            break

        else:

            print()
            print("Opción no válida")

menu()