import csv

def crear_archivo():

    estudiantes = [
        ["Juan Perez",20,"Masculino","Ingeniería de Sistemas",4.2],
        ["Maria Garcia",22,"Femenino","Medicina",4.8],
        ["Carlos Lopez",19,"Masculino","Derecho",3.5],
        ["Ana Martinez",21,"Femenino","Psicología",4.1],
        ["Luis Rodriguez",23,"Masculino","Administración",3.9],
        ["Laura Sanchez",20,"Femenino","Ingeniería Civil",4.5],
        ["Diego Gomez",22,"Masculino","Arquitectura",3.2],
        ["Elena Diaz",24,"Femenino","Economía",4.7]
    ]

    with open("estudiantes.csv","w",newline="",encoding="UTF-8") as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow(["Nombre","Edad","Sexo","Programa","Promedio"])

        for estudiante in estudiantes:
            escritor.writerow(estudiante)

    print()
    print("Archivo estudiantes.csv creado correctamente")


def leer_archivo():

    with open("estudiantes.csv","r",encoding="UTF-8") as archivo:

        lector = csv.reader(archivo)

        print()
        print("=========================================================================")
        print("                          LISTADO DE ESTUDIANTES")
        print("=========================================================================")

        encabezado = next(lector)

        print(f"{encabezado[0]:<20}{encabezado[1]:<8}{encabezado[2]:<12}{encabezado[3]:<25}{encabezado[4]:<10}")

        print("-------------------------------------------------------------------------")

        for fila in lector:

            print(f"{fila[0]:<20}{fila[1]:<8}{fila[2]:<12}{fila[3]:<25}{fila[4]:<10}")


def calcular_promedio():

    suma = 0
    cantidad = 0

    with open("estudiantes.csv","r",encoding="UTF-8") as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            suma += float(fila["Promedio"])
            cantidad += 1

    promedio = suma / cantidad

    print()
    print("=========================================================================")
    print("                       PROMEDIO GENERAL DEL GRUPO")
    print("=========================================================================")
    print("Promedio:", round(promedio,2))


def estudiantes_destacados():

    with open("estudiantes.csv","r",encoding="UTF-8") as archivo:

        lector = csv.DictReader(archivo)

        print()
        print("=========================================================================")
        print("                  ESTUDIANTES CON PROMEDIO SUPERIOR A 4.0")
        print("=========================================================================")

        print(f"{'Nombre':<20}{'Edad':<8}{'Sexo':<12}{'Programa':<25}{'Promedio':<10}")

        print("-------------------------------------------------------------------------")

        for fila in lector:

            if float(fila["Promedio"]) > 4.0:

                print(f"{fila['Nombre']:<20}{fila['Edad']:<8}{fila['Sexo']:<12}{fila['Programa']:<25}{fila['Promedio']:<10}")


crear_archivo()
leer_archivo()
calcular_promedio()
estudiantes_destacados()