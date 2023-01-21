#denuevo se importan modulos
from songs.song import*
from imports import*

def ingreso():
    #se usa la funcion del modulo song
    imperialmarchtheme()
    while True:
        #se le pide al usuario que ingrese algun nombre y este tambien sera usado como nombre de archivo
        cls()
        name = input("ingrese el nombre del recluta: ")
        FileName1 =  name + ".txt" 
        FileName = str("code/Reclutas/" +FileName1)
        
        cls()

        #el ususario debe ingresar los datos que se le solicitan4
        try:
            peso = int(input("ingrese el peso en Kg: "))
            peso2 = peso
            cls()
        except ValueError:
            print("no es un numero")
            pause()
            cls()
            continue

        try:
            altura = (input("ingrese la altura en CM: "))
            altura2 = altura
            cls()

        except:
            print("no es un numero")
            pause()
            cls()
            continue
        
        try:
            #se genera el txt y se escribe el nombre
            f = open(FileName,"x")
            f.write("Nombre del Recluta: "+str(name)+"\n")
        except:
            print("el archivo de nombre ya extste cambia el nombre o pone un numero")
            pause()
            cls()
            continue

        # a partir del archivo txt generado se agregan los datos al final de este
        f = open(FileName,"a")
        f.write("peso: "+str(peso)+"\n")

        f = open(FileName,"a")
        f.write("altura: "+str(altura)+"\n")

        #se declaran variables que almacenan el resultado de comparar si algo es mayor o igual a una cifra
        finalt = int(altura2) >= 180
        finpes = int(peso2) >= 95

        finalt2 = int(altura2) >= 170
        finpes2 = int(peso2) >= 70

        #se comparan los resultados almacenados en las variables para que dependiendo de estos se llege a
        #un resultado para asignar la mision al recluta
        if finalt and finpes:
            f = open(FileName,"a")
            f.write("mision: labores de seguridad\n")

        elif int(altura2) >= 170 or int(altura2) < 180 and int(peso2) > 70 or int(peso2) < 95:
            f = open(FileName,"a")
            f.write("mision: grupo de asalto armado")

        else:
            f = open(FileName,"a")
            f.write("mision: labores de exploracion en luna endor")
            f.close()
            cls()
        print("Los datos se guardaton en: /imperio/code/reclutas/",FileName)
        pause()
        cls()

        playagain = input("===================================================\ndesea volver a agregar reclutas? (s/n)>")
        if playagain.lower() == "n":
            cls()
            os.system("pause")
            break
        cls()
        f.close()

