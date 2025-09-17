from creador import *
import shutil
import os
#Crea una familia y annnadele tres integrantes
def make_dir(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"Carpeta '{carpeta}' creada.")
    else:
        print(f"La carpeta '{carpeta}' ya existe.")
def main_start():
    for i in ['SAm', 'Pam', 'Kam']:
        i = Familia(i)
        i.constructor_familia()
    print(Familias)    
def fam_saver(mode = None):
    os.chdir('/Users/jorge/OneDrive/Documentos/Nueva carpeta')
    carpeta = 'family_files'
    if mode == 0:
        if os.path.exists(carpeta):
            shutil.rmtree(carpeta)
            print(f"Carpeta '{carpeta}' y su contenido fueron eliminados.")
        else:
            print(f"La carpeta '{carpeta}' no existe.")
    make_dir(carpeta)
    ruta_b = '/Users/jorge/OneDrive/Documentos/Nueva carpeta/family_files'
    for families in Familias:
        nom =families.nombre_familia
        os.chdir(ruta_b)
        families: Familia
        make_dir(nom)
        ruta_c= f'/Users/jorge/OneDrive/Documentos/Nueva carpeta/family_files/{nom}'
        os.chdir(ruta_c)
        for person in families.miembros:
            person: Persona
            nombre = f'{person.nombre}_{families.nombre_familia}' 
            with open(f'{nombre}.txt', 'w', encoding='utf-8') as f:
                for i in [person.nombre, str(person.edad), person.genero,str(person.personalidad) ,str(person.moralidad), person.oficio,
                          str(person.padre), str(person.madre), str(person.adn)]:
                    f.write(f"{i}\n")
'''
File order; family_files
-family
--name of personaje
    nombre
    edad
    genero
'''            

if __name__ == '__main__':
    main_start()
    fam_saver(0)