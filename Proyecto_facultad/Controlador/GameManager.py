import GeneradorPersonas 
import funciones_utiles as respuesta


#GeneradorPersonas.crea_archivo_json('Personas')
#GeneradorPersonas.eliminar_persona("Personas",1)
#GeneradorPersonas.agregar_persona("Mari", "Sanchez","20","21","Personas")
GeneradorPersonas.agregar_persona("Maria", "Sanchez","20","21","Personas")
#modificar_persona("Franci", "Nombre", "Francisco","Personas")


while True:
    print("Toca 0 para salir")
    print("Toca 1 para agregar un paciente")

    print("Toca 2 para modificar un paciente")
    pregunta = input("Que queres hacer")
    if(pregunta.isnumeric):
        pregunta=int(pregunta)
    else:
        print("Inserte un valor")
        break
    if respuesta.es_cero(int(pregunta)):
        print("Saliste")
        break
    if respuesta.es_uno(int(pregunta)):
        Nombre=input("Escribe un nombre")
        Apellido=input("Escribe un nombre")
        GeneradorPersonas.agregar_persona(Nombre, Apellido,"20","21","Personas")
    if respuesta.es_dos(int(pregunta)):
        Nombre=input("Escribe un nombre")
        GeneradorPersonas.modificar_persona("Franci", "Nombre", "Francisco","Personas")