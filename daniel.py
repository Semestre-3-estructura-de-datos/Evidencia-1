import shutil 

def copiar(original,nombre2,carpeta):
    shutil.copy(original,nombre2)
    print(f"El Documento ya esta copiado en la carpeta :{carpeta}")

def mover(archivox,archivo):
    shutil.move(archivox,archivo,copy_function=shutil.copy)
    print(f"El Documento ya esta copiado en la carpeta :{archivo}")
