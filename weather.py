#City, Time, Temperature, Condition

import requests

openweathermap_key =''

url1 ='api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}'

def get_weather(city_name, api_key='a5dc08224e805ea90ec982239685a5f8' ):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    r = requests.get(url)
    content = r.json()
    s = content['list']
    
    for i in range(0, len(s)):
        x = s[i]
        orario = x['dt_txt']
        condition = x['weather'][0]['main']
        temperature = int(x['main']['temp']-273.15)
        print(f'City_name: {city_name}, Time: {orario}, Condition: {condition}, Temperature: {temperature}')
        ++i
        #temperature


get_weather(city_name='Venezia')

