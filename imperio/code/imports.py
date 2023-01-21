#se importan unas cuantas librerias y se declaran unas pocas funciones que se usaran en otros modulos
import os 
import random
def pause():
    os.system("pause")

def cls():
    os.system("cls")

def msgerr():
    msgerr = ["opcion no valida","lo siento no puedo encontrar esta opcion","creo que las opciones son solo las que vez","creo que te equivocaste"]
    selmsg = random.choice(msgerr)
    print(selmsg)

def msgvoid():
    msg = ["no puede quedar vacio","esta vacio","tengo que recordartelo...NO DEJES COSAS EN BLANCO","vas a dejarlo en blanco??? no puede ser"]
    selmsg = random.choice(msg)
    print(selmsg)

def claveerr():
    msgerr = ["clave invalida","esa no es la clave","te sabes la calve?"]
    selerr = random.choice(msgerr)
    print(selerr)

def clavecorr():
    msgcorr = ["clave correcta","bienvenido user23","hola denuevo","acertaste la calve"]
    selcorr = random.choice(msgcorr)
    print(selcorr)

def excepterror():
    exerr = ["creo que eso es una letra","no puedes usar letras"]
    selerr = random.choice(exerr)
    print(selerr)

def errfound():
    err = ["el archivo no exixte","no lo encuentro","fijate de que este bien escrito"]
    sellerr = random.choice(err)
    print(sellerr)
    