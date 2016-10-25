import socket, select, string, sys

class Client: 

	def __init__(self, ip, port, name):
		self.serverIP = ip
		self.serverPort = port
		self.name = name
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.sock.connect((self.serverIP, self.serverPort))
		print 'Connected to the server.'

	def sendRecvMsg(self, read_sockets):
		for rSock in read_sockets:
			if rSock == self.sock:
				data, addr = rSock.recvfrom(4096)
				if not data:
					print '\nDisconnected from the server.'
					sys.exit()
				else:
					sys.stdout.write(data)
			else:
				msg = sys.stdin.readline()
				self.sock.send(msg)

	def run(self):
		while(1):
			socket_list = [sys.stdin, self.sock]
			read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
			self.sendRecvMsg(read_sockets)
		self.sock.close()

if __name__ == "__main__":
	client = Client('0.0.0.0', 5000, 'nolan')
	client.connect()
	client.run()

	


