import speech_recognition as sr
import pyttsx3 
from datetime import datetime
from datetime import date
import os

def say(speech): 
    #Robot Reply ... -> Read
    converter.setProperty('rate', 150) 
    converter.setProperty('volume', 0.7) 
    converter.say(speech) 
    
    converter.runAndWait()


converter = pyttsx3.init() 
r = sr.Recognizer()
welcome = "Hello, welcome to A I robot"
print("Robot: "+ welcome)
say(welcome)
while 1: 
    ###Robot Listen
    Robot = "I'm listening. Say something ..."
    you = ""
    print("Robot: " + Robot)
    say(Robot)
    try: 
        with sr.Microphone() as source:    
            audio = r.record(source, duration = 4)                   
            try:
                you = r.recognize_google(audio)
            except LookupError: 
                you = "Could no understand audio"                           
            print("You: " + you)   
    except: 
        you = ""
   


    ### AI --> Robot Brain
    if "hello" in you: 
        Robot = "Hello FoveIT"
    elif you=="":
        Robot = "You are busy, aren't you?. Goodbye!"
        print("Robot: "+ Robot)
        converter.say(Robot) 
        converter.runAndWait()
        break
    elif "your name" in you:
        Robot = "My name is AI robot"
    elif "bye" in you:
        Robot = "Goodbye, See you next time"
        print("Robot: "+ Robot)
        converter.say(Robot) 
        converter.runAndWait()
        break
    elif "time" in you:
        now = datetime.now()
        Robot = now.strftime("%H:%M:%S")
    elif "president" in you:
        Robot = "John Biden"
    elif "search" in you:
        Robot= "I'm searching it in google, please wait me..."
        #os.start("wwww.google.com")
    elif "today" in you: 
        today = date.today()
        Robot = today.strftime("%B %d, %Y")
    else:
        Robot = "I can't understand you"

    ###Robot Say
    print("Robot: "+ Robot)
    say(Robot)
    say(you)

