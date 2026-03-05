class Contrato:
    def __init__(self, tipo, inicio, fin):
        self.__tipo = tipo
        self.__inicio = inicio
        self.__fin = fin

    def obtenerTipo(self):
        return self.__tipo

    def obtenerInicio(self):
        return self.__inicio

    def obtenerFin(self):
        return self.__fin

    def modificarTipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo


class Empleado:
    def __init__(self, identificacion, nombre, salario_base):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__salario_base = salario_base
        self.__contrato = None   # Asociación


    def obtenerIdentificacion(self):
        return self.__identificacion

    def obtenerNombre(self):
        return self.__nombre

    def obtenerSalarioBase(self):
        return self.__salario_base

    def obtenerContrato(self):
        return self.__contrato


    def modificarNombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def asignarContrato(self, contrato):
        self.__contrato = contrato


    #Polimorfismo
    
    def calcularSalario(self):
        return self.__salario_base


    def mostrarInformacion(self):

        print(f"Empleado        : {self.__nombre}")
        print(f"ID              : {self.__identificacion}")
        print(f"Salario Total   : ${self.calcularSalario():,.2f}")

        if self.__contrato is not None:
            print("Contrato:")
            print(f"   Tipo         : {self.__contrato.obtenerTipo()}")
            print(f"   Inicio       : {self.__contrato.obtenerInicio()}")
            print(f"   Fin          : {self.__contrato.obtenerFin()}")

        print("-" * 60)


#Herencia

class Administrativo(Empleado):

    def __init__(self, area, identificacion, nombre, salario_base):
        super().__init__(identificacion, nombre, salario_base)
        self.area = area

    def calcularSalario(self):
        bono = self.obtenerSalarioBase() * 0.20
        return self.obtenerSalarioBase() + bono


class Operativo(Empleado):

    def __init__(self, turno, identificacion, nombre, salario_base):
        super().__init__(identificacion, nombre, salario_base)
        self.turno = turno

    def calcularSalario(self):
        bono = self.obtenerSalarioBase() * 0.10
        return self.obtenerSalarioBase() + bono


#Composición

class Departamento:

    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def registrarEmpleado(self, empleado):
        self.empleados.append(empleado)


#Agregación

class Empresa:

    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = []

    def registrarDepartamento(self, departamento):
        self.departamentos.append(departamento)