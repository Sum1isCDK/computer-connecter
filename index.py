import socket
sock = socket.create_server((socket.gethostname(), 10))
print(sock)
