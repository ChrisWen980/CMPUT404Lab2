import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1" #IP #localhost
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ) #Wait for a request, and when you get it, receive it!
            if not data:
                break
            print(data)
            conn.sendall(data)

# Start single threaded echo server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,POST)) #bind to ip and port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen() #listen for incoming connections
        conn, addr = s.accept() #accepting the client connection
        handle_connection(conn, addr) #send it a response

# Start multithreaded echo server
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2) # Allow backlog of up to 2 connections ==> queue [ waiting conn1, waiting conn2 ]
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

start_server()
#start_threaded_server()
