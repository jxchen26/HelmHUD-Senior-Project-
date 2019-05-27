import urllib.request
import json
from GPS_function import *

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyD8557tz2G5zgFcoPfqIp3L4rgrP47Nw3Y'
nav_request = 'origin=San+Jose+State+University&destination=2+pierce+Avenue+,+San+Jose&key=AIzaSyD8557tz2G5zgFcoPfqIp3L4rgrP47Nw3Y'
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
print(directions)

print('/n/n/n')

# below gives directions in text and in miles or feet
routes = directions['routes']
first_tree = (routes[0].keys())
   #print ('/n/n/n')
   #print (routes[0]['legs'])
legs = routes[0]['legs']

print('/n/n/n')
print('/n/n/n')
   #print (legs[0]['distance']['text'])
   #print (legs[0]['steps'])
steps = legs[0]['steps']

text_directions= steps[0]['html_instructions']
distance = steps[0]['distance']['text']

text_directions = str(text_directions).translate("</b>")

#test_obj = turn_signal(text_directions)
#test_obj.show()

print (text_directions)
print (distance)

text_directions= steps[1]['html_instructions']
distance = steps[1]['distance']['text']

text_directions = str(text_directions).translate("</b>")

#test_obj = turn_signal(text_directions)
#test_obj.show()

print (text_directions)
print (distance)

text_directions= steps[2]['html_instructions']
distance = steps[2]['distance']['text']

text_directions = str(text_directions).translate("</b>")

#test_obj = turn_signal(text_directions)
#test_obj.show()

print (text_directions)
print (distance)

text_directions= steps[3]['html_instructions']
distance = steps[3]['distance']['text']
text_directions = str(text_directions).translate("</b>")

#test_obj = turn_signal(text_directions)
#test_obj.show()


print (text_directions)
print (distance)

text_directions= steps[4]['html_instructions']
distance = steps[4]['distance']['text']

text_directions = str(text_directions).translate("</b>")

#test_obj = turn_signal(text_directions)
#test_obj.show()

print (text_directions)
print (distance)










