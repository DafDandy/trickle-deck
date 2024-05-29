import board
class varList():
    col_pins = (
        board.GP14,
        board.GP13,
        board.GP12,
        board.GP11,
        board.GP10
    )
    row_pins = (
        board.GP0,
        board.GP1,
        board.GP2
    )

    coord_mapping = [
        0,  1,  2,  3,  4,  
        5,  6,  7,  8,  9,              
        10, 11, 12, 13, 14                  
    ]
