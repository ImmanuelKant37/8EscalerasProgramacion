import json

Historias_clinicas = [] #lo primero que hay que crear antes de crer el json 
for Registro_de_historias_clinicas in range (1): #Parametrizable, hacer funcion para adaptar
    H_clinicas= {}
    Fecha = input ("Ingresar fecha de consulta: ") #Para validar tipo Fecha valida
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

with open ("hitorias_clinicas", "w") as Archivo_clinica: #para creear un archivos json segunel programa de arriba
    json.dump(Historias_clinicas, Archivo_clinica, indent=4)
    print ("Historia clinica actualizada")
