# Dockerized Client-Server System

A containerized Python client-server application demonstrating TCP socket communication, concurrent request handling, and basic response-time measurement. Developed as a group project for CYB3023 (Large-Scale Distributed Systems).

This is an educational prototype, not a production-ready distributed system.

## Overview

The application consists of two independently containerized components:

- **TCP server:** Listens on port `5000`, accepts client connections, and handles each request in a separate Python thread. It simulates a two-second processing task before returning a response.
- **TCP client:** Connects to the server, sends `PROCESS DATA`, receives `Request Completed`, and records send/receive timestamps and elapsed response time.

The project demonstrates how networked services communicate, how concurrency affects request handling, and how Docker can package the components for consistent execution.

## Technologies

- Python 3.12
- Docker
- TCP/IP sockets (`socket`)
- Multithreading (`threading`)
- Timing and logging (`time`, `datetime`)


## Project Structure

```text
Dockerized_Client-Server-System/
├── README.md
├── client_1.log ... client_6.log
└── week3_lab/
    ├── client/
    │   ├── client.py
    │   └── Dockerfile
    └── server/
        ├── server.py
        └── Dockerfile
```

## Run Locally

**Requirements:** Docker Engine or Docker Desktop with Linux containers enabled. Run these commands from the repository root.

### 1. Build the images

```bash
docker build -t week3-server ./week3_lab/server
docker build -t week3-client ./week3_lab/client
```

### 2. Start the server

```bash
docker run --rm --name week3-server -p 5000:5000 week3-server
```

Leave this terminal running.

### 3. Run a client

In a second terminal:

```bash
docker run --rm --network host week3-client
```

**Networking note:** The client code currently connects to `localhost:5000`. The command above uses Docker host networking so the client can reach the server's published port. Host networking may need to be enabled on Docker desktop. A bridge-network setup is also compatible with this project if you change the client host to the server containers service name, then running both containers on the same Docker network.

### 4. Test concurrent requests

With the server still running, launch several clients in separate terminals:

```bash
docker run --rm --network host week3-client
```

Repeat for multiple simultaneous clients. The server starts a separate thread for each accepted connection, so the simulated processing delays can overlap rather than being strictly sequential.

## Example Output

Client output resembles:

```text
Connected to server at localhost:5000
Sent:
12:00:00.000

Response:
Request Completed

Received:
12:00:02.001

Response Time:
2.001 seconds
```

## Implementation Details

- **Transport:** TCP over IPv4, using UTF-8 encoded messages.
- **Server binding:** `0.0.0.0:5000` allows the server to accept connections on available interfaces.
- **Concurrency:** Each accepted connection is processed by a `threading.Thread`.
- **Simulated workload:** `time.sleep(2)` represents processing time; the application does not perform actual data transformation.
- **Measurement:** The client uses `time.perf_counter()` to measure elapsed time from immediately before sending the request until the response is received.
- **Timeout:** The client socket has a 20-second timeout.

## Lessons Learned

- Containerizing separate client and server components with Dockerfiles.
- Implementing a TCP request-response exchange with Python sockets.
- Handling multiple connections concurrently with threads.
- Observing the difference between processing delay and client-observed response time.

## Limitations and Potential Improvements
- Make the server hostname configurable through an environment variable to support bridge networking without editing code.
- Add robust error handling and connection cleanup on failures.
- Add structured logging, automated tests, and repeatable concurrency benchmarks.

## My Contributions

I worked on the **Python TCP client, Docker setup, and Threaded Server-Model**, including request-response communication, timestamp and latency measurement, container image configuration, networking troubleshooting, and concurrent request handling. Other server implementation and testing were completed collaboratively with my teammates.



