from goldmansachsclases import *
from datetime import datetime as dt


if __name__ == "__main__":

    empresa = Empresa("Goldman Sachs")

    #Departamentos

    departamento1 = Departamento("Banca de Inversión")
    departamento2 = Departamento("Operaciones")

    empresa.registrarDepartamento(departamento1)
    empresa.registrarDepartamento(departamento2)

    #Empleados

    admin1 = Administrativo("Finanzas", 101, "Karen Niheidy Pastás Valencia", 9000)
    oper1 = Operativo("Nocturno", 102, "Michael Bloomberg", 7000)

    #Contratos

    fecha_actual = dt.now().date()

    contrato1 = Contrato("Indefinido", fecha_actual, "Indefinido")
    contrato2 = Contrato("Termino Fijo", fecha_actual, "31-12-2026")

    admin1.asignarContrato(contrato1)
    oper1.asignarContrato(contrato2)

    # ------------------ Composición ------------------

    departamento1.registrarEmpleado(admin1)
    departamento2.registrarEmpleado(oper1)

    # ------------------ Mostrar Información ------------------

    print("=" * 60)
    print("EMPRESA:", empresa.nombre)
    print("=" * 60)

    for depto in empresa.departamentos:
        print(f"\nDepartamento: {depto.nombre}")
        print("-" * 60)

        for emp in depto.empleados:
            emp.mostrarInformacion()