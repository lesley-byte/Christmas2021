# Altered by lesley-byte for the people who have the "Merry Christmas here's a keyboard" kit.  Do not attempt to use this code at this time.  Incomplete.

# ------------**import section** Probably don't change this unless you understand it. GO TO NEXT SECTION---------------
# The first part of this code imports modules that are used later.
# You will not need to change the imported modules.
import os
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# -------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------*THIS section is where you define the key presses*---------------------------------------------------------------------------
#---------------------You can change things here but you have to FOLLOW rules and KEEP the formatting.-------------------------------------------------
# type out a string on keypress:
key_output1 = "Hello World! \n"
# type one character on keypress:
key_output2 = Keycode.A
# type simple multiple simultaneous keypresses:
key_output3 = (Keycode.SHIFT, Keycode.A)  # capital A
key_output4 = (Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)  # three finger salute!
# complex commands! we make a list of dictionary entries for each command
# each line has 'keys' which is either a single key, a list of keys, or a string
# then the 'delay' is in seconds, since we often need to give the computer a minute
# before doing something!
# this will open up a notepad in windows, and ducky the user:
key_output5 = (
   {'keys': Keycode.GUI, 'delay': 0.1},
   {'keys': "notepad\n", 'delay': 1},  # give it a moment to launch!
   {'keys': "YOU HAVE BEEN DUCKIED!", 'delay': 0.1},
   {'keys': (Keycode.ALT, Keycode.O), 'delay': 0.1},  # open format menu
   {'keys': Keycode.F, 'delay': 0.1},  # open font submenu
   {'keys': "\t\t100\n", 'delay': 0.1},  # tab over to font size, enter 100
)

# -----------------** Don't touch anything below this line unless you know what you are doing **------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Christmas pico keyboard")  # This prints on the repl line.  It doesn't affect what happens when a button is pressed.
# -------led section--------  This section tells the light on the pico to stay on when the code is working ------------
led = DigitalInOut(board.LED)  # board.LED is the address of the LED on the pico, tells pico where the led is
led.direction = Direction.OUTPUT # tells the pico how to "talk" to the led 
led.value = True  # keeps the LED on.  if you don't like it then change True to False

#--------a bunch of things defined.  otherwise the pico doesn't know what it all means----------------
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems * important
keyboard = Keyboard(usb_hid.devices) # important
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)
pins = [   # This should look familiar. These are the addresses for the pins that are attached to the buttons:
    board.GP0, 
    board.GP1,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP9,
    board.GP10,
    board.GP12,
    board.GP14
]
buttons = [0, 1, 2, 3, 4, 5, 6,  # This assigns numbers to the buttons to make them easier to deal with
            7, 8, 9]            
for i in range(10):  #  This part tells the system how to read the pins
    buttons[i] = DigitalInOut(pins[i]) # Defines the pins as buttons to make it easier to deal with them
    buttons[i].direction = Direction.INPUT # tells the pico how to "talk" to the buttons
    buttons[i].pull = Pull.UP # Not every microcontroller uses Pull.UP, some use PULL.DOWN. If using this code with board that is not a pico pay attention to this.
      
buttons_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # This part gives a starting value to the buttons/pins

key_output = key_output1  # This is a starting value for key_output, it will change.
# our helper function will press the keys themselves

def make_keystrokes(keys, delay):
    if isinstance(keys, str):  # If it's a string...
        keyboard_layout.write(keys)  # ...Print the string
    elif isinstance(keys, int):  # If its a single key
        keyboard.press(keys)  # "Press"...
        keyboard.release_all()  # ..."Release"!
    elif isinstance(keys, (list, tuple)):  # If its multiple keys
        keyboard.press(*keys)  # "Press"...
        keyboard.release_all()  # ..."Release"!
    time.sleep(delay)
    
while True:  # Main loop...the stuff that does stuff...without this nothing happens at all
    for button in range(10):
        if buttons[button].value and not buttons_state[button]:  # if specific button in list of buttons is pressed *not debounced*
            # print("Button pressed.")  
            buttons_state[button] = True  # Shift value of that specific button 
        if not buttons[button].value and buttons_state[button]:  # If specific button in the list of buttons is released
            print("Button released.") # repl feedback
            print(pins[button])  # repl feedback
            if pins[button] == board.GP0:  # If GP0 is pressed then
                key_output = key_output1  # thing to be typed is in key_output1
                pass
            elif pins[button] == board.GP1:  # If GP1 is pressed then
                key_output = key_output2  # thing to be typed is in key_output2
                pass
            elif pins[button] == board.GP4:  # If GP4 is pressed then
                key_output = key_output3  # thing to be typed is in key_output3
                pass
            elif pins[button] == board.GP5:  # If GP5 is pressed then
                key_output = key_output4  # thing to be typed is in key_output4
                pass
            if isinstance(key_output, (list, tuple)) and isinstance(key_output[0], dict):  # tells it how to use make_keystrokes for complex combos
                for k in key_output:
                    make_keystrokes(k['keys'], k['delay'])
            else:
                make_keystrokes(key_output, delay=0)  # tells it how to use make_keystrokes for everything else
            buttons_state[button] = False  # shifts value of that specific button back

 
