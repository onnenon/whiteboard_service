import logging
import os
import sys

import grpc


def logFactory(log_level: str) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
    handler.setLevel(log_level)

    logger.addHandler(handler)
    return logger


def cred_factory() -> grpc.ServerCredentials:
    with open(CERT_FILE, "rb") as f:
        private_key = f.read()
    with open(KEY_FILE, "rb") as f:
        cert = f.read()
    return grpc.ssl_server_credentials((private_key, cert))


CERT_FILE: str = os.getenv("CERT_FILE", "whiteboard.crt")
KEY_FILE: str = os.getenv("KEY_FILE", "whiteboard.key")

LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
LOGGER: logging.Logger = logFactory(LOG_LEVEL)

SERVER_PORT: str = os.getenv("SERVER_PORT", "8990")
SERVER_HOST: str = os.getenv("SERVER_HOST", "localhost")
SERVER_SOCKET: str = f"{SERVER_HOST}:{SERVER_PORT}"

ROW_COUNT: int = os.getenv("ROW_COUNT", 20)
USE_BOARD: bool = True if os.getenv("USE_BOARD") is not None else False

BANNER: str = f"""

*************************************************

  Start Gatekeeper GRPC Server @ {SERVER_SOCKET}

*************************************************
"""
