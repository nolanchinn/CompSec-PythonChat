import socket, select, string, sys
serverIP = '0.0.0.0'
serverPort = 5000
name = 'generic guy'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((serverIP, serverPort))
print 'Connected to server. Start sending messages.'
while(1):
	"""inputReady, outputReady, exceptReady = select.select([sys.stdin, sock],[], [])
	for inputs in inputReady:
		message, address = inputs.recvfrom(4096)
		print message
		if(sys.stdin):
			rawData = sys.stdin.readline()
			if(rawData.startswith('exit')):
				print '~~~EXITING~~~'
				sys.exit()
			else: 
				sock.send(rawData)"""
	socket_list = [sys.stdin, sock]
	read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

	for rSock in read_sockets:
		if rSock == sock:
			data, address = rSock.recvfrom(4096)
			if not data :
				print '\nDisconnected'
				sys.exit()
			else:
				sys.stdout.write(data)
		else :
			msg = sys.stdin.readline()
			sock.send(name + ': ' + msg)
sock.close()

	


