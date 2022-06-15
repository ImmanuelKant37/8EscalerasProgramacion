import json

Registro_pacientes = []

for pacientes in range (1) :
    paciente  = {}
    Documento_de_identidad = input ("Ingrese DNI: ")
    Apellido= input ("Ingrese apellido: ")
    Nombre = input ("Ingrese nombre: ")
    Fecha_de_nacimento = input("Ingrese fecha de nachimiento EJ(mm/mm/mmmm): ")
    Nacionalidad= input ("Ingrese nacionalidad: ")
    paciente ["Documento_de_identidad"] = Documento_de_identidad
    paciente ["Apellido"]=Apellido
    paciente ["Nombre"]= Nombre
    paciente ["Fecha_de_nacimento"]= Fecha_de_nacimento
    paciente ["Nacionalidad"]= Nacionalidad
    Registro_pacientes.append (paciente)
print (Registro_pacientes)

with open ("Registro_pacientes", "w") as Archivo_paciente:
    json.dump(Registro_pacientes, Archivo_paciente, indent=4)
    print ("Paciente registrado")



