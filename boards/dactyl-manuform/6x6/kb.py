import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (board.A2, board.A1, board.A0, board.SCK, board.MISO, board.MOSI, board.D10)
    row_pins = (board.D3, board.D4, board.D5, board.D6,  board.D7,   board.D8,   board.D9)
    diode_orientation = DiodeOrientation.COL2ROW
    
coord_mapping = [
     0,  1,  2,  3,  4,  5,            38, 39, 40, 41, 42, 43,
     6,  7,  8,  9, 10, 11,            44, 45, 46, 47, 48, 49,
    12, 13, 14, 15, 16, 17,            50, 51, 52, 53, 54, 55,
    18, 19, 20, 21, 22, 23,            56, 57, 58, 59, 60, 61,
    24, 25, 26, 27, 28, 29,            62, 63, 64, 65, 66, 67,
            30, 31, 32, 33,            68, 69, 70, 71,
                34, 35, 36, 37,    72, 73, 74, 75,                      
]

from kmk.extensions.RGB import RGB
from kb import rgb_pixel_pin # This can be imported or defined manually
rgb_pixel_pin = board.D2 # DEFINED BY Pete

rgb_ext = RGB(
    pixel_pin=rgb_pixel_pin,
    num_pixels=48
    val_limit=100,
    hue_default=0,
    sat_default=100,
    rgb_order=(1, 0, 2),  # GRB WS2812
    val_default=100,
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
_KMKKeyboard.extensions.append(rgb_ext)