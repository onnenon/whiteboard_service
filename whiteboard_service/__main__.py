from concurrent import futures

import grpc

from whiteboard_service import config
from whiteboard_service.impl.whiteboard_service import WhiteboardService
from whiteboard_service.stubs import whiteboard_pb2_grpc
from whiteboard_service.whiteboard import Whiteboard


def main():
    LOGGER = config.LOGGER

    server = grpc.server(futures.ThreadPoolExecutor())

    whiteboard = Whiteboard(config.ROW_COUNT, config.USE_BOARD)

    whiteboard_pb2_grpc.add_WhiteBoardServiceServicer_to_server(
        WhiteboardService(whiteboard), server
    )

    LOGGER.info(config.BANNER)

    try:
        server.start()
        server.wait_for_termination()
    except Exception as e:
        LOGGER.error(e.message)


def server_factory(env: str) -> grpc.Server:
    server = grpc.server(futures.ThreadPoolExecutor())

    whiteboard_pb2_grpc.add_WhiteBoardServiceServicer_to_server(
        WhiteboardService(), server
    )
    if env != "PROD":
        server.add_insecure_port(config.SERVER_SOCKET)
    else:
        credentials = config.cred_factory()
        server.add_secure_port(config.SERVER_SOCKET, credentials)

    return server


if __name__ == "__main__":
    main()
