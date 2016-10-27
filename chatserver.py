import socket, select
 
class Server:
    def __init__(self, port):
        self.CONNECTION_LIST = []
        self.RECV_BUFFER = 4096
        self.PORT = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("0.0.0.0", self.PORT))
        self.server_socket.listen(10)
        self.CONNECTION_LIST.append(self.server_socket)
        print "Server started on port " + str(self.PORT)

    #Function to broadcast chat messages to all connected clients
    def broadcast_data (self, sock, message):
        #Do not send the message to master socket and the client who has send us the message
        for socket in self.CONNECTION_LIST:
            if socket != self.server_socket and socket != sock :
                try :
                    socket.send(message)
                except :
                    # broken socket connection may be, chat client pressed ctrl+c for example
                    socket.close()
                    self.CONNECTION_LIST.remove(socket)
    def run(self): 
        while 1:
            # Get the list sockets which are ready to be read through select
            read_sockets,write_sockets,error_sockets = select.select(self.CONNECTION_LIST,[],[])
 
            for sock in read_sockets:
                #New connection
                if sock == self.server_socket:
                    # Handle the case in which there is a new connection recieved through server_socket
                    sockfd, addr = self.server_socket.accept()
                    self.CONNECTION_LIST.append(sockfd)
                    print "Client (%s, %s) connected" % addr
                 
                    self.broadcast_data(sockfd, "[%s:%s] entered room\n" % addr)
             
                #Some incoming message from a client
                else:
                    # Data recieved from client, process it
                    try:
                        data = sock.recv(self.RECV_BUFFER)
                        if data:
                            self.broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)  
                            print("\r" + '<' + str(sock.getpeername()) + '>' + data)         
                 
                    except:
                        self.broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                        print "Client (%s, %s) is offline" % addr
                        sock.close()
                        self.CONNECTION_LIST.remove(sock)
                        continue
        self.server_socket.close()

if __name__ == "__main__":
    server = Server(5000)
    server.start()
    server.run()