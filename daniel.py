import shutil 

def copiar(nombre):
    shutil.copy('Documento.txt',nombre)

def mover():
    shutil.move('Documento.txt','archivo_mover',copy_function=shutil.copy)
