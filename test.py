import urllib.request
import xml.etree.ElementTree as ET

airports = ['KINT','KGSO','KMSP','KSTP','KSGF']
flightCat = ['','','','','','']
x = 0

for n in airports:
  url = ('https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=5&mostRecentForEachStation=true&stationString=' + n)

  req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'})

  content = urllib.request.urlopen(req).read()

  root = ET.fromstring(content)

  for metar in root.iter('METAR'):
	  flightCat[x] = metar.find('flight_category').text
    

  x = x + 1

for a,b in zip(airports,flightCat):
    print(a + ' is ' + b)  