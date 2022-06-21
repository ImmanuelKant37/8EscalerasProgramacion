import json
import funciones_utiles
profesionales={}
profesionales['profesional']=[]

def leer_json():
    try:
        with open("profesionales.json","r") as Archivo:
            profesionales = json.load(Archivo)  
        return(dict(profesionales))
    except:
        print()


def id_maximo():
    profesionales=leer_json()
    profesional= list(profesionales.get('profesional'))
    lista_de_ides=[]
    for atributo in profesional:
        id=atributo['id_medico']
        valor_id=int(id)
        lista_de_ides.append (valor_id)  

    return max(lista_de_ides)

def crear_json(nombre_archivo):
    try:
        with open(str(nombre_archivo)+".json","r") as Archivo:
            print(Archivo)                                      
    except :
         with open(str(nombre_archivo)+".json","w") as Archivo:  
            json.dump(profesionales, Archivo, indent=4)      
         profesional_base=leer_json()
         with open(str(nombre_archivo)+".json","w") as Arch:    
            inicial=list(profesional_base['profesional'])
            profesional_cero={'id_medico':'0', 'Nombre': '','Apellido':'','Especialidad':''}
            inicial.append(profesional_cero)
            profesional_base['profesional']=inicial 
            json.dump(profesional_base, Arch, indent=4)


def agregar_profesionales():
    inombre=funciones_utiles.valida(input("Ingrese un nombre: "))
    iapellido=funciones_utiles.valida(input("Ingrese un apellido: "))
    iespecialidad=funciones_utiles.valida(input("Ingrese su especialidad: "))
   

    profesionales=leer_json()       
    atributos= list(profesionales['profesional'])
    id_max=id_maximo()
    caracteristicas= {'id_medico':str(id_max+1),'Nombre':inombre, 'Apellido':iapellido, 'Especialidad': iespecialidad }
    atributos.append(caracteristicas)
    profesionales['profesional']=atributos
    
    actualizar_json(profesionales)
            
def actualizar_json(diccionario):
    with open("profesionales.json","w") as Archivo:
        json.dump(diccionario,Archivo,indent=4)

def lista_medicos():
    profesionales=list(leer_json()['profesional'])
    for profesional in profesionales:
        print('Nombre:', profesional['Nombre'], "Especialidad:", profesional['Especialidad'] )

def existe_medico(nombre):
    profesionales=list(leer_json()['profesional'])
    for profesional in profesionales:
        if nombre== profesional['Nombre']:
             return nombre

        else:
            print('Ingrese un medico existente')