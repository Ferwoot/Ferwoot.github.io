from beeply import notes
from covid import Covid
from gtts import gTTS
import speech_recognition as sr
from time import ctime
import datetime
import os
import os.path
import playsound
import random
import serial
import time
import webbrowser

r = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            Elisa_speak(ask)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='es-SP')
        except sr.UnknownValueError:
            Elisa_speak('Disculpa, no te entendí')
        except sr.RequestError:
            Elisa_speak('Disculpa, mi servicio de voz no funciona')
        return voice_data

def Elisa_speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'es')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def saludo_inicial():
    '''this function simple wish me to and speak.'''
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12 : 
        Elisa_speak("Buenos dias")

    elif hour >=12 and hour < 18:
        Elisa_speak("Buenas tardes")

    else:
        Elisa_speak("Buenas noches")
    
    Elisa_speak('Estoy lista. ¿Cómo puedo ayudarte?')

def name():
    Elisa_speak('Mi nombre es Elisa')

def hour():
    Elisa_speak(ctime())

def search():
    search = record_audio('Que es lo que deseas que busque?')
    url = 'https://www.google.com/search?q=' + search
    webbrowser.get().open(url)
    Elisa_speak('esto es lo que encontré ' + search)

def local():
    location = record_audio('Dime la direccion que debo ubicar')
    url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
    webbrowser.get().open(url)
    Elisa_speak('esta es la dirección ' + location)

def video():
    video = record_audio('Dime el video que deseas ver')
    url = 'https://www.youtube.com/results?search_query=' + video 
    webbrowser.get().open(url)
    Elisa_speak('Este es el video que encontré ' + video)

def code():
    Elisa_speak('Abriendo Visual Studio Code...')
    code_path = "C:\\Users\\Windows10\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(code_path)

def word():
    Elisa_speak('Abriendo Office Word...')
    code_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
    os.startfile(code_path)

def edge():
    Elisa_speak('Abriendo Microsoft Edge...')
    code_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    os.startfile(code_path)

def covidd():
    covid = Covid()
    covid.get_data()
    Elisa_speak("Confirmados en total: " + str(covid.get_total_confirmed_cases())) # Get total confirmed cases from JHU CSSE
    Elisa_speak("Muertes: " + str(covid.get_total_deaths())) # Get total deaths from JHU CSSE
    Elisa_speak("Recuperados: " + str(covid.get_total_recovered()))

def covperu():
    covid = Covid()
    covid.get_data()
    cov = str(covid.get_status_by_country_name('Peru')) # Search for country and save result in variable
    Elisa_speak(cov)

def comercio():
    Elisa_speak('Te recomiendo este diario...')
    webbrowser.open('https://elcomercio.pe/')


def respond(voice_data):
    Elisa_speak('Dime que puedo hacer por ti')
    if 'nombre' in voice_data:
        name()
    elif 'hora' in voice_data:
        hour()
    elif 'busca' in voice_data:
        search()
    elif 'lugar' in voice_data:
        local()
    elif 'musica' in voice_data:
        video()
    elif 'coronavirus' in voice_data:
        covidd()
    elif 'país' in voice_data:
        covperu()
    elif 'hoy' in voice_data:
        comercio()
    elif 'caja' in voice_data:
        Elisa_speak('Ingresa la contraseña en el teclado')
        arduino()
    elif 'visual' in voice_data:
        code()
    elif 'hojas' in voice_data:
        word()
    elif 'internet' in voice_data:
        edge()
    elif 'gracias' in voice_data:
        Elisa_speak('Denada, puedo ayudarte en algo mas?')
        # pronto mas codigo
        quit()

m=3
def arduino():
    m=3
    serArduino = serial.Serial('COM3',9600)
    time.sleep(1)
    for m in range(m,-1,-1):
        try:

            datosASCII = serArduino.readline().decode().rstrip() 
            print(datosASCII)
            if datosASCII != '16A0':
                Elisa_speak('contraseña errónea')
            elif datosASCII == '16A0':
                Elisa_speak('abierto')
            raios()
        except datosASCII.UnknownValueError:
            print('error al leer datos')

def raios():
    if m==1:
        print('pista, pista. 4 al cuadrado, la primera letra de tu apellido y la nota que sacas si no estudias')
    if m==0:
        print('Alarmas activadas')
        alarma()

def alarma():
    mybeep = notes.beeps(2000)
    i = 0
    for i in range(8):
        mybeep.hear('A_', 1000)
        i +=1
    return voice_data

time.sleep(1)
saludo_inicial()
while 1:
    voice_data = record_audio()
    respond(voice_data)










