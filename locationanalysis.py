import json

print 'test'

f = open('location.json', 'r')
jsoncontent = f.read()
print jsoncontent

location = json.loads(jsoncontent)
print len(location)
