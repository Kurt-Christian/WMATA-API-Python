import urllib2
import json

url = "http://api.wmata.com/StationPrediction.svc/json/GetPrediction/ALL?api_key=INSERT_YOUR_WMATA_API_KEY_HERE"
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)
for item in data["Trains"]:
    #print item
    print "Line: ",
    print item ['Line']
    print "Arriving at: ",
    print item ["LocationName"]
    print "Direction: ",
    print item ['DestinationName']
    print "Time til arrival: ",
    print item ["Min"]
    print "On track number: ",
    print item ["Group"]
    print ""
    print "#########################################" 
    print ""


