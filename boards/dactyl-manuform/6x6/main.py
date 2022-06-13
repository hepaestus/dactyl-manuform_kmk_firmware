##################################################################
author='Pete Olsen III hepaestus@gmail.com https://hepaestus.com/'
manufacturer='Olsen Design 06-2022'
version = 'Version 1.0.16.keys'
##################################################################
print("Starting...")

import board
import neopixel # Adafruit NeoPixels Lib
import adafruit_pioasm
from storage import getmount
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic
from kmk.scanners.digitalio import MatrixScanner

## Wiring/Build Specific Configuration ##########################################
#
my_rgb_pixel_pin = board.D2
my_split_data_pin = board.D3
my_col_pins=[board.A2, board.A1, board.A0, board.SCK, board.MISO, board.MOSI, board.D10]
my_row_pins=[board.D4, board.D5, board.D6, board.D7, board.D8, board.D9]
my_diode_orientation = DiodeOrientation.COL2ROW
my_split_side = SplitSide.LEFT # DEFAULT TO LEFT SIDE
neopixels_per_side = 24
debugging_on = True
#
## End Build Config #############################################################

## Figure Out Which Side I am On from the Mount Point.
name = str(getmount('/').label)
print('Keyboard Left Or Right: {}'.format(name))
if name == 'RIGHT':
     # right
     my_split_side=SplitSide.RIGHT
elif name == 'LEFT': 
     # left
     my_split_side=SplitSide.LEFT,    
else:
    print('ERROR: UNKNOWN DRIVE Cannot tell if right or left keyboard side. Default to LEFT')

### Extensions
rgb_ext = RGB(
    pixel_pin=my_rgb_pixel_pin,
    num_pixels = neopixels_per_side*2,
    val_limit = 128,
    hue_default = 126,
    sat_default = 255,
    rgb_order = (1, 0, 2),  # GRB WS2812
    val_default = 64,
    hue_step = 16,
    sat_step = 16,
    val_step =1 6,
    animation_speed = 3,
    breathe_center = 2,  # 1.0-2.7
    knight_effect_length = 4,
    # animation_mode=AnimationModes.STATIC,
    reverse_animation = False,
    refresh_rate = 60
)

## Modules
split_mod = Split(
    split_side = my_split_side,   
    split_flip = True, # If both halves are the same, but flipped, set this True
    split_type = SplitType.UART,  # Defaults to UART
    uart_interval = 20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin = my_split_data_pin,  # The primary data pin to talk to the secondary device
    # data_pin2 = split_data_pin,  # Second uart pin to allow 2 way communication
    use_pio = True,  # allows for UART to be used with PIO
)

## My Keyboard Class
class DactylManuformKeyboard6x6(_KMKKeyboard):
    # create and register the scanner
    def __init__(self):      
        # create and register the scanner
      
        # Using Global variables as any null value passed, or not setting, causes errors in digitalio.py line 17
        #                            ROW PINS     COLUMN PINS  DIODES
        self.matrix = MatrixScanner( my_row_pins, my_col_pins, my_diode_orientation )
        
    def __repr__(self):
        return (
            '\n  DactylManuformKeyboard6x6( \n'
            '    debug_enabled = {}\n'
            '    diode_orientation = {}\n'
            '    matrix = {}\n'
            '    unicode_mode = {}\n'
            '    _hid_helper = {}\n'
            '    keys_pressed = {}\n'
            '    coordkeys_pressed = {}\n'
            '    hid_pending = {}\n'
            '    active_layers = {}\n'
            '    timeouts = {}\n'
            '    split = {}\n'
            '  )\n'
        ).format(
            self.debug_enabled,
            self.diode_orientation,
            self.matrix,
            self.unicode_mode,
            self._hid_helper,            
            self.keys_pressed,
            self._coordkeys_pressed,
            self.hid_pending,
            self.active_layers,
            self._timeouts,
            my_split_side,
        )
        
keyboard = DactylManuformKeyboard6x6()
keyboard.debug_enabled = debugging_on

# NOTE: If there was not the error stated above 
#   I would use the lines below to configure the keyboard.
# keyboard.diode_orientation = my_diode_orientation
# keyboard.row_pins=my_row_pins
# keyboard.col_pins=my_col_pins

keyboard.pixel_pin = my_rgb_pixel_pin
keyboard.num_pixels = neopixels_per_side*2

keyboard.modules.append(split_mod)
keyboard.modules.append(Layers())
keyboard.extensions.append(rgb_ext)

#### KEY Definitions
XXXXXXX = KC.NO
_______ = KC.TRNS
UNDO = KC.LCTL(KC.Z)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
LSTRT = KC.LCTL(KC.HOME)
LEND = KC.LCTL(KC.END)
BACK = KC.LALT(KC.LEFT)
NEXT = KC.LALT(KC.RGHT)
LBSPC = KC.LCTL(KC.BSPC)
LOWER = KC.MO(1)
RAISE = KC.MO(2)
RGBTOG = KC.RGB_TOG # Toggle 
RGBSWL = KC.RGB_MODE_SWIRL
RGBBRH = KC.RGB_MODE_BREATHE
RGBBOW = KC.RGB_MODE_RAINBOW
RGBBBW = KC.RGB_MODE_BREATHE_RAINBOW
RGBKNT = KC.RGB_MODE_KNIGHT
RGBHUD = KC.RGB_HUD # Increase Hue
RGBHUI = KC.RGB_HUI # Decrease Hue
RGBFST = KC.RGB_ANI	# Increase animation speed
RGBSLW = KC.RGB_AND	# Decrease animation speed
RGBSAI = KC.RGB_SAI # Increase Saturation
RGBSAD = KC.RGB_SAD # Decrease Saturation
RGBVAI = KC.RGB_VAI # Increase Value
RGBVAD = KC.RGB_VAD # Decrease Value


                                                       # A truer representation of the physical layout of the 3d printed board
                                                       # The wiring makes the keymap layout possible with a 6x7(-4) on each side
keyboard.coord_mapping = [                             #   
     0, 1,  2,  3,   4,  5,    47, 46, 45, 44, 43, 42, #   0  1  2  3  4  5        47 46 45  x 43 42
     6, 7,  8,  9,  10, 11,    53, 52, 51, 50, 49, 48, #   6  7  8  9 10 11        53 52 51 50 49  x
    12, 13, 14, 15, 16, 17,    59, 58, 57, 56, 55, 54, #  12 13 14 15 16 17        59 58 57 56 55 54
    18, 19, 20, 21, 22, 23,    65, 64, 63, 62, 61, 60, #  18 19 20 21 22 23        65 64 63 62 61 60
    24, 25, 26, 27, 28, 29,    71, 70, 69, 68, 67, 66, #  24 25 26 27 28 29        71 70 69 68 67 66
            32, 33, 34, 35,    77, 76, 75, 74,         #        32 33 34 35        77 76 75 74
            38, 39, 40, 41,    83, 82, 81, 80,         #               40 41      83 82
]                                                      #                39 38    81 80

keyboard.keymap = [
    # QWERTY
    [    
        KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,       KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12,
        KC.ESC, KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,       KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINUS,
        KC.TAB, KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,        KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.EQUAL,
        KC.LSFT,KC.A,   KC.S,   KC.D,   KC.F,   KC.G,        KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,KC.QUOTE,
        KC.LCTL,KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,        KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,KC.BSLASH,
                        KC.LBRC,KC.RBRC,KC.SPC, LOWER,       RAISE,  KC.SPC, CUT,    PASTE,
                        KC.GRV, KC.ENT ,KC.BSPC,KC.DEL,      KC.DEL, KC.BSPC,KC.ENT ,KC.SPC,
    ],
    # LOWER
    [           
        _______, _______, _______, _______, _______, _______,    _______, _______, _______, _______, _______, _______,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        _______, XXXXXXX, KC.PGUP, KC.UP,   KC.PGDN, XXXXXXX,    XXXXXXX, KC.PGUP, KC.UP,   KC.PGDN, XXXXXXX, XXXXXXX,
        _______, XXXXXXX, KC.LEFT, KC.DOWN, KC.RGHT, XXXXXXX,    XXXXXXX, KC.LEFT, KC.DOWN, KC.RGHT, XXXXXXX, XXXXXXX,
                          RGBKNT,  RGBTOG,  RGBSAD,  LOWER,      RAISE,   RGBSAI,  RGBTOG,  RGBKNT, 
                          RGBSWL,  RGBBOW,  RGBBRH,  RGBBBW,     RGBBBW,  RGBBRH,  RGBBOW,  RGBSWL,
    ],    
    #RAISE
    [       
        _______, _______, _______, _______, _______, _______,   _______, _______, _______, _______, _______, _______,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,   XXXXXXX, XXXXXXX, KC.PSCR, KC.MUTE, KC.VOLU, KC.VOLD,
        _______, XXXXXXX, KC.PGUP, KC.UP,   KC.PGDN, XXXXXXX,   XXXXXXX, XXXXXXX, KC.PGUP, KC.HOME, XXXXXXX, XXXXXXX,
        _______, XXXXXXX, KC.LEFT, KC.DOWN, KC.RGHT, XXXXXXX,   XXXXXXX, XXXXXXX, KC.PGDN, XXXXXXX, XXXXXXX, XXXXXXX,
                          BACK,    NEXT,    KC.LGUI, CUT,       COPY   , PASTE,   _______, _______,
                          RGBSAD, RGBHUD,   RGBVAD,  _______,   _______, RGBVAI,  RGBHUI,  RGBSAI,
    ],
]

print("Started! Version: {}".format(version))
if __name__ == '__  main__':
    keyboard.go()
