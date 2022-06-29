from datetime import date as fecha
from datetime import datetime, timedelta
import datetime as tiempo
import controlPacientes
def es_cero(numero):

    if numero.isnumeric():
        numero=int(numero)
        if numero==0:
            return True
def es_uno(numero):
  
    if numero.isnumeric():
        numero=int(numero)
        if numero==1:
            return True
def es_dos(numero):
   
    if numero.isnumeric():
        numero=int(numero)
        if numero==2:
            return True
def es_tres(numero):
   
    if numero.isnumeric():
        numero=int(numero)
        if numero==3:
            return True
def es_cuatro(numero):
   
    if numero.isnumeric():
        numero=int(numero)
        if numero==4:
            return True

def es_cinco(numero):
    if numero.isnumeric():
        numero=int(numero)
        if numero==5:
            return True

def es_seis(numero):
    if numero.isnumeric():
        numero=int(numero)
        if numero==6:
            return True
def es_siete(numero):
    if numero.isnumeric():
        numero=int(numero)
        if numero==7:
            return True
def devuelve_edad(fecha_ingresada):
    hoy_str=str(fecha.today())
    hoy=int(hoy_str[0:4])
    try:
        if len(fecha_ingresada)==10: 
          año=int(fecha_ingresada[6:10])
          edad=hoy-año
          return str(edad)
        elif(len(fecha_ingresada)==8):
         año=fecha_ingresada[6:8]
         edad=hoy-año
         return str(edad)
        else:
         print("ingrese una fecha valida")
    except:
        print("Formato de fecha incorrecto")


def calcula_rango_fechas():
    desde=input("Ingrese la fecha desde: ")
    hasta=input("Ingrese la fecha hasta: ")
    lista_fechas_json=controlPacientes.obtener_fechas_json("historia clinica")[0]
    lista_json=controlPacientes.obtener_fechas_json("historia clinica")[1]
    lista_nombre_paciente=controlPacientes.obtener_nombre_paciente("atributos")
    rango_de_fechas=lista_fechas_rango(desde,hasta)
    fecha_resultado=[]
    for fecha in lista_fechas_json:
        for fecha_rango in rango_de_fechas:
            if fecha==fecha_rango:
                indice=lista_fechas_json.index(fecha)
                fecha_resultado.append( "Nombre: " + lista_nombre_paciente[indice] +" "+  "Medico que lo atiende: "+ lista_json[indice] +" " + "Fecha: " + fecha )
    return (list(fecha_resultado))


def valida(entrada="Nombre"):
    return str(entrada).title()

def lista_fechas_rango(fecha_desde, fecha_hasta):

    año_desde=int(fecha_desde[6:10])
    mes_desde=int(fecha_desde[3:5])
    dia_desde=int(fecha_desde[0:2])

      
    año_hasta=int(fecha_hasta[6:10])
    mes_hasta=int(fecha_hasta[3:5])
    dia_hasta=int(fecha_hasta[0:2])

    inicio = datetime(año_desde,mes_desde,dia_desde)
    fin    = datetime(año_hasta,mes_hasta,dia_hasta)



    lista_fechas = [(inicio + timedelta(days=dia)).strftime("%d/%m/%Y") 
                    for dia in range((fin - inicio).days + 1)] 
    return(lista_fechas)




