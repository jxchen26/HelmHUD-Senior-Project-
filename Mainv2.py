import tkinter as tk
from PIL import ImageTk, Image
import time
import random
from math import sin, cos, pi
from GPS_function import *
from gps_directionsv2 import *

num_list = ['1','2','3','4','5']        # string values
img = [None]   # global variable that holds turn signal image

direction, distance = gps_request() # pass back 2 values [direction, distance]


def time_update():
    time_str = time.strftime('%H:%M')
    clock.config(text = time_str)
    clock.after(500, time_update)

def speed_update():

    changing_variable = random.choice(num_list)
    speed_str = changing_variable
    speedometer.config(text = speed_str + "   MPH")
    speedometer.after(1000, speed_update)

def turn_signal_update():
    print (3)
    temp = Image.open(turn_signal_request(direction))  #call gps turn function
    img[0] = ImageTk.PhotoImage(temp)
    pic.config( image = img[0] )
    window.update_idletasks()
    window.after(3000, turn_signal_update)
    
def distance_update():
    text_distance.config(text = "turn in   " + distance )
    text_distance.after(1000, distance_update)

def direction_update():
    #direction_string = str(direction)
    text_direction.config(text = "Head southwest on E San Salvador" )
    text_direction.after(3000, direction_update)
    


# gui
window = tk.Tk()
print("start")
#window.geometry()      # width x height

#info-table
clock = tk.Label(window, font=('times', 14, 'bold'), bg ='black', fg ='yellow')
speedometer = tk.Label(window, font=('times', 30, 'bold'),bg = 'black', fg = 'light green')
text_distance = tk.Label(window, font=('times', 30, 'bold'),bg = 'black', fg = 'light green')
text_direction=tk.Label(window, font = ('times',14,'bold'), bg ='black', fg= 'light green' )
pic = tk.Label(window, bg = 'black')

#layout
time_update()
clock.pack(expand = 'yes', fill = 'both')
speed_update()
speedometer.pack(expand = 'yes', fill ='both')
pic.pack(fill = 'both')
text_distance.pack(expand ='yes', fill = 'both')
distance_update()
print ("now")
text_direction.pack(expand ='yes', fill = 'both')
direction_update()
turn_signal_update()
window.mainloop()



