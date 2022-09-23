#Format required City, Time, Temperature, Condition

from asyncore import write
import requests

openweathermap_key =''

url1 ='api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}'

def get_weather(city_name, api_key='a5dc08224e805ea90ec982239685a5f8' ):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    r = requests.get(url)
    content = r.json()
    content = content['list'] #get only the content of the file, what is passed in the list of 40 dictionaries
    with open(f'{city_name}.txt','w') as w: 
        for i in range(0, len( content)):
            x = content[i] #extract each dictionary for each time slot and store it in a variable
            orario = x['dt_txt'] #get time
            condition = x['weather'][0]['main'] 
            temperature = int(x['main']['temp']-273.15)
            w.write(f'City_name: {city_name}, Time: {orario}, Condition: {condition}, Temperature: {temperature}')
            print(f'City_name: {city_name}, Time: {orario}, Condition: {condition}, Temperature: {temperature}')
            ++i
        

get_weather(city_name='Venezia')

