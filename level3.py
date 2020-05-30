import requests
import emoji
import json

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=****ENTER YOUR API KEY HERE****&units=metric'.format(city)

res = requests.get(url)

data = res.json()
temperature=data['main']['temp']
cond=data['weather'][0]['main']
if cond=='Clouds':
	emoj=':cloud:'
elif cond=='Clear':
	emoj=':sun_with_face:'
elif cond=='Rain':
	emoj='\U0001F327'
elif cond=='Drizzle':
	emoj=':umbrella:'
elif cond=='Thunderstorm':
	emoj='\U000026C8'
elif cond=='Snow':
	emoj='\U0001F328'
else:
	emoj=':no_entry_sign:'
try:
	print("The weather condition in city : {} is {}{} \nThe temperature in Celcius is {} C".format(city,data['weather'][0]['description'],emoji.emojize(emoj),temperature))
	print("Temperature in Fahreinheit = {} F ".format(temperature*1.8+32)) 
except:print("Invalid city name")
