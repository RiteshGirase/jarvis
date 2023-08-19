import geocoder
from geopy.geocoders import Nominatim
from speak import speak

def current_loc():
    g = geocoder.ip('me')
    geoLoc = Nominatim(user_agent="GetLoc")
    

    print("\n Current latitude : ",g.lat)
    print("\n Current longitude : ",g.lng)
    locname = geoLoc.reverse(str(g.lat)+", "+ str(g.lng))
    

    
    speak(' you are at '+str(locname.address))
    return

if __name__ =="__main__":
    current_loc()
    
