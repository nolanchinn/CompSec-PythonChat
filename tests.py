from chatserver import Server
from chatclient import Client
import unittest
import socket

class TestClientAndServer(unittest.TestCase):

	# Tests both the client and the server by creating a connection between the two
	def test_client(self):
		server = Server(5000)
		server.start()
		client = Client('0.0.0.0', 5000, 'nolan')
		client.connect()

	# Tests the server by starting the server and sending a message from a socket to the server
	def test_server(self):
		server = Server(5000)
		server.start()
		client = socket.create_connection(('0.0.0.0', 5000))
		client.send('Test it out')

	# Test that everything is properly initialized when the server is created
	def test_server_init(self):
		server = Server(5000)
		self.assertEqual(server.RECV_BUFFER, 4096)
		self.assertEqual(server.PORT, 5000)

	# Test that everything is properly initalized when the client is created
	def test_client_init(self):
		client = Client('0.0.0.0', 5000, 'nolan')
		self.assertEqual(client.serverIP, '0.0.0.0')
		self.assertEqual(client.serverPort, 5000)
		self.assertEqual(client.name, 'nolan')

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestClientAndServer)
	unittest.TextTestRunner(verbosity=1).run(suite)