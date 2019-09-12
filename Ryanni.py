import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import vlc
import time
import os
import sys


            # You have to successfully import all the above library file






 
engine = pyttsx3.init()

client = wolframalpha.Client('XXXXXXXXXXXXXX')      #Create your wolframalpha id and put it in the place of XXXXXXXXXXXXXX
                                                    #For creating id google wolframalpha and go into their site and create your personal id 

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Ryanni: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def welcome():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

welcome()

speak('Hello Pallab Sir, I am your digital assistant Ryanni, the Lady Jarvis!')  #Here you can add your name by changing this name 'Pallab'
speak('How may I help you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        
    try:
        q = r.recognize_google(audio, language='en-in')
        print('User: ' + q + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        q = str(input('Write here : '))

    return q



while True:
    q=myCommand();
    q=q.lower()
    if q=="who create you" or q=="who create you?" or q=="who created you?" or q=="who created you" or q=="what's your father name" or q=="what's your mother name" or q=="what is your father name" or q=="what is your father's name" or q=="what is your mother name" or q=="what is your mother's name":
        speak('Pallab sir created me, he is my father and mother')           # Here you can put your name, now it is my name
    elif q=="what is your name?" or q=="what is your name" or q=="whats your name?"or q=="whats your name" or q=="who are you" or q=="your name" or q=="name":
        speak('My name is Ryanni.')
        speak("And yours: ")
        name=str(input('Type your name:  ')).lower()
        if name=="pallab" or name=="pallab bag" or name=="pallabbag":
            speak("Nice to meet you Sir.")
        else:
            speak("Nice to meet you " +name)
    elif 'open youtube' in q:
            speak('okay')
            webbrowser.open('www.youtube.com')

    elif 'open google' in q:
            speak('okay')
            webbrowser.open('www.google.co.in')
    elif 'open facebook' in q:
            speak('okay')
            webbrowser.open('www.facebook.com')
    elif 'open gmail' in q:
            speak('okay')
            webbrowser.open('www.gmail.com')

    elif "what's up" in q or "whats up" in q:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

    elif q=="what is your age" or q=="what is your age?":
        speak("My date of birth is  First April, 2019")
    elif q=="who is god" or q=="what is god" or q=="who is krishna" or q=="krishna" or q=="supreme personility of godhead":
        speak('Krishna is the supreme personility of godhead.')
    elif q=="play music" or q=="play song" or q=="play any song":
        sound_path=" type address of song "                                                     # type address of file which contain songs like C:\\songs\\ 
        sound_name=[" type songs name for random playing"," type songs name for random playing"," type songs name for random playing"," type songs name for random playing"," type songs name for random playing"]
        song=sound_path + random.choice(sound_name) + '.mp3'
        ready_song=vlc.MediaPlayer(song)
        ready_song.play()
        speak('ok')
        time.sleep(10)
    elif q==" set your song name " or q==" set your song name " or q=="put different different pronunciation for more easily recognising the song":   # Hare you can set your favorite song name from local desktop 
        mang=vlc.MediaPlayer("put address of your song name with proper extension like .mp3")               # Put address of your song with song name and extension
        mang.play()
        speak('ok')
        time.sleep(10)
    elif q=="set your sng name" or q==" set your song name ":                          # Hare you can set your favorite song name from local desktop
        nar=vlc.MediaPlayer("put address of your song name with proper extension like .mp3")                       # Put address of your song with song name and extension
        nar.play()
        speak('ok')
        time.sleep(10)
    elif q=="today is my birthday" or q=="today is my birth day":
        wish=["Wishing you a beautiful day with good health and happiness forever. Happy birthday!","Here’s wishing you a day full of pleasant surprises! Happy birthday!","Happy Birthday! Hope your special day brings you all that your heart desires!","Wishing you a day filled with happiness , Happy Birth Day","Congratulations! Happy Birth Day","Happy birthday! May your Facebook wall be filled with messages from people you never talk to.","Your birthday is the first day of another 365-day journey. Happy Birth Day and Enjoy the ride.","Count not the candles…see the lights they give.Happy birthday.","This birthday, I wish you abundant happiness and love.","Happy birthday! Your life is just about to pick up speed and blast off into the stratosphere.","Wishing you a very happy birthday!","Wishing you a very happy and fun-filled birthday!","Happy birthday! I hope all your birthday wishes and dreams come true."]
        w=random.choice(wish)
        speak(w)
        time.sleep(5)
    elif q=="bye" or q=="exit" or q=="take rest" or q=="stop" or q=="nothing" or q=="abort":
        speak('ok bye, have a good day')
        speak('See you soon')
        break
    else:
        q=q
        speak('Searching')
        try:
            try:
                res=client.query(q)
                output=next(res.results).text
                speak('Got it.')
                speak(output)

            except:
                res = wikipedia.summary(q,sentences=2)
                speak('Got it')
                speak('WikiPedia says - ')
                speak(res)

        except:
            webbrowser.open('www.google.com')

    speak('Next command sir..')


