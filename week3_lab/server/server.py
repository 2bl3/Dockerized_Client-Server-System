import socket
from datetime import datetime
import time

HOST = "0.0.0.0"
PORT = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")


request_id = 0

conn, addr = server_socket.accept()

request_id += 1
handle_request(conn, addr, request_id)

def handle_request (conn, addr, request_id):
    data = conn.recv(4096)
    message = data.decode('utf-8')

    