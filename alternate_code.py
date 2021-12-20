#Altered by lesley-byte for the people who have the "Merry Christmas here's a keyboard" kit.  Do not attempt to use this code at this time.  Incomplete.

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
print("Christmas pico keyboard")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)
# create the switch, add a pullup, start it with not being pressed
pins = [
    board.GP0, # This should look familiar. Its on the board...to make it easier to alter.
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
buttons = [0, 1, 2, 3, 4, 5, 6,
            7, 8, 9]
            
for i in range(10):
    buttons[i] = DigitalInOut(pins[i])
    buttons[i].direction = Direction.INPUT
    buttons[i].pull = Pull.UP
    
buttons_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#button = DigitalInOut(board.GP0)
#button.switch_to_input(pull=Pull.UP)


#button_state = False
# print a string on keypress
key_output1 = "Hello World!\n"
# one character on keypress
key_output2 = Keycode.A
# multiple simultaneous keypresses
key_output3 = (Keycode.SHIFT, Keycode.A)  # capital A
key_output4 = (Keycode.CONTROL, Keycode.ALT, Keycode.DELETE) # three finger salute!
# complex commands! we make a list of dictionary entries for each command
# each line has 'keys' which is either a single key, a list of keys, or a string
# then the 'delay' is in seconds, since we often need to give the computer a minute
# before doing something!
# this will open up a notepad in windows, and ducky the user

key_output5 = (
   {'keys': Keycode.GUI, 'delay': 0.1},
   {'keys': "notepad\n", 'delay': 1},  # give it a moment to launch!
   {'keys': "YOU HAVE BEEN DUCKIED!", 'delay': 0.1},
   {'keys': (Keycode.ALT, Keycode.O), 'delay': 0.1}, # open format menu
   {'keys': Keycode.F, 'delay': 0.1}, # open font submenu
   {'keys': "\t\t100\n", 'delay': 0.1}, # tab over to font size, enter 100
)

key_output = key_output1

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


while True:
    for button in range(10):
        if buttons[button].value and not buttons_state[button]:
            #print("Button pressed.")
            buttons_state[button] = True

        if not buttons[button].value and buttons_state[button]:
            print("Button released.")
            print(pins[button])
            if pins[button] == board.GP0:
                key_output = key_output1
                pass
            else:
                key_output = key_output2
                pass
            
            if isinstance(key_output, (list, tuple)) and isinstance(key_output[0], dict):
                for k in key_output:
                    make_keystrokes(k['keys'], k['delay'])
            else:
                make_keystrokes(key_output, delay=0)
                print("nothing happening")
            buttons_state[button] = False

 
