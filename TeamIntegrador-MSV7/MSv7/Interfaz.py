import controlPacientes as paciente
import controlMedicos as medico
import funciones_utiles as respuesta

paciente.crear_json("Personas")
medico.crear_json("profesionales")
while True:
    print("-------menu principal-------")
    print("0:","SALIR")
    print("1:","Listar medicos")
    print("2:","Agregar paciente")
    print("3:","Agregar medico")
    print("4:","Filtrar paciente")
    print("5:","Buscar por atributo de paciente")
    print("6:","Modificar paciente por atributo")
    print("7:","Eliminar paciente por dni")
    print("----------------------------")

    valor=input("Ingrese un numero: ")
    if respuesta.es_cero(valor): 
        print("Saliste")
        break

    if respuesta.es_uno(valor):
        print("Lista de medicos: ")
        medico.lista_medicos()
        input("Presione una tecla continuar")

    if respuesta.es_dos(valor):
        paciente.agregar_persona()
        print("se agregó paciente: ")
        input("Presione una tecla continuar")

    if respuesta.es_tres(valor):
        medico.agregar_profesionales()
        print("se agregó profecional: ")
        input("Presione una tecla continuar")

    if respuesta.es_cuatro(valor):
        print("Filtrar por: ")
        print("-Nombre")
        print("-Apellido")
        print("-Documento")
        print("-Nacionalidad")
        paciente.filtar_personas()

    if respuesta.es_cinco(valor):
        print("Lista de atributos: ")
        print("-Nombre")
        print("-Apellido")
        print("-Documento")
        print("-Nacionalidad")
        print("-Medico")
        print("-Enfermedad")
        print("-fecha(por rango de fechas)")
        paciente.buscar_por_atributo()
        input("Presione una tecla continuar")

    if respuesta.es_seis(valor):
        print("Lista de atributos: ")
        print("-Nombre")
        print("-Apellido")
        print("-Documento")
        print("-Nacionalidad")
        paciente.modificar_por_atributo()
        print("se modificó paciente: ")
        input("Presione una tecla continuar")

    if respuesta.es_siete(valor):
        paciente.eliminar_por_atributo()
        print("se borró paciente: ")
        input("Presione una tecla continuar")

