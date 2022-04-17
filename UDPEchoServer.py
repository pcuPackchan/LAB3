

import socket

host = "127.0.0.1"
port = 11455
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serveraddress = (host,port)
sock.bind(serveraddress)

while True:
    print("\nwaiting for request... ")
    message,client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from {} port {}".format(serveraddress[0],serveraddress[1]))
    sock.sendto(message,client_address)

    try:
        n = int(message)
        if n%2 == 0:
            print("짝수입니다.")
        if n%2 == 1:
            print("홀수입니다.")
    except ValueError:
        print("숫자가 아닙니다.")


sock.close()