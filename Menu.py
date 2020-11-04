import shutil 
import sys
from daniel import copiar
from daniel import mover


separador=("*"*40)
menu=1
try:
    while menu ==1:
        print(separador+"BIENVENIDO AL Menu Principal: "+separador)
        print("-"*15+"Menu de opciones: "+"-"*15)
        print("1=Quiero copiar un documento entre directorios del sistema de archivos\n2=Quiero mover un documento entre directorios del sistema de archivos")
        opcion=int(input("Que opcion eliges : "))

        if opcion==1:
            nombre=input("Dime como quieres que se llame la copia del documento ya existente : ")
            nombre2=("archivos/"+nombre+".txt")
            copiar(nombre2)
            print("1=SI\n2=NO")
            menu=int(input("Deseas regresar al menu principal : "))


except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)
    
finally:
    print("FIN DEL CODIGO ...")
    print("*"*30)
       