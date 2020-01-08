from whiteboard_service.config import LOGGER
from whiteboard_service.stubs.whiteboard_pb2 import BoardUpdateResponse
from whiteboard_service.stubs.whiteboard_pb2_grpc import WhiteboardServiceServicer
from whiteboard_service.whiteboard import Whiteboard


class WhiteboardService(WhiteboardServiceServicer):
    def __init__(self, whiteboard: Whiteboard):
        super().__init__()
        self.whiteboard = whiteboard

    def updateBoard(self, request, context):
        for update in request.updates:
            LOGGER.info(f"set status of position: {update.position} to {update.status}")
            self.whiteboard.set_status(update.position, update.status)
        return BoardUpdateResponse()
