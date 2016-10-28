from chatserver import Server
from chatclient import Client
import unittest

class TestClientAndServer(unittest.TestCase):
	def test_client(self):
		self.assertEqual(1,1)
	def test_server(self):
		self.assertEqual(1,1)

if __name__ == "__main__":
	unittest.main()