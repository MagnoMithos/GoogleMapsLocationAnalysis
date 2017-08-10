import json
import math
import datetime


_DATA_DIR = '../data/'
_LOCATION_FILENAME = 'location.json'
_AREAS_FILENAME = 'areasofinterest.json'
_OUTPUT_FILENAME = "out.csv"

def deg2rad(deg):
  return deg * (math.pi/180)

# Haversine formula
def getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2):
  R = 6371 # Radius of the earth in km
  dlat = deg2rad(lat2-lat1)
  dlon = deg2rad(lon2-lon1)
  a = math.sin(dlat/2) * math.sin(dlat/2) + \
  math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * \
  math.sin(dlon/2) * math.sin(dlon/2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  d = R * c # Distance in km
  return d

def loadLocationData():
  filename = _DATA_DIR + _LOCATION_FILENAME
  print 'Loading file {}'.format(filename)
  f = open(filename, 'r')
  jsoncontent = f.read()
  locations = json.loads(jsoncontent)
  print 'Loaded objects: {}'.format(len(locations['locations']))
  return locations['locations']

def loadAreasOfInterest():
  filename = _DATA_DIR + _AREAS_FILENAME
  print 'Loading file {}'.format(filename)
  f = open(filename, 'r')
  jsoncontent = f.read()
  areas = json.loads(jsoncontent)
  print 'Loaded objects: {}'.format(len(areas))
  return areas

def processLocationHistory(locations, areas):
  for location in locations:
    date = datetime.datetime.utcfromtimestamp(
        int(location['timestampMs']) / 1000
    )
    print date.strftime('%Y-%m-%d %H:%M:%S')


def main():
  print 'Welcome to file analysis'
  locations = loadLocationData()
  areas = loadAreasOfInterest()
  processLocationHistory(locations, areas)
  print 'File analysis done'



if __name__ == "__main__":
    main()


