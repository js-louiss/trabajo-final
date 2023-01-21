#se importa un modulo y la libreria pygame con mixer para poder reproducir audios en segundo plano
#estas funciones se pueden usar en cualquier modulo
from imports import*
import socket
import sys 

try:

    from pygame import mixer

except ModuleNotFoundError:


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:

        s.connect(("www.google.com",80))
    except(socket.gaierror,socket.timeout):
        print("Asegurate de estar conectado a la red")
        pause()
        cls()
        sys.exit()
    else: 
        cls()
        print("hay modulos faltantes, se instalaran automaticamente")
        pause()
        cls()   
        import subprocess
        subprocess.call([r"code\songs\install.bat"])
        s.close()


def shutdown():
    from pygame import mixer
    mixer.init()
    mixer.music.load('code\songs\shutdownwin.mp3')
    mixer.music.play()
    cls()


def maintheme():
    from pygame import mixer
    mixer.init()
    mixer.music.load('code\songs\starwarstheme.mp3')
    mixer.music.play(loops= -1)
    cls()


def imperialmarchtheme():
    from pygame import mixer
    mixer.init()
    mixer.music.load('code\songs\starwars.mp3')
    mixer.music.play(loops= -1)
    cls()
    