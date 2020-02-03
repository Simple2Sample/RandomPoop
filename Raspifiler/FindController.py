#import evdev
from evdev import InputDevice, categorize, ecodes
import os
import ControllerVariables
import AssignControllerValues
#creates object 'gamepad' to store the data
#you can call it whatever you like
while not os.path.exists('/dev/input/event0'):
    print('Waiting for connection')
    

gamepad = InputDevice('/dev/input/event0')

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    #filters by event type
   # if event.type == ecodes.EV_KEY:
    #    print(event)
    
    AssignControllerValues.assign_ValueToButtons(event)
    #print(len(ControllerVariables.code))
    print(ControllerVariables.code[1])