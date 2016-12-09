import socket
import sys

data = "Poruka"
while(data != "Exit"):
    HOST = "127.0.0.1"
    PORT = 34300
    data = input("Poruka: ")

    byte = data.encode()

    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto(byte, (HOST, PORT))#posalji poruku
    
    received = sock.recv(1024)
    print ("Primljeno: " + str(received.decode()))#ispisi sta je server vratio
