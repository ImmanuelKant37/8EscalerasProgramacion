import GeneradorPersonas 
import funciones_utiles as respuesta


#GeneradorPersonas.crea_archivo_json('Personas')
#GeneradorPersonas.eliminar_persona("Personas",1)



while True:
    print("Toca 0 para salir: ")
    print("Toca 1 para agregar un paciente: ")

    print("Toca 2 para modificar un paciente: ")
    print("Toca 3 para eliminar un paciente: ")
    print("Toca 4 para crear un archivo: ")
    pregunta = input("Que queres hacer? ")
    if(pregunta.isnumeric):
        pregunta=int(pregunta)
    else:
        print("Inserte un valor valido")
        break
    if respuesta.es_cero(int(pregunta)):
        print("Saliste")
        break
    if respuesta.es_uno(int(pregunta)):
        Documento=input("Escribe un Documento: ")
        Nombre=input("Escribe un nombre: ")
        Apellido=input("Escribe un apellido: ")
        FechaDeNacimiento=input("Escribe un Fecha de Nacimiento: ")
        Nacionalidad=input("Escribe un Nacionalidad: ")

        GeneradorPersonas.agregar_persona(Documento,Nombre, Apellido,FechaDeNacimiento,Nacionalidad,"Personas")

    if respuesta.es_dos(int(pregunta)):
        Atributo=input("¿Que atributo modificar?")
        Idenficador=input("¿Que "+Atributo+" quieres modificar?")
        nuevo_valor=input("Ingrese el nuevo valor")
        GeneradorPersonas.modificar_persona(Idenficador,Atributo, nuevo_valor,"Personas")
  
    if respuesta.es_tres(int(pregunta)):
        pacienteBorrado=input("Ingrese la ubicación del usuario a borrar teniendo en cuenta que comienza en 0(cero)")
        GeneradorPersonas.eliminar_persona("Personas",int(pacienteBorrado))
        print("Primer paciente eliminado")

    if respuesta.es_cuatro(int(pregunta)):
        GeneradorPersonas.crea_archivo_json("Personas") 
    
    if respuesta.es_dos(int(pregunta)):
        Atributo=input("¿Que atributo modificar?")
        Idenficador=input("¿Que "+Atributo+" quieres modificar?")
        nuevo_valor=input("Ingrese el nuevo valor")
        GeneradorPersonas.modificar_persona(Idenficador,Atributo, nuevo_valor,"Personas")