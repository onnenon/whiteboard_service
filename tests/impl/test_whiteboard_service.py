from dataclasses import dataclass
from unittest import TestCase
from unittest.mock import MagicMock

from whiteboard_service.impl.whiteboard_service import WhiteboardService


@dataclass
class Update:
    position: int
    status: int


class ServiceTests(TestCase):
    def test_updateBoard(self):
        whiteboard_mock = MagicMock()
        service = WhiteboardService(whiteboard_mock)
        request = MagicMock()
        request.updates = [
            Update(1, 4),
            Update(5, 3),
        ]

        service.updateBoard(request, None)

        self.assertEquals(whiteboard_mock.set_status.call_count, 2)
