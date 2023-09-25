import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"Get / HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,port)) #connect to google
        s.send(request) #send request
        s.shutdown(socket.SHUT_WR) #I'm done sending!
        chunk = s.recv(BYTES_TO_READ)
        result = b'' + chunk

        while(len(chunk)>0):
            chunk = s.recv(BYTES_TO_READ)
            result +=chunk
        s.close()
        return result

print(get("127.0.0.1", 8080))