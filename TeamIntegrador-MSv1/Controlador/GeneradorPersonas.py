import json

Personas = {}

Personas['pacientes'] = []

def crea_archivo_json(Nombre):
    with open(Nombre+'.json', 'w') as Archivo:
        json.dump(Personas, Archivo, indent=4)

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
    pacientes.append({'Documento': Documento,'Nombre':Nombre,'Apellido':Apellido,'FechaDeNacimiento':FechaDeNacimiento,'Nacionailidad':Nacionalidad})
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


#crea_archivo_json('Personas')
#eliminar_persona("Personas",1)
#agregar_persona("Mari", "Sanchez","20","21","Personas")
#agregar_persona("Maria", "Sanchez","20","21","Personas")
#modificar_persona("Franci", "Nombre", "Francisco","Personas")