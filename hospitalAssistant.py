from latitude_longitude_distance import calculate
import pyodbc
import speech_recognition as sr
import geocoder
from geopy.geocoders import Nominatim
import speech_recognition as sr
import copy
from speak import speak

def hospitalAssistant():
    r = sr.Recognizer()
    geoLoc = Nominatim(user_agent="GetLoc")

    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\HP\Documents\Bank.accdb;')
    cursor = conn.cursor()
    geoLoc = Nominatim(user_agent="GetLoc")

    # def speak(cmd):
    #     engine = pyttsx3.init()
    #     engine.say(cmd )
    #     print(cmd )
    #     engine.runAndWait()
    

    def hospital_list():
        list="select hname from hospital"
        cursor.execute(list)
        list = cursor.fetchall() # to fecth whole column use fetchall()
        return list    
    def coordinate(x):
        no=""
        for i in range(len(x)):
            if(x[i]>='0' and x[i]<='9') or x[i] ==".":
                no=no+x[i]
        
        return no

    def isHospital(MyText):
        list =hospital_list()
        for name in list :
            hospitalName=""
            for  i in range(len(name)) :
                if (name[i]>='a' and name[i]<='z') or (name[i]>='A' and name[i]<='Z') or name[i]==" "or name[i]=="'"or name[i]==".":
                    hospitalName=hospitalName+name[i]
            if hospitalName in MyText:
                return hospitalName


    def getLat(hospitalName):
        lat="select lat from hospital where hname = '"+hospitalName+"'"
        cursor.execute(lat)
        lat=cursor.fetchone()
        lat=coordinate(lat)
        return lat

    def getLon(hospitalName):
        lng="select lng from hospital where hname = '"+hospitalName+"'"
        cursor.execute(lng)
        lng=cursor.fetchone()
        lng=coordinate(lng)
        return lng


    def add( MyText ):    
        hospitalName = isHospital(MyText)
        print(hospitalName)
        if hospitalName != None :
            lat = getLat(hospitalName)
            lng = getLon(hospitalName)
            print("lat : ",lat)
            print("lng : ",lng)
            locname = geoLoc.reverse(str(lat)+", "+ str(lng))
            speak(hospitalName+" hospital address is "+ locname.address)

        else:
            speak("hospital not found , sorry")
    def find(MyText):
        list =hospital_list()
        min = 99999999999.9
        for name in list :
            hospitalName=""
            for  i in range(len(name)) :
                if (name[i]>='a' and name[i]<='z') or (name[i]>='A' and name[i]<='Z') or name[i]==" "or name[i]=="'"or name[i]==".":
                    hospitalName=hospitalName+name[i]

            if hospitalName != None:
                lat = getLat(hospitalName)
                lng = getLon(hospitalName)
                distance = calculate(19.9733644,73.8239614,float (lat),float (lng))
                if min > distance:
                    min = distance
                    minLat=float (lat)
                    minLng=float (lng)
        locname = geoLoc.reverse(str(minLat)+", "+ str(minLng))

        speak("distance from upnagar to "+ locname.address + " is : "+ str (min)+ " kilo meters  " )

    def hospital():
        speak('Welcome to  hospital  assist')
        while(1):   
            
            try:
                
                with sr.Microphone() as source2:
                    
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    
                    
                    audio2 = r.listen(source2)
                    
                
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()
        
                    print("Did you say : ",MyText)
                    if('hospital' in MyText and 'list' in MyText):
                            list = hospital_list()
                            speak(list)

                    if 'address' in MyText :
                        add(MyText)

                    if ('nearby' in MyText or 'near' in MyText or 'closest' in MyText or 'nearest' in MyText or 'short' in MyText or 'long' in MyText ) and 'hospital' in MyText :
                        find(MyText)
                        
                    if 'quit' in MyText or 'exit' in MyText or 'close' in MyText:
                        speak("closing hospital assistant")
                        return
                    
                    
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
                
            except sr.UnknownValueError:
                print("listening")
        conn.close()
    hospital()

    

if __name__ == "__main__":
    hospitalAssistant()
