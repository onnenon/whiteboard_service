from enum import Enum
from whiteboard_service import config

_pixels = [{}] * config.ROW_COUNT

_leds = []

if config.USE_BOARD is not None:
    import board
    import neopixel

    _pixels = neopixel.NeoPixel(board.D12, config.ROW_COUNT)

_colors = {
    "red": (35, 0, 0),
    "green": (0, 35, 0),
    "blue": (0, 0, 35),
    "off": (0, 0, 0),
    "yellow": (45, 25, 0),
}


class WhiteboardError(Exception):
    pass


class WhiteboardStatusEnum(Enum):
    OUT = 0
    IN = 1
    STATA = 2
    STATB = 3
    STATC = 4


class Whiteboard:
    @staticmethod
    def _translate_position(index: int):
        num_leds = len(_pixels)
        if index < num_leds / 2:
            return num_leds - (1 + index)
        else:
            return index - (num_leds // 2)

    @staticmethod
    def set_status(position: int, status: int):
        """
        Change LED of given position to new value
        """
        if position >= len(_pixels):
            raise WhiteboardError(
                "position {} exceeds row count {}".format(position, len(_pixels))
            )
        led_position = Whiteboard._translate_position(position)
        if status == WhiteboardStatusEnum.OUT.value:
            _pixels[led_position] = _colors["yellow"]
        elif status == WhiteboardStatusEnum.IN.value:
            _pixels[led_position] = _colors["green"]
        else:
            _pixels[led_position] = _colors["off"]

    @staticmethod
    def toggle_status(status: WhiteboardStatusEnum):
        for i in range(len(_pixels)):
            Whiteboard.set_status(i, status)
