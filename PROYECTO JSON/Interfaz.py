import controlPacientes as juego
import controlMedicos as medico
import funciones_utiles as respuesta

juego.crear_json("Personas")
medico.crear_json("profesionales")
while True:
    print("0:","SALIR")
    print("1:","Listar medicos")
    print("2:","Agregar persona")
    print("3:","Agregar medico")
    print("4:","Buscar paciente")
    print("5:","Buscar por atributo")
    print("6:","Modificar por atributo")
    print("7:","Eliminar por dni")

    valor=input("Ingrese un numero")
    if respuesta.es_cero(valor): 
        break
    if respuesta.es_uno(valor):
        medico.lista_medicos()
    if respuesta.es_dos(valor):
        juego.agregar_persona()
    if respuesta.es_tres(valor):
        medico.agregar_profesionales()
    if respuesta.es_cuatro(valor):
        juego.buscar_paciente()
    if respuesta.es_cinco(valor):
        juego.buscar_por_atributo()
    if respuesta.es_seis(valor):
        juego.modificar_por_atributo()
    if respuesta.es_siete(valor):
        juego.eliminar_por_atributo()

