import SocketServer

class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        prijem = data.decode("utf-8")
        print (prijem)
        socket.sendto(prijem.encode(), self.client_address) 
        """if(prijem == "ZDRAVO"):
            slanje = "IP,192.168.1.5"
            print (slanje)
            socket.sendto(slanje.encode(), self.client_address) 
        elif(prijem == "UPIT"):
            slanje = "21.5,50.50,60,1,1,1,1,10,50"
            print (slanje)
            socket.sendto(slanje.encode(), self.client_address) """
            
if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 34300
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()


input()
