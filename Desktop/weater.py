from pyowm import OWM
import json
import requests
api='11e295de4ad9d50b9db153edd02054e5'
owm=OWM(api)
ok = owm.weather_at_place("Palakkad")
print(ok.get_weather())
print(getattr(ok))

