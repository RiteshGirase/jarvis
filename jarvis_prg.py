import speech_recognition as sr
from hospitalAssistant import hospitalAssistant
from car_auto import indicator
from app_open import app_open
from speak import speak
from current_loc import current_loc
# from append_file import append

r = sr.Recognizer()


def jarvis_prg():
    speak("please command Sir")
    while(1):   
        
        try:
            
            with sr.Microphone() as source2:
                
                r.adjust_for_ambient_noise(source2, duration=0.2)
               
                audio2 = r.listen(source2)
               
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                
                print("Did you say : ",MyText)
                if('where' in MyText and 'i' in MyText):
                    current_loc()
                if 'open' in MyText or 'turn on' in MyText:
                        if 'website' in MyText :
                            app_open("website")
                            
                        elif 'url' in MyText :
                            app_open("url")
                if (('car automation' in MyText or 'car' in MyText )and ('open' in MyText or 'turn on' in MyText)):
                    indicator()
                if 'hospital' in MyText and ('open' in MyText or 'turn on' in MyText):
                    hospitalAssistant()
                # if 'open file' in MyText or 'turn on file' in MyText:
                #     append()
      
                if 'quit' in MyText or 'exit' in MyText  or 'close' in MyText :
                    speak("jarvis closing")
                    break
                    exit()

                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("listening")

if __name__ == "__main__":
    jarvis_prg()
