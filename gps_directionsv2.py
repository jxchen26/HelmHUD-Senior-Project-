import urllib.request
import json
#from custom_library import *


def gps_request():
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    api_key = 'AIzaSyAVtFtehPuqDGnK5NEWbQJLaqcFcOaRcvE'
    nav_request = 'origin=San+Jose+State+University&destination=2+pierce+Avenue+,+San+Jose&key='+api_key
    request = endpoint + nav_request
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    #print(directions)

    #print('/n/n/n')

    #below gives directions in text and in miles or feet
    routes = directions['routes']
    first_tree = (routes[0].keys())
    legs = routes[0]['legs']
    steps = legs[0]['steps']

    text_directions= steps[0]['html_instructions']
    distance = steps[0]['distance']['text']

    text_directions = str(text_directions).translate("</b>")

    #test_obj = turn_signal(text_directions)
    #test_obj.show()

    print (text_directions)
    print (distance)

  #  text_directions= steps[1]['html_instructions']
  #  distance = steps[1]['distance']['text']

  #  text_directions = str(text_directions).translate("</b>")

    #test_obj = turn_signal(text_directions)
    #test_obj.show()

   # print (text_directions)
   # print (distance)

#    text_directions= steps[2]['html_instructions']
 #   distance = steps[2]['distance']['text']

#    text_directions = str(text_directions).translate("</b>")

    #test_obj = turn_signal(text_directions)
    #test_obj.show()

#    print (text_directions)
#    print (distance)

 #   text_directions= steps[3]['html_instructions']
 #   distance = steps[3]['distance']['text']
 #   text_directions = str(text_directions).translate("</b>")

    #test_obj = turn_signal(text_directions)
    #test_obj.show()


# print (text_directions)
  #  print (distance)

  #  text_directions= steps[4]['html_instructions']
  #  distance = steps[4]['distance']['text']

  #  text_directions = str(text_directions).translate("</b>")

    #test_obj = turn_signal(text_directions)
    #test_obj.show()

  #  print (text_directions)
  #  print (distance)

    return text_directions, distance








