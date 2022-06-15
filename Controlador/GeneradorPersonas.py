import json

Personas = {}

Personas['Caracteristicas'] = []

Personas['Caracteristicas'].append({
    'Nombre': 'Franci',
    'Apellido': 'Cantero',
    'Edad': 25,
    'Peso':'52kg'})

Personas['Caracteristicas'].append({
    'Nombre': 'Juan',
    'Apellido': 'Perez',
    'Edad': 31,
    'Peso': '50Kg'})
Personas['Caracteristicas'].append({
    'Nombre': 'Ramon',
    'Apellido': 'Valdez',
    'Edad': 36,
    'Peso': '25Kg'})

def crea_archivo_json(Nombre):
    with open(Nombre+'.json', 'w') as Archivo:
        json.dump(Personas, Archivo, indent=4)

def leer_archivo_json(Nombre):
    with open(Nombre+'.json') as Archivo:
        Personas = json.load(Archivo)
    return dict(Personas)

def modificar_persona(Nombre, Atributo,NuevoNombre,Archivo):
    Personas=leer_archivo_json('Personas')
    Caracteristicas = Personas.get('Caracteristicas')
    for Caracteristica in Caracteristicas :
        if Caracteristica[Atributo]==Nombre:
            with open(Archivo+'.json', 'w') as Archivo:
                 
                Caracteristica[Atributo]=NuevoNombre
        
                json.dump(Personas, Archivo, indent=4)
            #print(Caracteristica[Atributo])


def agregar_persona(Nombre,Apellido,Edad,Peso,Archivo):
    Personas=leer_archivo_json('Personas')
    Caracteristicas = list(Personas['Caracteristicas'])
    Caracteristicas.append({'Nombre':Nombre,'Apellido':Apellido,'Edad':Edad,'Peso':Peso})
    Personas['Caracteristicas']=Caracteristicas
    with open(Archivo+'.json', 'w') as Archivo:
        json.dump(Personas, Archivo, indent=4)

   
def eliminar_persona(Archivo,index):
    Personas=leer_archivo_json('Personas')
    Caracteristicas = list(Personas['Caracteristicas'])
    Caracteristicas.pop(index)
    Personas['Caracteristicas']=Caracteristicas
    with open(Archivo+'.json', 'w') as Archivo:
        json.dump(Personas, Archivo, indent=4)


#crea_archivo_json('Personas')
#eliminar_persona("Personas",1)
#agregar_persona("Mari", "Sanchez","20","21","Personas")
#agregar_persona("Maria", "Sanchez","20","21","Personas")
#modificar_persona("Franci", "Nombre", "Francisco","Personas")