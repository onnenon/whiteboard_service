from whiteboard_service.config import LOGGER
from whiteboard_service.stubs.whiteboard_pb2 import BoardUpdateResponse
from whiteboard_service.stubs.whiteboard_pb2_grpc import WhiteBoardServiceServicer
from whiteboard_service.whiteboard import Whiteboard


class WhiteboardService(WhiteBoardServiceServicer):
    def updateBoard(self, request, context):
        for update in request.updates:
            LOGGER.info(f"set status of position: {update.position} to {update.status}")
            Whiteboard.set_status(update.position, update.status)
            response = BoardUpdateResponse()
            response.requestStatus = True
        return response
