import smbus
import time
import socket
import sys

MSGLEN = 1

class I2CInt:
	TIME_WAIT = 0.01
	address = 0x04
	bus = smbus.SMBus(1)
	def writeByte(self, byte):
		time.sleep(self.TIME_WAIT);
		self.bus.write_byte(self.address, int(byte))
	def readNumber(self):
		time.sleep(self.TIME_WAIT);
		return self.bus.read_byte(self.address)


class Socket:
	port = int(sys.argv[1])
	nbPendingCo = 1
	serverSocket = None
	clientSocket = None
	clientAddress = None

	def init(self):
		self.serverSocket = socket.socket(
		    socket.AF_INET, socket.SOCK_STREAM)
		self.serverSocket.bind(('', self.port))
		self.serverSocket.listen(self.nbPendingCo)
	def accept(self):
		(self.clientSocket, self.clientAddress) = self.serverSocket.accept()
	def read(self):
		chunks = bytearray()
		bytes_recd = 0
		while bytes_recd < MSGLEN:
			chunk = self.clientSocket.recv(min(MSGLEN - bytes_recd, 2048))
			if len(chunk) == 0:
				return bytearray()
			if chunk == '':
				raise RuntimeError("socket connection broken")
			chunks += chunk
			bytes_recd = bytes_recd + len(chunk)
		return chunks


comCommand = Socket();
comCommand.init();
i2c = I2CInt();
comCommand.accept();
while True:
	msg = comCommand.read();
	if len(msg) == 0:
		comCommand.accept();
	for byte in msg:
		print ("Send byte: ", int(byte))
		i2c.writeByte(byte)
