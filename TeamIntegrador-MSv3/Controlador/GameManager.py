import GeneradorPersonas 
import funciones_utiles as respuesta


#GeneradorPersonas.crea_archivo_json('Personas')
#GeneradorPersonas.eliminar_persona("Personas",1)

GeneradorPersonas.crea_archivo_json("Personas") 

while True:
    print("Toca 0 para salir: ")
    print("Toca 1 para agregar un paciente: ")
    print("Toca 2 para modificar un paciente: ")
    print("Toca 3 para eliminar un paciente: ")
    print("Toca 4 para filtrar pacientes: ")
    print("Toca 5 para buscar un paciente: ")
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
        Atributo=input("¿Que atributo modificar?: ")
        Idenficador=input("¿Que "+Atributo+" quieres modificar? ")
        nuevo_valor=input("Ingrese el nuevo valor: ")
        GeneradorPersonas.modificar_persona(Idenficador,Atributo, nuevo_valor,"Personas")
  
    if respuesta.es_tres(int(pregunta)):
        pacienteBorrado=input("Ingrese la ubicación del usuario a borrar teniendo en cuenta que comienza en 0(cero)")
        GeneradorPersonas.eliminar_persona("Personas",int(pacienteBorrado))
        print("Primer paciente eliminado")
    
    if respuesta.es_cuatro(int(pregunta)):
        print("1:Documento")
        print("2:Nombre")
        print("3:Apellido")
        print("4:Fecha de nacimiento")
        print("5:Nacionalidad")

        tipo_busqueda=input("Ingrese un atributo a filtrar: ")
        print("-----------------")
        GeneradorPersonas.filtar_personas(tipo_busqueda)
        print("-------------------")
        input("Presione una tecla continuar")

    if  respuesta.es_cinco(int(pregunta)):
        print("Nombre")
        print("Apellido")
        print("Nacionalidad")

        tipo_filtro=input("Ingrese un atributo: ")
        Idenficador=input("Ingrese "+tipo_filtro+": ")

        print("-----------------")
        GeneradorPersonas.buscar_persona(Idenficador,tipo_filtro)
        print("-------------------")
        input("Presione una tecla continuar")