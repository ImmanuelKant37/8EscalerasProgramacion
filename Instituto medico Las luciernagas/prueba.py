import json

Registro_pacientes = [] #lista vacia 

for pacientes in range (1) :# range 3 significa que 3 veces te va a pedir la pinche informacion que estaba abajo 
    paciente  = {} #diccionario vacio
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

Historias_clinicas = [] #lo primero que hay que crear antes de crer el json 
for Registro_de_historias_clinicas in range (1):
    H_clinicas= {}
    Fecha = input ("Ingresar fecha de consulta: ")
    Condicion_medica = input ("Condicion medica: ")
    Medico_del_insituto= input ("Ingrese nombre del medico que lo trató: ")
    Especialidad_del_medico = input ("Ingresar especialidad del medico: ")
    Observaciones = input( "Ingresar observaciones generales: ")
    H_clinicas ["fecha"] = Fecha
    H_clinicas ["Condicion_medica"] = Condicion_medica
    H_clinicas["Medico_del_instituto"]= Medico_del_insituto
    H_clinicas["Ingresar especialidad del medico"]= Especialidad_del_medico
    H_clinicas["Observaciones"]= Observaciones
    Historias_clinicas.append (H_clinicas)
print (Historias_clinicas)

with open ("Registro_paciente", "Historias_clinicas", "w") as Archivo_paciente_clinica: #para creear un archivos json segunel programa de arriba
    json.dumps(Registro_pacientes,Historias_clinicas, Archivo_paciente_clinica, indent=  8 )
    print ("Paciente y historia clinica actualizada.")