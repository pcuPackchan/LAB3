
import socket
server_IP = "127.0.0.1"
server_port = 11455
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_addr = (server_IP,server_port)
message = input("Enter message : ")

try:
    byte_sent = sock.sendto(message.encode(),server_addr)
    data,address = sock.recvfrom(BUFF_SIZE)
    print("Recived from server: {}".format(data.decode()))
except Exception as e:
    print("Exception : {}".format(str(e)))

sock.close()