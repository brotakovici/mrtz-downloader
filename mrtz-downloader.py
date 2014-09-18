import requests
from  parameterize import parameterize

song = raw_input('Baga the song :')

song = parameterize(song)

url = 'http://www.mrtzcmp3.net/' + song  + '_1s.html'

res = requests.get(url)

print res.text
