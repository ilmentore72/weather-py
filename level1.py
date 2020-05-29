import requests
from pprint import pprint
import json

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=11e295de4ad9d50b9db153edd02054e5&units=metric'.format(city)

res = requests.get(url)

data = res.json()
try:
	print("The weather condition in city : {} is {} \n The average temperature is {}".format(city,data['weather'][0]['description'],data['main']['temp']))
except:print("Invalid city name")
