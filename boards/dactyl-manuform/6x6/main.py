##################################################################
author='Pete Olsen III hepaestus@gmail.com https://hepaestus.com/'
manufacturer='Olsen Design 06-2022'
version = 'Version 1.0.8d'
##################################################################
print("Starting...")

import board
import neopixel # Adafruit NeoPixels Lib
import adafruit_pioasm

# from kb import _KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard

## Import Scanners
from kmk.scanners import DiodeOrientation
from kmk.scanners import intify_coordinate as ic
from kmk.scanners.digitalio import MatrixScanner

## Wiring/Build Specific Configuration
rgb_pixel_pin = board.D2
split_data_pin = board.D3
my_col_pins=[board.A2, board.A1, board.A0, board.SCK, board.MISO, board.MOSI, board.D10]
my_row_pins=[board.D4, board.D5, board.D6, board.D7, board.D8, board.D9]
my_diode_orientation=DiodeOrientation.COL2ROW
neopixels_per_side = 24
debug=True
## End Build Config

rgb_ext = RGB(
    pixel_pin=rgb_pixel_pin,
    num_pixels=neopixels_per_side,
    val_limit=100,
    hue_default=100,
    sat_default=100,
    rgb_order=(1, 0, 2),  # GRB WS2812
    val_default=50,
    hue_step=5,
    sat_step=5,
    val_step=5,
    animation_speed=1,
    breathe_center=1,  # 1.0-2.7
    knight_effect_length=3,
    animation_mode=AnimationModes.STATIC,
    reverse_animation=False,
    refresh_rate=60
)

split_mod = Split(
    split_flip=True, # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=split_data_pin,  # The primary data pin to talk to the secondary device
    #data_pin2=split_data_pin,  # Second uart pin to allow 2 way communication
    use_pio=True,  # allows for UART to be used with PIO
)

class DactylManuformKeyboard6x6(_KMKKeyboard):
    # create and register the scanner
    def __init__(self):      
      # create and register the scanner      
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
            '  )\n'
        ).format(
            self.debug_enabled,
            self.diode_orientation,
            self.matrix,
            self.unicode_mode,
            self._hid_helper,
            # internal state
            self.keys_pressed,
            self._coordkeys_pressed,
            self.hid_pending,
            self.active_layers,
            self._timeouts,
        )
        
keyboard = DactylManuformKeyboard6x6()
keyboard.debug_enabled = debug
# keyboard.diode_orientation = my_diode_orientation
# keyboard.col_pins=my_col_pins
# keyboard.row_pins=my_row_pins
keyboard.modules.append(split_mod)
keyboard.modules.append(Layers())
keyboard.extensions.append(rgb_ext)

keyboard.coord_mapping = [
    0,  1,  2,  3,  4,  5,          47, 46, 45, 44, 43, 42,
    6,  7,  8,  9, 10, 11,          53, 52, 51, 50, 49, 48,
    12, 13, 14, 15, 16, 17,         59, 58, 57, 56, 55, 54,
    18, 19, 20, 21, 22, 23,         65, 64, 63, 62, 61, 60,
    24, 25, 26, 27, 28, 29,         71, 70, 69, 68, 67, 66,
            30, 31, 32, 33,         75, 74, 73, 72,
                34, 35, 36, 37, 79, 78, 77, 76,
]                                          

# Cleaner key names
XXXXXXX = KC.NO
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

keyboard.keymap = [
    # QWERTY
    [    
        KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,      KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12,
        KC.ESC, KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,      KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINS,
        KC.TAB, KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,       KC.Y,   KC.U,   KC.I,   KC.O,   KC.P,   KC.EQL,
        KC.LSHIFT,KC.A, KC.S,   KC.D,   KC.F,   KC.G,       KC.H,   KC.J,   KC.K,   KC.L,   KC.SCLN,KC.QUOT,
        KC.LCTL,KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,       KC.N,   KC.M,   KC.COMM,KC.DOT, KC.SLSH,KC.BSLASH,
                KC.LCBR,    KC.RCBR,    RAISE,  KC.ENT,     KC.SPC, LOWER,  KC.RGUI,    KC.RSHIFT,
                    LOWER,  KC.SPC,     KC.TAB, KC.BSPC,    KC.DEL, KC.END, KC.DEL, KC.HOME,
    ],
    # LOWER
    [       
        KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,          KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12,
        KC.ESC, KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,          KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINS,
        KC.GRV, KC.EXLM,    KC.AT,  KC.HASH,    KC.DLR,         KC.PERC,    KC.CIRC,  KC.AMPR,  KC.ASTR,KC.LPRN,    KC.RPRN,    KC.PIPE,
        KC.RGB_TOG,KC.EQL,  KC.MINS,KC.PLUS,    KC.LCBR,        KC.RCBR,    KC.LBRC,  KC.RBRC,  KC.SCLN,KC.COLN,    KC.BSLS,    XXXXXXX,
                XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,     XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                    KC.TAB,  KC.BSPC,   KC.END,  KC.DEL,    KC.ENT, KC.END, KC.DEL, KC.HOME,
    ],
    #RAISE
    [       
        KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,        KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,        KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINS,
        XXXXXXX,  KC.INS,   KC.PSCR,  KC.APP,   XXXXXXX,  XXXXXXX,      KC.PGUP,  BACK,     KC.UP,    NEXT,     LBSPC,    KC.BSPC,
        XXXXXXX,  KC.LALT,  KC.LCTL,  KC.LSFT,  XXXXXXX,  KC.CAPS,      KC.PGDN,  KC.LEFT,  KC.DOWN,  KC.RGHT,  KC.DEL,   KC.PIPE,
        XXXXXXX,  UNDO,     CUT,      COPY,     PASTE,    XXXXXXX,      XXXXXXX,  LSTRT,    XXXXXXX,  LEND,     XXXXXXX,  XXXXXXX,
                XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                    KC.TAB,   KC.BSPC,  KC.ENT,  KC.SPC,    KC.ENT,    KC.END,   KC.DEL,   KC.BSPC,
    ]
]

print("Started! Version: {}".format(version))
if __name__ == '__main__':    
    keyboard.go()