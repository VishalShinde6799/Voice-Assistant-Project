import pyttsx3
import datetime
from datetime import date
import time
import speech_recognition as sr
import wikipedia
import sys
import webbrowser
import os
import random
import dictest as dt
import jarvis_history
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def takeCommand():

    r= sr.Recognizer()
    print("Listening....")
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.phrase_threshold= 0.3
        audio= r.listen(source)
    #return audio

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        f= query.title()
        print(f"User said::  {f}\n")
    
    except Exception as e:
        speak("Say that again please....")
        return "None"
    return query

def storeCommand():
    return takeCommand().query.title()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():

    hour=int(datetime.datetime.now().hour)
    dt1=date.today()
    hour1=datetime.datetime.now().strftime("%H %M %S")
    speak(f"the date is {dt1}")
    if hour>=4 and hour<12:
        speak("Good morning User!")
        speak(f"the time is {hour1}")
    elif hour>=12 and hour<18:
        speak("Good afternoon User!")
        speak(f"the time is {hour1}")
    elif hour>=18 and hour <20:
        speak("good evening User!")
        speak(f"the time is {hour1}")
    else:
        speak("its late in the night Dear!")
        speak(f"the time is {hour1}") 

#if __name__ == "__main__":
def meta():
    wishme()
    time.sleep(0.5)
    print(f"myself david... would you like a joke......?")
    speak(f"myself david... would you like a joke......?")
    vns=takeCommand().lower()
    if 'yes' in vns:
        speak("here you go.....")
        speak(dt.jokeswille())

    else:
        speak("all right...")
    print(" how can i be of assistance?")
    speak(" how can i be of assistance?")
    abc=True
    while abc:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia")
            query=query.replace("wikipedia", " ")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif query=='goodbye':
            speak("i will see you later")
            abc=False
            sys.exit()    

        elif 'open google' in query:
            speak("okay... opening google!!")
            webbrowser.open('google.com')
            #sys.exit()

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            #sys.exit()
        elif 'open github' in query:
            webbrowser.open('github.com')  
            #sys.exit()

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')   
            #sys.exit()

        elif 'play music' in query:
            speak("okay... playing music!!")
            music_dir= "F:\\Music"
            songs=os.listdir(music_dir)

            in1=random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[in1]))
            #sys.exit()

        elif 'play a movie' in query:
            speak("okay... playing a movie!!")
            mov_dir="F:\\MOVIES\\"
            mov=os.listdir(mov_dir)

            in1=random.randint(0, len(mov)-1)
            os.startfile(os.path.join(mov_dir, mov[in1]))    
            #sys.exit()
            

        elif 'my music' in query:
            music_dir= "F:\\Music"
            songs=os.listdir(music_dir)

            for music in range(0, len(songs)):
                print(f"{music}.{songs[music]}")
        
        elif 'open pubg' in query:
            speak("okay... Get to the safe zone!!")
            os.startfile("H:\\Program Files\\txgameassistant\\appmarket_2784781\\AppMarket.exe")
            #sys.exit()

        elif 'open whatsapp' in query:
            speak("okay... chit chat!!")
            os.startfile('C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_0.3.1847.0_x64__cv1g1gvanyjgm\\app\\WhatsApp.exe')
            #sys.exit()
        
        elif 'the time' in query:
            hour1= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {hour1}\n")
            print(hour1)
            speak("BY the way.... time is an illusion")
            #print(time.time())
            #sys.exit()

        elif 'a joke' in query:
            speak("Here's your joke........")
            speak(dt.jokeswille())
            #sys.exit()    

        elif 'study material' in query:
             speak("okay.... opening your study material")
             os.startfile("H:\\STUDY_MATERIAL")
             #sys.exit()

        elif 'my media' in query:
            speak("okay... here you go!!")
            os.startfile("F:")
             #sys.exit()

        elif 'my games' in query:
             os.startfile("G:")
             #sys.exit()

        elif 'calculation' in query:
            speak("what do you want to calculate...?")
            speak("1. addition, 2. subtraction, 3. product, 4. division")
            query1=takeCommand().lower()

            if 'subtraction' in query1:
                speak("enter the first number...")
                no1=int(takeCommand().lower())
                time.sleep(0.5)
                speak("enter the second number...")
                no2=int(takeCommand().lower())
                no3=no1-no2
                print(f"the difference is {no3}")
                speak(f"the difference is {no3}")

            elif 'addition' in query1:
                speak("enter the first number...")
                no1=int(takeCommand().lower())
                time.sleep(0.5)
                speak("enter the second number...")
                no2=int(takeCommand().lower())
                no3=no1+no2
                print(f"the addition is {no3}")
                speak(f"the addition is {no3}")

            elif 'product' in query1:
                speak("enter the first number...")
                no1=int(takeCommand().lower())
                time.sleep(0.5)
                speak("enter the second number...")
                no2=int(takeCommand().lower())
                no3=no1*no2
                print(f"the product is {no3}")
                speak(f"the product is {no3}") 

            elif 'division' in query1:
                speak("enter the first number...")
                no1=int(takeCommand().lower())
                time.sleep(0.5)
                speak("enter the second number...")
                no2=int(takeCommand().lower())
                no3=no1/no2
                print(f"the division is {no3}")
                speak(f"the division is {no3}")       
            jarvis_history.jarv_db(query1)

        elif 'history' in query:
            jarvis_history.show_his()

        elif 'email' in query:
            speak('Who is the recipient?')
            recipient@mail = takeCommand().lower()

            if 'vishal' in recipient@mail:
                speak('What should I say to him?')
                content = takeCommand().title()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('sneder@mail', 'Sender_passwd')
                mail.sendmail('sneder@mail', 'recipient@mail', content)
                mail.close()
            
            
            elif 'cowstoob' in recipient@mail:
                speak('What should I say to him?')
                content = takeCommand().title()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('sneder@mail', 'Sender_passwd')
                mail.sendmail('sneder@mail', 'recipient@mail', content)
                mail.close()
            

            elif 'dakshata' in recipient@mail:
                speak('What should I say to her?')
                content = takeCommand().title()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('sneder@mail', 'Sender_passwd')
                mail.sendmail('sneder@mail', 'recipient@mail', content)
                mail.close()
            

            elif 'shruti' in recipient@mail:
                speak('What should I say to her?')
                content = takeCommand().title()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('sneder@mail', 'Sender_passwd')
                mail.sendmail('sneder@mail', 'recipient@mail', content)
                mail.close()

            elif 'group' in recipient@mail:
                speak('What should I say to the group?')
                content = takeCommand().title()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('sneder@mail', 'Sender_passwd')
                mail.sendmail('sneder@mail', 'recipient@mail', content)
                mail.sendmail('sneder@mail', 'recipient@mail', content)
                mail.sendmail('sneder@mail', 'recipient@mail', content)
                mail.close()

            print('Email has been sent successfuly. You can check your sentbox.')
            speak('Email has been sent successfuly. You can check your sentbox.')

        else:
            print('Command not recognized, please try again...!')
            speak('Command not recognized, please try again...!')

        jarvis_history.jarv_db(query)
        print("wait some time before giving next command")
        speak("wait some time before giving next command")
        time.sleep(4)

if __name__ == "__main__":
    meta()

#.............................................END...........................................#