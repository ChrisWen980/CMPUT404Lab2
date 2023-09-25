#This is part 1 of lab

import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"Get / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #opened up a socket here #socket.af_inet => use IPv4
    s.connect((host,port)) #connect to google
    s.send(request) #send request
    s.shutdown(socket.SHUT_WR) #I'm done sending!
    result = s.recv(BYTES_TO_READ) #keep reading incoming data
    while(len(result)>0):
        print(result)
        result = s.recv(BYTES_TO_READ)

    s.close()

get("www.google.com", 80)
#get("localhost", 8080)