import requests

def apirequest(a, b):
    api="http://api.openweathermap.org/data/2.5/weather?lat="
    api+=str(a)
    api+="&lon="
    api+=str(b)
    api+="&APPID=6cb2a52bb77a7c60fde88c2a1c7e4371"
    return api

lat=float(input("Enter Latitude"))
long=float(input("Enter Longitude"))
apiurl=apirequest(lat,long)


response=requests.get(apiurl)
data=response.json()

weather=data['weather']
description=weather[0]['description']
rainy="rain" in description
print(rainy)




