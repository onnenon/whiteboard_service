from dataclasses import dataclass
from unittest import TestCase
from unittest.mock import MagicMock, patch

from whiteboard_service.impl.whiteboard_service import WhiteboardService
from whiteboard_service.whiteboard import Whiteboard


@dataclass
class Update:
    position: int
    status: int


class ServiceTests(TestCase):
    @patch.object(Whiteboard, "set_status")
    def test_updateBoard(self, set_status_mock):
        service = WhiteboardService()
        request = MagicMock()
        request.updates = [
            Update(1, 4),
            Update(5, 3),
        ]

        service.updateBoard(request, None)

        self.assertEquals(set_status_mock.call_count, 2)
