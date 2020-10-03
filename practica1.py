import requests
import json

output = []
def link(url):
    rq = requests.get(url)
    return (json.loads(rq.content))

key = str(input("Api key (OpenWeatherMap): "))
output.append(link("https://api.openweathermap.org/data/2.5/weather?q=Barcelona&units=metric&appid="+key))
output.append(link("https://api.openweathermap.org/data/2.5/weather?id="+key))
output.append(link("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid="+key))

with open("practica1.txt","w+") as txt:
    for i in output:
        txt.write(str(i)+"\n")