import socket
from datetime import datetime
import time

HOST = "0.0.0.0"
PORT = 5000

def handle_request(conn, addr, request_id):
    data = conn.recv(4096)
    message = data.decode('utf-8')

    start_time = datetime.now()
    print(f"Request {request_id} START")
    print(f"Client: {addr[0]}")
    print(f"Message: {message}")
    print(f"Start: {start_time.strftime('%H:%M:%S')}")
    print()

    time.sleep(2)

    response = "Request Completed"
    conn.sendall(response.encode())

    end_time = datetime.now()
    print(f"Request {request_id} END")
    print(f"End: {end_time.strftime('%H:%M:%S')}")
    print()

    conn.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print(f"Server is listening on {HOST}:{PORT}")

request_id = 0

while True:
    conn, addr = server_socket.accept()
    request_id += 1
    handle_request(conn, addr, request_id)