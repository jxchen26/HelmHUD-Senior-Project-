import urllib
import json
from PIL import ImageTk, Image

def turn_signal_request(api_directions):
    print (api_directions)
    if "Head" or "Continue" in api_directions:
        picture = "straight.png"

    elif "Turn right"in api_directions:
        picture = "Right turn(green).png"

    elif "Turn left" in api_directions:
        picture = "Left turn(green).png"

    elif "Keep left" in api_directions:
        picture = "Keep Left.png"

    elif "Keep right" in api_directions:
        picture = "Keep right.png"

    elif "Merge" in api_directions:
        picture = "merge.png"
        
    elif "U" in api_directions:
        picture = "u turn.png"


    return picture