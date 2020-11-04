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
        print(separador)

        if opcion==1:
            carpeta=input("Como se llama la carpeta donde esta en archivo : ")
            archivo=input("Como se llama el archivo que quieres copiar : ")
            nombre=input("Dime como quieres que se llame la copia  : ")
            print(separador)
            original=(carpeta +"/"+ archivo + ".txt")
            nombre2=(carpeta+"/"+nombre+".txt")
            copiar(original,nombre2,carpeta)
            print(separador)
            print("1=SI\n2=NO")
            menu=int(input("Deseas regresar al menu principal : "))
            print("")

        elif opcion==2:
            carpeta=input("Como se llama la carpeta donde esta en archivo : ")
            archivo=input("Como se llama la carpeta a donde lo quieres mover : ")
            nombre=input("Dime como se llama el archivo  : ")
            print(separador)
            archivox=(carpeta+"/"+nombre +".txt")
            mover(archivox,archivo)
            print("1=SI\n2=NO")
            menu=int(input("Deseas regresar al menu principal : "))
            print("")



except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)
    
finally:
    print("FIN DEL CODIGO ...")
    print("*"*30)
       