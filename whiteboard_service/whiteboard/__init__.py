from enum import Enum


def pixel_factory(row_count: int, use_board: bool):
    if use_board:
        import board
        import neopixel

        return neopixel.NeoPixel(board.D12, row_count)
    else:
        return [{}] * row_count


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
    def __init__(self, row_count: int, use_board: bool, pixels=None):
        self.row_count = row_count
        if pixels:
            self.pixels = pixels
        else:
            self.pixels = pixel_factory(row_count, use_board)

    def _translate_position(self, index: int):
        num_leds = self.row_count
        if index < num_leds / 2:
            return num_leds - (1 + index)
        else:
            return index - (num_leds // 2)

    def set_status(self, position: int, status: int):
        """
        Change LED of given position to new value
        """
        if position >= self.row_count:
            raise WhiteboardError(
                "position {} exceeds row count {}".format(position, self.row_count)
            )
        led_position = Whiteboard._translate_position(self, position)
        if status == WhiteboardStatusEnum.OUT.value:
            self.pixels[led_position] = _colors["yellow"]
        elif status == WhiteboardStatusEnum.IN.value:
            self.pixels[led_position] = _colors["green"]
        else:
            self.pixels[led_position] = _colors["off"]

    def toggle_status(self, status: WhiteboardStatusEnum):
        for i in range(self.row_count):
            self.set_status(i, status)
