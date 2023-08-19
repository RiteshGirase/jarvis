import speech_recognition as sr
from speak import speak


def indicator(): 
    r = sr.Recognizer()
    speak("car automation turn on")
    while(1):   
        try:
            
          
            source = sr.Microphone()
            with source as source2:
          
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("command : ",MyText)
                
                if ('right' in MyText ) and ('on' in MyText):
                    
                    speak('right indicator turned on')
                elif ('right' in MyText ) and ('off' in MyText or 'of' in MyText):
                    
                    speak('right indicator turned off')
                elif ('left' in MyText ) and ('on' in MyText):
                    
                    speak('left indicator turned on')
                elif ('left' in MyText ) and ('off' in MyText or 'of' in MyText):
                   
                    speak('left indicator turned off')
                elif ('wiper' in MyText ) and ('on' in MyText):
                    
                    speak('wiper turned on')
                elif ('wiper' in MyText ) and ('off' in MyText or 'of' in MyText):
                   
                    speak('wiper python ind turned off')
                elif 'off' in MyText or 'car automation' in MyText or 'quit' in MyText or 'close' in MyText or 'exit' in MyText:
                    
                    speak('car automation turned off')
                return



        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("listening")
if __name__ == "__main__":
    indicator()