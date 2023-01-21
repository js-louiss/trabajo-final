#se impostan los modulos necesarios 
from songs.song import*
from imports import*
from claves import*
from ingresoreclutas import*
from verdatos import*
from shutdowncode import*

#se "invoca" la funcion desde el modulo claves a este 
start()
while True:
    #pasa lo mismo con todas las funciones se "invocan" desde otros modulos 
    maintheme()
    #ese es un menu para que el ususario pueda elegir que hacer
    print("1. ingresar nuevo recluta\n2. revisar datos de reclutas\n3. salir\n4.apagar el equipo\n======================================")
    #en try se pone el codigo que genera un error
    try:
        select = int(input("que desea hacer: "))
        if not select:
            msgvoid()
            pause()
            cls()
            continue
    #en except se genera la exepcion y se pone un mensaje de error
    #esto aplica para todo
    except ValueError:
        cls()
        excepterror()
        pause()


    try:
        if select == 1:
            ingreso()
      

        elif select == 2:
            revisar()
    
        elif select == 3:

            cls()
            sys.exit()

        elif select == 4:
            shut()
            sys.exit()
        else: 
            msgerr()

    except NameError:
        cls()

# a qui se sale del while para que esta instruccion se ejecute cada vez que se salga del bucle while en otro modulo 
    playagain = input("===================================================\nvolver al menu principal? (s/n)>")
    if playagain.lower() == "n":
        cls()
        shutdown()
        os.system("pause")
        break
    cls()
