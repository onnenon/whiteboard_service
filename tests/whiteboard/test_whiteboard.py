from unittest import TestCase
from unittest.mock import patch

from whiteboard_service.whiteboard import Whiteboard


class TestWhiteboard(TestCase):
    @patch("whiteboard_service.whiteboard.pixel_factory")
    def test_001_init_should_init_whiteboard(self, pixel_factory_mock):
        row_count = 5
        pixels = [{}, {}, {}]
        use_board = False

        board = Whiteboard(row_count, use_board, pixels)

        self.assertEquals(row_count, board.row_count)
        self.assertEquals(pixel_factory_mock.call_count, 0)

    @patch("whiteboard_service.whiteboard.pixel_factory", return_value="pixels")
    def test_002_should_init_whiteboard_and_call_pixel_factory(self, pxl_factory_mock):
        row_count = 5
        use_board = False

        board = Whiteboard(row_count, use_board)

        self.assertEquals(row_count, board.row_count)
        self.assertEquals(pxl_factory_mock.call_count, 1)
        self.assertEquals(board.pixels, "pixels")
