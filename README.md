# Whiteboard-Microservice

A gRPC service for remotely updating a Neopixel at a given position to the color of a given status enum.

## Dependencies

- Python3-devel or Python3-dev
- Python3 >= 3.6
- GCC

## Getting Started

### Setting up the Pi Backend

Create a python virtual environment with `python3 -m venv venv`

Activate the virtual environment `source ${VENV_DIR}/bin/activate`

Install poetry with pip `pip install poetry`

Install all dependencies with poetry `poetry install`

Run the gRPC backend with `make run`

## Contributing

Github users in the "All Teammates" team have Write access to this repository. The `master` branch is protected, and requires a PR with at least one approving review to merge.

Troubleshooting grpc in the command line can be done with the grpcurl utility.

An example to run the updateBoard function is:

```
grpcurl -v --plaintext -proto ./whiteboard_service/stubs/whiteboard.proto -d '{"updates":[{"position":1, "status": 2}]}' localhost:8990 Whiteboard.WhiteboardService/updateBoard
```
