import sys                         #buildin module
import pyttsx3                     #pip install pyttsx3
import datetime                    
import speech_recognition as sr    #pip install speechrecognition
import wikipedia                   #pip intall wikipedia
import webbrowser                
import os 
import random 
import smtplib                    
from sys import exit               #for exit() from the while loop
#import pywhatkit
 

engine = pyttsx3.init('sapi5')    #creatin an object and 'sapi5' is microsoft speech recognition technology
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #[0] index 0 is the male voice. You can choose 1 for girl


def speak(audio):                        #this function use here to producing sound from M.S speech recognition
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour) #this will give the only hour from current datetime module
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>12 and hour<=18:
        speak("Gud Afternoon!")
    else:
        speak("Good Evening")
    speak("Helo sir! I am Jarvis! please tell me how can i help you")

def takeCommand():                  #it take the microphone input from user and change it to the string format                         
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(sourse)
    
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as a:
        print("Say that again please...") 
        return "None"
    return query
 
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587) 
    server.ehlo()
    server.starttls()
    server.login('YourGmailId@gmail.com','GmailPassword')
    server.sendmail('YourGmailId@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    
     wishMe()
     while True:
         query=takeCommand().lower()

         #logic for executing task bassed on querry
         if 'wikipedia' in query:
             speak("Searching wikipedia...")
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query,sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)

         elif 'open youtube' in query:
             print("loading...")
             webbrowser.open("youtube.com")
            
         elif 'open google' in query:
             print("loading...")
             webbrowser.open("google.com")
          
         elif 'open linkedin' in query:
             print("loading...")
             webbrowser.open("linkedin.com")

         elif 'play music' in query:
             music_dir = 'D:\\video'
             songs = os.listdir(music_dir)
             x=random.randint(0,len(songs)-1)
             print(songs)
             os.startfile(os.path.join(music_dir,songs[x]))

         elif 'time' in query:
             strtime=datetime.datetime.now().strftime("%H:%M:%S")
             print(strtime)
             speak(f"Sir!, the time is {strtime}") 
        
         elif 'sublime' in query:
             codePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
             print("loading...")
             os.startfile(codePath)

         
         elif 'email' in query:
             try:
                 speak("what should i say")
                 content = takeCommand()
                 to = "vikashcs.iimt@gmail.com"
                 sendEmail(to, content)
                 speak("email has been sent!")
                 
             except Exception as e:
                 speak("sorry my friend vikash , please try again ")
         quit=input("Quit or Exit type y/n: ")
         if quit=="y":
             sys.exit()
                
         #elif 'whatsapp' in query:
         #    pywhatkit.sendwhatmsg("+917903126335","oooya",10,12)