import socket # Provides networking tools for TCP communication
import time # Provides tools for recording request and response times
from datetime import datetime # Provide readable timestamps for logging

SERVER_HOST = "localhost" # The hostname of the server to connect to
SERVER_PORT = 5000 # The port number to connect to on the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
client.settimeout(20)
client.connect((SERVER_HOST, SERVER_PORT)) # Connect to the server

print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}") # Print a message indicating successful connection

message = "PROCESS DATA" # The message to send to the server

sent_at = datetime.now() # Record the time the message is sent
start_time = time.perf_counter() # Record the start time for measuring response time

client.sendall(message.encode("utf-8")) # Encode and send the message to the server
response_data = client.recv(1024) # Receive the response from the server (up to 1024 bytes)

end_time = time.perf_counter()
received_at = datetime.now()

response = response_data.decode("utf-8")
response_time = end_time - start_time

client.close()

# Print the timestamp when the message was sent
print("Sent:")
print(sent_at.strftime("%H:%M:%S.%f")[:-3])  # Format to show milliseconds
print() 

# Print the servers response
print("Response:")
print(response) 
print() 

# Print the timestamp when the response was received
print("Received:")
print(received_at.strftime("%H:%M:%S.%f")[:-3])  # Format to show milliseconds
print()

# Print the response time in seconds
print("Response Time:")
print(f"{response_time:.3f} seconds")