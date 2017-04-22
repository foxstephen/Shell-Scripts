try:
	import requests
except:
	exit()

def parse_weather_short(weather):
	lines = weather.split('\n')
	parsed = ''
	for _ in range(0, 7):
		parsed += (lines[_] + '\n')
	return parsed

r = requests.get('http://wttr.in/Dublin')
print(r.text)
print(parse_weather_short(r.text))
