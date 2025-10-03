import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
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

    speak("Hey There! I am Jarvis. How may I help you? ")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query
        
if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()
        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...please wait')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            

        elif 'open youtube' in query:
            speak("Opening Youtube, Please Wait")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google, Please Wait")
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow, Please Wait")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("Opening Music, Please Wait")
            music_dir = 'C:\\Users\\Forza Motorsport\\Desktop\\temp\\Music Box'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the date' in query:
            DateCode = datetime.datetime.now()
            print("The date is= ", DateCode)
            speak(DateCode)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Forza Motorsport\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            speak("Opening Chrome, Please Wait")
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
 
        elif 'open firefox' in query:
            speak("Opening Firefox, Please Wait")
            codePath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(codePath)

        elif 'power point presentation' in query or 'powerpoint' in query:
            speak("Opening Power Point Presentation, Please Wait")
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)

        elif 'excel' in query:
            speak("Opening Excel, Please Wait")
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(codePath)

        elif 'word' in query:
            speak("Opening Word, Please Wait")
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        elif 'notepad' in query:
            speak("Opening Notepad, Please Wait")
            codePath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(codePath)


        elif 'how are you' in query:
            print("I am all good, Thanks for asking!")
            speak("I am all good, Thanks for asking!")
            print("How are you?")
            speak("How are you?")
 
        elif 'fine' in query or "good" in query:
            print("That's good")
            speak("That's good")

        elif "who made you" in query or "who created you" in query:
            print("I have been developed by scientists and computers.")
            speak("I have been developed by scientists and computers.")

        elif "introduce" in query:
            print("Sure! Hey There, I am Jarvis and I was born a week ago. I am a Desktop Assistant of this Computer and I can perform various functions such as opening applications and websites, playing music, crack jokes and search for articles on Wikipedia. This program is written in Python and uses various Text to Speech Algorithms and Libraries in order to perform functions. That's all.")
            speak("Sure! Hey There, I am Jarvis and I was born a week ago. I am a Desktop Assistant of this Computer and I can perform various functions such as opening applications and websites, playing music, crack jokes and search for articles on Wikipedia. This program is written in Python and uses various Text to Speech Algorithms and Libraries in order to perform functions. That's all.")

        elif 'thank you' in query:
            print("Is there anything else I can do for you?")
            speak("Is there anything else I can do for you?")

        if 'quit' in query or 'no thanks' in query:
            print('Okay Goodbye! See you later!')
            speak('Okay Goodbye! See you later!')
            exit()

        if 'goodbye jarvis' in query:
            print('Okay Goodbye! See you later!')
            speak('Okay. Goodbye! See you later!')
            exit()
            

        

        


        

        
