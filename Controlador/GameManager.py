import GeneradorPersonas 
import funciones_utiles as respuesta


#GeneradorPersonas.crea_archivo_json('Personas')
#GeneradorPersonas.eliminar_persona("Personas",1)
#GeneradorPersonas.agregar_persona("Mari", "Sanchez","20","21","Personas")
#GeneradorPersonas.agregar_persona("Maria", "Sanchez","20","21","Personas")
#modificar_persona("Franci", "Nombre", "Francisco","Personas")


while True:
    print("Toca 0 para salir")

    print("Toca 1 para agregar un profesional")
    
    print("Toca 2 para modificar un profesional")

    print("Toca 3 para eliminar un profesional")

    print("Toca 4 para crear un archivo")
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
        Apellido=input("Escribe un apellido")
        Especialidad=input("Escribe una especialidad")
        GeneradorPersonas.agregar_persona(Nombre, Apellido,Especialidad,"Profesional")
    if respuesta.es_dos(int(pregunta)):
        Atributo=input("¿Que atributo modificar?")
        Idenficador=input("¿Que "+Atributo+" quieres modificar?")
        nuevo_valor=input("Ingrese el nuevo valor")
        GeneradorPersonas.modificar_persona(Idenficador,Atributo, nuevo_valor,"Profesional")
    if respuesta.es_tres(int(pregunta)):
        GeneradorPersonas.eliminar_persona("Profesional",0)
        print("Primer profesional eliminado")
    if respuesta.es_cuatro(int(pregunta)):
        GeneradorPersonas.crea_archivo_json('Profesional')
        print("Archivo creado")