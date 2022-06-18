import json

Personas = {}

Personas['pacientes'] = []

def crea_archivo_json(Nombre):
    try:
        with open(Nombre+'.json', 'r') as Archivo:
            print("Archivo encontrado")
    except:
        with open(Nombre+'.json', 'w') as Archivo:
            json.dump(Personas, Archivo, indent=4)
            print("Archivo creado")
    
def leer_archivo_json(Nombre):
    with open(Nombre+'.json') as Archivo:
        Personas = json.load(Archivo)
    return dict(Personas)

def modificar_persona(Nombre, Atributo,NuevoNombre,Archivo):
    Personas=leer_archivo_json('Personas')
    pacientes = Personas.get('pacientes')
    for Caracteristica in pacientes :
        if Caracteristica[Atributo]==Nombre:
            with open(Archivo+'.json', 'w') as Archivo:
                 
                Caracteristica[Atributo]=NuevoNombre
        
                json.dump(Personas, Archivo, indent=4)
            #print(Caracteristica[Atributo])


def agregar_persona(Documento,Nombre,Apellido,FechaDeNacimiento,Nacionalidad,Archivo):
    Personas=leer_archivo_json('Personas')
    pacientes = list(Personas['pacientes'])
    pacientes.append({'Documento': Documento,'Nombre':Nombre,'Apellido':Apellido,'Fecha de nacimiento':FechaDeNacimiento,'Nacionalidad':Nacionalidad})
    Personas['pacientes']=pacientes
    with open(Archivo+'.json', 'w') as Archivo:
        json.dump(Personas, Archivo, indent=4)

   
def eliminar_persona(Archivo,index):
    Personas=leer_archivo_json('Personas')
    pacientes = list(Personas['pacientes'])
    pacientes.pop(index)
    Personas['pacientes']=pacientes
    with open(Archivo+'.json', 'w') as Archivo:
        json.dump(Personas, Archivo, indent=4)

def filtar_personas(tipo_filtro):
    Personas=leer_archivo_json('Personas')
    pacientes=list(Personas['pacientes'])
    for atributo in pacientes:
            print(atributo[tipo_filtro])


def buscar_persona(nombre,tipo_filtro):
    Personas=leer_archivo_json('Personas')
    pacientes=list(Personas['pacientes'])
    for atributo in pacientes:
        if atributo[tipo_filtro]==nombre:
            print(atributo)


#crea_archivo_json('Personas')
#eliminar_persona("Personas",1)
#agregar_persona("Mari", "Sanchez","20","21","Personas")
#agregar_persona("Maria", "Sanchez","20","21","Personas")
#modificar_persona("Franci", "Nombre", "Francisco","Personas")