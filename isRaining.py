import requests

def apirequest(a, b): #a is lattitude, b is longitude, function creates api url to call
    api="http://api.openweathermap.org/data/2.5/weather?lat="
    api+=str(a)
    api+="&lon="
    api+=str(b)
    api+="&APPID=6cb2a52bb77a7c60fde88c2a1c7e4371"
    return api

def precipitation():
    weather = data['weather']
    description = weather[0]['description']  # used to check weather description for rain
    precipitation = ("rain" in description) | ("snow" in description) | ("sleet" in description) | (
    "hail" in description) | ("showers" in description)
    return precipitation

def currentTemp():
    temp = data['main']
    currenttemp = temp['temp']  # finds current temperature in kelvin
    currenttemp = (currenttemp - 273.15) * (9.0 / 5.0) + 32
    return currenttemp



lat=float(input("Enter Latitude"))
long=float(input("Enter Longitude"))
apiurl=apirequest(lat,long)


response=requests.get(apiurl)
data=response.json()

#ispleasant = FALSE
#temperaturestorage = currenttemp
#if temperaturestorage >= 55 and temperaturestorage <= 80
#    ispleasant = TRUE

print(precipitation(),currentTemp())
#print("Current Temperature: ",currenttemp)
#print("Precipitation: ",precipitation)





