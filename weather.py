import sys
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

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print('Not enough arguments for weather.py')
		exit()

	url = 'http://wttr.in/%s' % (sys.argv[1])
	r = requests.get(url)
	if r.status_code != 200:  # something went wrong, just exit
		exit()
	print(parse_weather_short(r.text.encode('utf-8')))
