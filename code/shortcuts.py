from kmk.keys import KC
from kmk.modules.mouse_keys import MouseKeys
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

_______ = KC.TRNS
XXXXX = KC.NO

base   = KC.FD(0)
layer1 = KC.FD(1)
layer2 = KC.FD(2)
layer3 = KC.FD(3)

#  LED Array                ROTARY1     ROTARY2     ROTARY3
#  Button1      Button2     Button3     Button4     Button5
#  Button6      Button7     Button8     Button9     Button10
#  Button11     Button12    Button13    Button14    Button15

# Rotary encoder syntax
# (Turn up, Turn Down, [optional] Encoder Button Press)

# Layer 1
layer1_rotary1  = (KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.AUDIO_MUTE)
layer1_rotary2  = (KC.LCTRL(KC.UP), KC.LCTRL(KC.DOWN), KC.LALT(KC.M))
layer1_rotary3  = (KC.F19, KC.F20, KC.F21)

layer1_button1  = KC.F14
layer1_button2  = KC.F13
layer1_button3  = KC.F16
layer1_button4  = KC.F17
layer1_button5  = KC.F18
layer1_button6  = KC.F15
layer1_button7  = KC.LGUI(KC.E)
layer1_button8  = KC.NO
layer1_button9  = KC.NO
layer1_button10 = simple_key_sequence((send_string("a1218323Ibanez_970w"), KC.MACRO_SLEEP_MS(100), KC.ENTER))
layer1_button11 = simple_key_sequence((send_string("Anubis_Osiris"), KC.MACRO_SLEEP_MS(100), KC.ENTER))
layer1_button12 = KC.LCTRL(KC.LALT(KC.T))
layer1_button13 = KC.NO
layer1_button14 = KC.NO
layer1_button15 = layer1


# Layer 2
layer2_rotary1  = (KC.NO, KC.NO, KC.NO)
layer2_rotary2  = (KC.NO, KC.NO, KC.NO)
layer2_rotary3  = (KC.NO, KC.NO, KC.NO)

layer2_button1  = KC.NO
layer2_button2  = KC.NO
layer2_button3  = KC.NO
layer2_button4  = KC.NO
layer2_button5  = KC.NO
layer2_button6  = KC.NO
layer2_button7  = KC.NO
layer2_button8  = KC.NO
layer2_button9  = KC.NO
layer2_button10 = KC.NO
layer2_button11 = KC.NO
layer2_button12 = KC.NO
layer2_button13 = KC.NO
layer2_button14 = KC.NO
layer2_button15 = layer2



# Layer 3
layer3_rotary1  = (KC.NO, KC.NO, KC.NO)
layer3_rotary2  = (KC.NO, KC.NO, KC.NO)
layer3_rotary3  = (KC.NO, KC.NO, KC.NO)

layer3_button1  = KC.NO
layer3_button2  = KC.NO
layer3_button3  = KC.NO
layer3_button4  = KC.NO
layer3_button5  = KC.NO
layer3_button6  = KC.NO
layer3_button7  = KC.NO
layer3_button8  = KC.NO
layer3_button9  = KC.NO
layer3_button10 = KC.NO
layer3_button11 = KC.NO
layer3_button12 = KC.NO
layer3_button13 = KC.NO
layer3_button14 = KC.NO
layer3_button15 = layer3



# Layer 4
layer4_rotary1  = (KC.NO, KC.NO, KC.NO)
layer4_rotary2  = (KC.NO, KC.NO, KC.NO)
layer4_rotary3  = (KC.NO, KC.NO, KC.NO)

layer4_button1  = KC.NO
layer4_button2  = KC.NO
layer4_button3  = KC.NO
layer4_button4  = KC.NO
layer4_button5  = KC.NO
layer4_button6  = KC.NO
layer4_button7  = KC.NO
layer4_button8  = KC.NO
layer4_button9  = KC.NO
layer4_button10 = KC.NO
layer4_button11 = KC.NO
layer4_button12 = KC.NO
layer4_button13 = KC.NO
layer4_button14 = KC.NO
layer4_button15 = base
