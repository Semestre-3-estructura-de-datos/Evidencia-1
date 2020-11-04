import shutil 

def copiar(nombre):
    shutil.copy('Documento.txt',nombre)
    print("El Documento ya esta copiado :)")

def mover():
    shutil.move('Documento.txt','archivo_mover',copy_function=shutil.copy)
