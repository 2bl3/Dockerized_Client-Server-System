import socket # Provides networking tools for TCP communication
import time # Provides tools for recording request/response times

SERVER_HOST = "week3-server" # The hostname of the server to connect to
SERVER_PORT = 5000 # The port number to connect to on the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket