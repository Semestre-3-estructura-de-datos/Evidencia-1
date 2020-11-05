import shutil 
import sys
import os 
from daniel import copiar
from daniel import mover


separador=("*"*40)
menu=1
try:
    while menu ==1:
        print(separador+"BIENVENIDO AL Menu Principal: "+separador)
        print("-"*15+"Menu de opciones: "+"-"*15)
        print("1=Quiero copiar un documento entre directorios del sistema de archivos.\n2=Quiero mover un documento entre directorios del sistema de archivos.")
        print("3=Aplicación de listas y  Aplicación de tuplas como estructuras de datos nativas.")
        opcion=int(input("Que opcion eliges : "))
        print(separador)

        if opcion==1:
            carpeta=input("Como se llama la carpeta donde esta el archivo : ")
            archivo=input("Como se llama el archivo que quieres copiar con su extension: ")
            nombre=input("Dime como quieres que se llame la copia con su extension  : ")
            print(separador)
            directorio_actual=os.getcwd()
            print(f"El Directorio actual es :{directorio_actual}")
            print(separador)
            original=(carpeta +"/"+ archivo)
            nombre2=(carpeta+"/"+nombre)
            copiar(original,nombre2,carpeta)
            print(separador)
            print("1=SI\n2=NO")
            menu=int(input("Deseas regresar al menu principal : "))
            print("")

        elif opcion==2:
            carpeta=input("Como se llama la carpeta donde esta el archivo : ")
            archivo=input("Como se llama la carpeta a donde lo quieres mover : ")
            nombre=input("Dime como se llama el archivo con su extension  : ")
            print(separador)
            directorio_actual=os.getcwd()
            print(f"El Directorio actual es :{directorio_actual}")
            print(separador)
            archivox=(carpeta+"/"+nombre)
            mover(archivox,archivo)
            print("1=SI\n2=NO")
            menu=int(input("Deseas regresar al menu principal : "))
            print("")
        
        elif opcion==3:
            #Aqui va JARED
            pass






except:
    print("*"*30)
    print(f"Ocurrió un problema {sys.exc_info()[1]}")
    print("Intenta respetar lo que se te pide :) ")
    print("*"*30)
    
finally:
    print("*"*30)
    print(f"{os.path.getsize('archivos')} bytes de la carpeta archivos")
    print("*"*30)
    print(f"{os.path.getsize('archivomover')} bytes de la carpeta archivomover")
    print("*"*30)
    print("FIN DEL CODIGO ...")
    print("*"*30)
       