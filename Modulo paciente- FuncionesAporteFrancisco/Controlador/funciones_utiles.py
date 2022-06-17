from datetime import date as fecha

def es_cero(entrada):
    if entrada==0:
        return True

def es_uno(entrada):
    if entrada==1:
        return True

def es_dos(entrada):
    if entrada==2:
        return True
        
def es_tres(entrada):
    if entrada==3:
        return True

def es_cuatro(entrada):
    if entrada==4:
        return True

def devuelve_edad(fecha_ingresada):
    hoy_str=str(fecha.today())
    hoy=int(hoy_str[0:4])
    try:
        if len(fecha_ingresada)==10: 
          edad=hoy-int(fecha_ingresada[6:8])
          return edad
        elif(len(fecha_ingresada)==8):
         edad=hoy=int(hoy_str[2:4])
         return edad
        else:
         print("ingrese una fecha valida")
    except(e):
        print("Formato de fecha incorrecto")
