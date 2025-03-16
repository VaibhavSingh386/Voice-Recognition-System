import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id)
engine.setProperty("voices",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 5 and hour < 12:
        speak ("Good Morning!")
    
    elif hour >= 12 and hour < 17:
        speak ("Good Afternoon!")

    elif hour >= 17 and hour < 22:
        speak ("Good Evening!")

    else :
        speak ("Good Night!")

    speak ("I am Shaun. Sir, Please tell me how may I help you.")

def takeCommand():

    v = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        v.energy_threshold = 300
        audio = v.listen(source)
    
    try :
        print("Recognizing...")
        query = v.recognize_google(audio , language="en-in")
        print(f"User said: {query}\n")

    except Exception as e :
        print("Say that again please...")
        return None
    return query

def sendEmail(do, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.login('vaibhav.22scse1010550@galgotiasuniversity.edu.in','gu@12345')
    server.sendmail('vaibhav.22scse1010550@galgotiasuniversity.edu.in', to, content)
    server.close

if __name__ == "__main__":
    wishme()
    while True :
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open map' in query:
            webbrowser.open("maps.google.co.in")

        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.com")

        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com")    

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open online compiler' in query:
            webbrowser.open("onlinecompiler.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'open hotstar' in query:
            webbrowser.open("www.hotstar.com")

        elif 'open instagram' in query:
            webbrowser.open("Instagram.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open spotify' in query:
            webbrowser.open("Spotify.com")

        elif 'open unacademy' in query:
            webbrowser.open("Unacademy.com")

        elif 'open lms' in query:
            webbrowser.open("lms.galgotiasuniversity.org")

        elif 'open icloud' in query:
            webbrowser.open("gu.icloudems.com")

        elif 'open store' in query:
            webbrowser.open("apps.microsoft.com")

        elif 'tell the weather' in query:
            webbrowser.open("www.msn.com") 
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\91902\\Pictures\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play video' in query:
            movies_dir = 'C:\\Users\\91902\Downloads\\Bollywood Movies\\The.Family.Man'
            videos = os.listdir(movies_dir)
            print(videos)
            os.startfile(os.path.join(movies_dir, videos[3]))

        elif 'show time' in query :
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strTime}')

        elif 'tell the date' in query :
            strDate = datetime.datetime.now().strftime('%m/%d/%y')
            speak(f'Sir, today is {strDate}')

        elif 'open vs code' in query :
            code = "C:\\Users\\91902\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            os.startfile(code)

        elif 'open ms excel' in query :
            excel = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"    
            os.startfile(excel)

        elif 'open ms word' in query :
            word =  "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE" 
            os.startfile(word)

        elif 'open powerpoint' in query :
            ppt =  "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(ppt)

        elif 'open brave' in query :
            browser = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"    
            os.startfile(browser)

        elif 'open chrome' in query :
            browse = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"    
            os.startfile(browse)

        elif 'open photos' in query:
            images_dir = 'C:\\Users\\91902\\Desktop\\image'
            image = os.listdir(images_dir)
            print(image)
            os.startfile(os.path.join(images_dir, image[0]))

        elif 'send email to shivam' in query:
            try :
                speak("What should I say?")
                content = takeCommand()
                to = '108shivamvivek@gmail.com'
                sendEmail(to , content)
                speak("Email has been sent")
            except Exception as e :
                print(e)
                speak("Sorry Sir. I can't able to send this email.")