import socket

h = '127.0.0.1'
p = 13593
bsize = 256
BL = 5

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((h,p))

s.listen(BL)

while True:
    print("waiting for request...")
    d_sock,addr = s.accept()
    print("request from {} port {}".format(addr[0],addr[1]))
    message = d_sock.recv(bsize)
    print(message.decode())
    if message:

        server_respone = "HTTP/1.0 200 OK\r\n" \
                         "Content-Type:text/html\r\n\r\n" \
                         "<HTML><BODY" \
                         "<H1>Hello World! 1689019</H1>" \
                         "</BODY></HTML>"
        d_sock.sendall(server_respone.encode())
        print("\n")
    else:
        d_sock.sendall()
        print("no")
    d_sock.close()