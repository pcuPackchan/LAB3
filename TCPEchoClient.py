import socket

server_IP = '127.0.0.1'
server_port = 13593
BUFF_SIZE = 256

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_Addr = (server_IP,server_port)

#print("connecting to {} port {}".format(server_Addr[0],server_Addr[1]))

sock.connect(server_Addr)

message = input("Enter message: ")
