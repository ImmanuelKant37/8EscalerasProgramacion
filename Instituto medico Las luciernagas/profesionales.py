
import json


Doctores_especialidades= []
for profesional in range (2):
    profesionales = {}
    Apellido= input ("Ingresar apellido del profesional: ")
    Nombre = input ("Ingresar nombre del profesional: ")
    Especialidad = input ("Ingresar especialidad: ")
    profesionales ["Apellido"] = Apellido
    profesionales ["Nombre"]= Nombre
    profesionales ["Especialidad"] = Especialidad
    Doctores_especialidades.append(profesionales)
print (Doctores_especialidades)

with open ("Doctores_especialidades", "w") as Archivo_profesionales:
    json.dump(Doctores_especialidades,Archivo_profesionales, indent=2)
    print ("Profesional cargado")