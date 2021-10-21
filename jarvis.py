import wikipedia
import speech_recognition as sr 
import pyttsx3
import datetime
import webbrowser 
import os
import random 





chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis. Please tell me how may I help you?")

def takeCommand():
    #takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  #non speaking time
        r.energy_threshold = 250 #pitch of the speaker
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"

    return query



if __name__ == "__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")

        elif 'open googlemap' in query:
            webbrowser.get(chrome_path).open("www.google.co.in//maps")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")

        elif 'open mail' in query:
            webbrowser.get(chrome_path).open("gmail.com")

        elif 'play music' in query:
            music_dir = "E:\\Anu\\MUSIC"
            songs = os.listdir(music_dir)
            music = random.choice(songs)
            #print(songs)
            os.startfile(os.path.join(music_dir,music))
            os.system("pause")

        elif 'search' in query:
            try:
                url ="https://www.google.co.in/search?q="
                search_url = url + query
                webbrowser.get(chrome_path).open(search_url)
            except:
                print("Sorry. Please say it again!")
