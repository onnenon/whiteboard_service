from concurrent import futures

import grpc

from whiteboard_service.config import BANNER, LOGGER, SERVER_SOCKET, cred_factory
from whiteboard_service.impl.whiteboard_service import WhiteboardService
from whiteboard_service.stubs import whiteboard_pb2_grpc


def main():
    server = grpc.server(futures.ThreadPoolExecutor())

    whiteboard_pb2_grpc.add_WhiteBoardServiceServicer_to_server(
        WhiteboardService(), server
    )

    LOGGER.info(BANNER)

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
        server.add_insecure_port(SERVER_SOCKET)
    else:
        credentials = cred_factory()
        server.add_secure_port(SERVER_SOCKET, credentials)

    return server


if __name__ == "__main__":
    main()
