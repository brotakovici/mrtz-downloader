import requests 
from  parameterize import parameterize
from bs4 import BeautifulSoup

song = raw_input('Baga the song :')

song = parameterize(song)

url = 'http://www.mrtzcmp3.net/' + song  + '_1s.html'

res = requests.get(url)
htmlContent = BeautifulSoup(res.content)
spanList = htmlContent.find_all('span', {'class': 'mp3Title'})
bitrateIndex = 0

for span in spanList:
    print span
    bitrate = htmlContent.find('span', {'id' : 'bitrate_' + str(bitrateIndex)})
    print bitrate
    bitrateIndex = bitrateIndex + 1
