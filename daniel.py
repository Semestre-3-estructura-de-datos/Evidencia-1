import shutil 

def copiar(nombre2):
    shutil.copy('archivos/Documento.txt',nombre2)
    print("El Documento ya esta copiado :)")

def mover():
    shutil.move('archivos/Documento.txt','archivo_mover',copy_function=shutil.copy)
