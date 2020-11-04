import shutil 

def copiar(original,nombre2,carpeta):
    shutil.copy(original,nombre2)
    print(f"El Documento ya esta copiado en la carpeta :{carpeta}")

def mover():
    shutil.move('archivos/Documento.txt','archivo_mover',copy_function=shutil.copy)
