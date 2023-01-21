from imports import*

#esto es solo para que si nadie tiene la clave nadie pueda acceder
def start():
    claves = "imperio"
    while True:
        cls()
        str(input("ingrese la clave: "))
        cls()
        if not input:
            msgvoid()
            pause()
            cls()

        else:
            if input != input:
                claveerr()
                print("pista: la clave es toda en minusculas")
                pause()
                cls()

            else:
                clavecorr()
                pause()
                cls()
                break

