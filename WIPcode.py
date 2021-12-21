# SPDX-FileCopyrightText: 2021 John Park for Adafruit Industries
# SPDX-License-Identifier: MIT
# RaspberryPi Pico RP2040 Mechanical Keyboard

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

print("---Pico Pad Christmas 2021 Keyboard---")

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = True

keyboard = Keyboard(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
kbd_layout = KeyboardLayoutUS(keyboard)
kbd_layout = KeyboardLayoutUS(keyboard)
keyboard_layout = KeyboardLayoutUS(keyboard)

# list of pins to use (always skipping GP15 on Pico because it's funky)
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

MEDIA = 1
KEY = 2
KEYWRITE = 3


keymap = {
    (0): (KEY, (Keycode.GUI, Keycode.R)),  # This thing always starts with number 0...not number 1.  Ask dad if you need to know why.
    (1): (KEYWRITE, "Notepad"),
    (2): (KEY, [Keycode.ENTER]),
    (3): (KEY, [Keycode.FOUR]),
    (4): (KEY, [Keycode.FIVE]),
    (5): (KEY, [Keycode.A]),
    (6): (KEY, [Keycode.B]),

    (7): (MEDIA, ConsumerControlCode.VOLUME_DECREMENT),
    (8): (MEDIA, ConsumerControlCode.VOLUME_INCREMENT),
    (9): (KEYWRITE, """ If you use three quotation marks in a row, then you can keep the formating.
    Neat trick, Right?
    ^-^
    @ @
     O 
     
    Remember that punctuation in your code is important.  eeek!
    """)
    # (10): (KEY, [Keycode.UP_ARROW]),  -----I have left these things as comments/examples because the keyboard I gave you only has 10 keys----
    # (11): (KEY, [Keycode.X]),      
    # (12): (KEY, [Keycode.Y]),
    # (13): (KEY, [Keycode.Z]),

    # (14): (KEY, [Keycode.I]),
    # (15): (KEY, [Keycode.O]),
    # (16): (KEY, [Keycode.LEFT_ARROW]),
    # (17): (KEY, [Keycode.DOWN_ARROW]),
    # (18): (KEY, [Keycode.RIGHT_ARROW]),
    # (19): (KEY, [Keycode.ALT]),
    # (20): (KEY, [Keycode.U]),

}
switches = [0, 1, 2, 3, 4, 5, 6,
            7, 8, 9]

for i in range(10):
    switches[i] = DigitalInOut(pins[i])
    switches[i].direction = Direction.INPUT
    switches[i].pull = Pull.UP

switch_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


while True:
    for button in range(10):
        if switch_state[button] == 0:
            if not switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.press(*keymap[button][1])
                        print("activity one")
                    elif keymap[button][0] == KEYWRITE:
                        kbd_layout.write(keymap[button][1])
                        print("activity three")
                    else:
                        cc.send(keymap[button][1])
                        print("activity two")
                except ValueError:  # deals w six key limit
                    pass
                switch_state[button] = 1

        if switch_state[button] == 1:
            if switches[button].value:
                try:
                    if keymap[button][0] == KEY:
                        kbd.release(*keymap[button][1])

                except ValueError:
                    pass
                switch_state[button] = 0

    time.sleep(0.01)  # debounce
