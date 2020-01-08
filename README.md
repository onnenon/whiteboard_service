```
grpcurl -v --plaintext -proto ./whiteboard_service/stubs/whiteboard.proto -d '{"updates":[{"position":1}]}' localhost:8990 Whiteboard.WhiteboardService/updateBoard
```
