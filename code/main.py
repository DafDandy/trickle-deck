# kmk for handwired corne keyboard
# credit given to reddit user gandi800 for providing a portion of this code
import board
import digitalio
import time
from kmk.kmk_keyboard import KMKKeyboard
from kb import varList
import shortcut as f
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.LED import LED
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()


keyboard.modules.append(MouseKeys(), EncoderHandler(), Layers())
keyboard.extensions.append(MediaKeys())


keyboard.diode_orientation = DiodeOrientation.COL2ROW


# debug feature allows user to validate keystrokes during debugging
keyboard.debug_enabled = True


keyboard.col_pins = varList.col_pins
keyboard.row_pins = varList.row_pins


# status led
def status_led1(*args, **kwargs):
    led1.value = not led1.value
    led2.value = 0
    led3.value = 0
    led4.value = 0

def status_led2(*args, **kwargs):
    led1.value = 0
    led2.value = not led2.value
    led3.value = 0
    led4.value = 0
    
def status_led3(*args, **kwargs):
    led1.value = 0
    led2.value = 0
    led3.value = not led3.value
    led4.value = 0
    
def status_led4(*args, **kwargs):
    led1.value = 0
    led2.value = 0
    led3.value = 0
    led4.value = not led4.value



encoder_handler.pins = (
    (board.GP21, board.GP20, board.GP22,), # encoder #1 
    (board.GP19, board.GP18, board.GP26,), # encoder #2
    (board.GP17, board.GP16, board.GP27,), # encoder #3
    )


encoder_handler.divisor = 2


led1 = digitalio.DigitalInOut(board.GP6)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP4)
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.GP7)
led3.direction = digitalio.Direction.OUTPUT
led4 = digitalio.DigitalInOut(board.GP5)
led4.direction = digitalio.Direction.OUTPUT


# default
led1.value = True


base.after_press_handler(status_led1)
layer1.after_press_handler(status_led2)
layer2.after_press_handler(status_led3)
layer3.after_press_handler(status_led4)


keyboard.keymap = [

    [   #layer1
        f.layer1_button1,  f.layer1_button2,  f.layer1_button3,  f.layer1_button4, f.layer1_button5,
        f.layer1_button6,  f.layer1_button7,  f.layer1_button8,  f.layer1_button9, f.layer1_button10,
        f.layer1_button11,  f.layer1_button12,  f.layer1_button13,  f.layer1_button14, f.layer1_button15
    ],
    [   #layer2
        f.layer2_button1,  f.layer2_button2,  f.layer2_button3,  f.layer2_button4, f.layer2_button5,
        f.layer2_button6,  f.layer2_button7,  f.layer2_button8,  f.layer2_button9, f.layer2_button10,
        f.layer2_button11,  f.layer2_button12,  f.layer2_button13,  f.layer2_button14, f.layer2_button15
     ],
    [   #layer3
        f.layer3_button1,  f.layer3_button2,  f.layer3_button3,  f.layer3_button4, f.layer3_button5,
        f.layer3_button6,  f.layer3_button7,  f.layer3_button8,  f.layer3_button9, f.layer3_button10,
        f.layer3_button11,  f.layer3_button12,  f.layer3_button13,  f.layer3_button14, f.layer3_button15
    ],
    [   #layer4
        f.layer4_button1,  f.layer4_button2,  f.layer4_button3,  f.layer4_button4, f.layer4_button5,
        f.layer4_button6,  f.layer4_button7,  f.layer4_button8,  f.layer4_button9, f.layer4_button10,
        f.layer4_button11,  f.layer4_button12,  f.layer4_button13,  f.layer4_button14, f.layer4_button15
     ]
]


# Rotary Encoder (1 encoder / 1 definition per layer)
encoder_handler.map = [ ((f.layer1_rotary1[0], f.layer1_rotary1[1], f.layer1_rotary1[2]),
                         (f.layer1_rotary2[0], f.layer1_rotary2[1], f.layer1_rotary2[2]),
                         (f.layer1_rotary3[0], f.layer1_rotary3[1], f.layer1_rotary3[2]),), # End Layer 1

                        ((f.layer2_rotary1[0], f.layer2_rotary1[1], f.layer2_rotary1[2]),
                         (f.layer2_rotary2[0], f.layer2_rotary2[1], f.layer2_rotary2[2]),
                         (f.layer2_rotary3[0], f.layer2_rotary3[1], f.layer2_rotary3[2]),), # End Layer 2

                        ((f.layer3_rotary1[0], f.layer3_rotary1[1], f.layer3_rotary1[2]),
                         (f.layer3_rotary2[0], f.layer3_rotary2[1], f.layer3_rotary2[2]),
                         (f.layer3_rotary3[0], f.layer3_rotary3[1], f.layer3_rotary3[2]),), # End Layer 3

                        ((f.layer4_rotary1[0], f.layer4_rotary1[1], f.layer4_rotary1[2]),
                         (f.layer4_rotary2[0], f.layer4_rotary2[1], f.layer4_rotary2[2]),
                         (f.layer4_rotary3[0], f.layer4_rotary3[1], f.layer4_rotary3[2]),), # End Layer 4
                        ]



if __name__ == '__main__':
    led2.value = 0
    led3.value = 0
    led4.value = 0
    keyboard.go()

