from calendar import month
from bs4 import BeautifulSoup
import requests
import datetime
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/58.0.3029.110 Safari/537.3'}
def weather(city):
    city=city+" weather"
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}\
    &oq={city}&aqs=chrome.0.35i3912j014146j69i60.6128j1j7&sourceid=\
    chrome&ie=UTF-8',headers=headers) 
    print("Buscando... \n")
    soup = BeautifulSoup(res.text,'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    return location, time, info, weather
city=input("Elija la ciudad ->> ")
location, time, info, weather = weather(city)
weatherstatus = info.lower()
print(str(location)+", siendo "+str(time)+"hs, el clima se encuentra "+str(weatherstatus)+\
    " y hay una temperatura de "+str(weather)+"ºC.")

# Inspirado y modificado en base al código de cLcoding.com