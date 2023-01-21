from imports import*
from songs.song import*

#se le permite al usuario revisar el archivi txt de un recluta dependiendo del nombre
def revisar():
    imperialmarchtheme()
    while True:
        cls()
        selecction = input("ingrese el nombre para buscar: \n")
        if not selecction:
            msgvoid()
            pause()
            cls()
            continue

        cls()

        try:
            #se añade la extension txt a la variable seleccion y se abre el archivo y se deja 
            #listo para leer
            sel = selecction + ".txt"
            sel2 = str("Reclutas/" + sel)
            #se lee el archivo y se muestra por pantalla
            f = open(sel2,"r")
            print(f.read())
            f.close()
        
        #se lanza un mensaje de archivo no encontrado en caso de que el archivo seleccionado no exista
        except:
            errfound()
            pause()
            cls()
            continue           
        
        #esto hace que se salga del while en caso de que sea no y se pueda volver al menu principal
        playagain = input("===================================================\ndesea volver a revisar datos? (s/n)>")
        if playagain.lower() == "n":
            cls()
            os.system("pause")
            break
        cls()
        