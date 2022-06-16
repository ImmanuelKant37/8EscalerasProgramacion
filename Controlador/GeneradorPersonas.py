import json

Profesional = {}

Profesional['Medico'] = []


def crea_archivo_json(Nombre):
    with open(Nombre+'.json', 'w') as Archivo:
        json.dump(Profesional, Archivo, indent=4)

def leer_archivo_json(Nombre):
    with open(Nombre+'.json') as Archivo:
        Profesional = json.load(Archivo)
    return dict(Profesional)

def modificar_persona(Nombre, Atributo,NuevoNombre,Archivo):
    Profesional=leer_archivo_json('Profesional')
    Medico = Profesional.get('Medico')
    for Caracteristica in Medico :
        if Caracteristica[Atributo]==Nombre:
            with open(Archivo+'.json', 'w') as Archivo:
                 
                Caracteristica[Atributo]=NuevoNombre
        
                json.dump(Profesional, Archivo, indent=4)
            #print(Caracteristica[Atributo])


def agregar_persona(Nombre,Apellido,Edad,Archivo):
    Profesional=leer_archivo_json('Profesional')
    Medico = list(Profesional['Medico'])
    Medico.append({'Nombre':Nombre,'Apellido':Apellido,'Especialidad':Edad})
    Profesional['Medico']=Medico
    with open(Archivo+'.json', 'w') as Archivo:
        json.dump(Profesional, Archivo, indent=4)

   
def eliminar_persona(Archivo,index):
    Profesional=leer_archivo_json('Profesional')
    Medico = list(Profesional['Medico'])
    Medico.pop(index)
    Profesional['Medico']=Medico
    with open(Archivo+'.json', 'w') as Archivo:
        json.dump(Profesional, Archivo, indent=4)


#crea_archivo_json('Profesional')
#eliminar_persona("Profesional",1)
#agregar_persona("Mari", "Sanchez","20","21","Profesional")
#agregar_persona("Maria", "Sanchez","20","21","Profesional")
#modificar_persona("Franci", "Nombre", "Francisco","Profesional")