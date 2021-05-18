import pyttsx3
import serial
import time
from beeply import notes

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 175)     # setting up new voice rate

serArduino = serial.Serial('COM3',9600)
time.sleep(1)


def raios():
    if m==1:
        engine.say('pista, pista. 4 al cuadrado, la primera letra de tu apellido y la nota que sacas si no estudias')
        engine.runAndWait()
        engine.stop()
    if m==0:
        engine.say('Alarmas activadas')
        engine.runAndWait()
        engine.stop()
        alarma()

def alarma():
    mybeep = notes.beeps(2000)
    i = 0
    for i in range(8):
        mybeep.hear('A_', 1000)
        i +=1

for m in range(3,-1,-1):
    try:

        datosASCII = serArduino.readline().decode().rstrip() 
        print(datosASCII)
        if datosASCII != '16A0':
            engine.say('contraseña errónea')
            engine.runAndWait()
            engine.stop()
        elif datosASCII == '16A0':
            engine.say('abierto')
            engine.runAndWait()
            engine.stop()
        raios()
    except datosASCII.UnknownValueError:
        engine.say('error al leer datos')
        engine.runAndWait()
        engine.stop()