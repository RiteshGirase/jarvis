from math import sin, cos, sqrt, atan2, radians
from geopy.geocoders import Nominatim

def calculate(lat1, lon1, lat2, lon2):
    R = 6370

    geoLoc = Nominatim(user_agent="GetLoc")
    # lat1=input("Starting Latitude : ")
    # lon1=input("Starting Longitude : ")
    # lat1 = 19.9733644
    # lon1 = 73.8239614
    lat_rad1 = radians(lat1 )  #insert value
    lon_rad1 = radians(lon1)
    locname1 = geoLoc.reverse(str(lat1)+", "+ str(lon1))
    print(locname1.address)


    print("\n To \n ")
    # lat2=input("Ending Latitude : ")
    # lon2=input("Ending Longitude : ")
    # lat2 = 20.011509334767222
    # lon2 = 73.79181876914272  
    lat_rad2 = radians(lat2)
    lon_rad2 = radians(lon2)
    locname2 = geoLoc.reverse(str(lat2)+", "+ str(lon2))
    print(locname2.address)


    dlon = lon_rad2 - lon_rad1
    dlat = lat_rad2- lat_rad1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

    # print("\n\n Distance : " + str(distance))
    # print (distance)
    return distance

if __name__ == "__main__":
    print(calculate(19.9733644,73.8239614,20.011509334767222,73.79181876914272))