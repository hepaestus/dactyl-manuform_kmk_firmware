print("Starting...")
import board
import neopixel 

from kb import _KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.extensions.RGB import RGB, AnimationModes                            

keyboard = _KMKKeyboard()

keyboard.debug_enabled = True

rgb_pixel_pin = board.D2
split_data_pin = board.D3

layers_ext = Layers()

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=split_data_pin,  # The primary data pin to talk to the secondary device
    # data_pin2=board.TX,  # Second uart pin to allow 2 way communication
    use_pio=True,  # allows for UART to be used with PIO
)

rgb_ext = RGB(
    pixel_pin=rgb_pixel_pin,
    num_pixels=24,
    val_limit=100,
    hue_default=0,
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
    refresh_rate=60,
)
keyboard.extensions.append(rgb_ext)
keyboard.modules = [layers_ext, split]

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
    [ # QWERTY
      # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,                                            KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINS,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,                                             KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.PIPE,
        KC.LSFT,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,                                             KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LCTL,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,                                             KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.BSLASH,
                            KC.LCBR,  KC.RCBR,  KC.LCTL,  KC.ENT,                                           KC.SPC,   KC.RCTL,  KC.RGUI,  KC.EQL,
                                      LOWER,    KC.SPC,   KC.TAB,   KC.BSPC,                       KC.ENT,  KC.END,   KC.DEL,   KC.HOME,
    ],
    [ # LOWER
      # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.F1,     KC.F2,    KC.F3,   KC.F4,   KC.F5,   KC.F6,                                            KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,
        KC.ESC,    KC.N1,    KC.N2,   KC.N3,   KC.N4,   KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINS,
        KC.GRV,    KC.EXLM,  KC.AT,   KC.HASH, KC.DLR,  KC.PERC,                                          KC.CIRC,  KC.AMPR,  KC.ASTR,  KC.LPRN,  KC.RPRN,  KC.PIPE,
        KC.RGB_TOG,KC.EQL,   KC.MINS, KC.PLUS, KC.LCBR, KC.RCBR,                                          KC.LBRC,  KC.RBRC,  KC.SCLN,  KC.COLN,  KC.BSLS,  XXXXXXX,
                             XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                                      KC.TAB,  KC.BSPC,   KC.END,   KC.DEL,                        KC.ENT,KC.END,   KC.DEL,   KC.HOME,
    ],
    [ #RAISE
      # HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----#ENCODER--#ENCODER--# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,                                            KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,                                            KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINS,
        XXXXXXX,  KC.INS,   KC.PSCR,  KC.APP,   XXXXXXX,  XXXXXXX,                                          KC.PGUP,  BACK,     KC.UP,    NEXT,     LBSPC,    KC.BSPC,
        XXXXXXX,  KC.LALT,  KC.LCTL,  KC.LSFT,  XXXXXXX,  KC.CAPS,                                          KC.PGDN,  KC.LEFT,  KC.DOWN,  KC.RGHT,  KC.DEL,   KC.PIPE,
        XXXXXXX,  UNDO,     CUT,      COPY,     PASTE,    XXXXXXX,                                          XXXXXXX,  LSTRT,    XXXXXXX,  LEND,     XXXXXXX,  XXXXXXX,
                            XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,                                          XXXXXXX,  XXXXXXX,  XXXXXXX,  XXXXXXX,
                                    KC.TAB,KC.BSPC,   KC.ENT,   KC.SPC,                             KC.ENT, KC.END,   KC.DEL,   KC.BSPC,
    ]
]

print("Started!")

if __name__ == '__main__':
    keyboard.go()
