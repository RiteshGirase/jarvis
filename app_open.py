import speech_recognition as sr
import webbrowser
from speak import speak

r = sr.Recognizer()
def app_open(toOpen):
    speak("Please speak your " +toOpen+" name ")

    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                app = r.recognize_google(audio2)
                app = app.lower()
                
                if app!="" and 'website' in toOpen :
                    speak("opening " +app)
                    webbrowser.open("www."+app+".com")
                    return 
                elif app!="" and 'url' in toOpen :
                    speak("opening " +app)
                    webbrowser.open("https://"+app)
                    return 
                

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("listening")

if __name__ == "__main__":
    app_open("website")