import requests
from pprint import pprint
import json

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=11e295de4ad9d50b9db153edd02054e5&units=metric'.format(city)

res = requests.get(url)

data = res.json()
temperature=data['main']['temp']
try:
	print("The weather condition in city : {} is {} \n The temperature in Celcius is {} C".format(city,data['weather'][0]['description'],temperature))
	print("Temperature in Fahreinheit = {} F ".format(temperature*1.8+32)) 
except:print("Invalid city name")