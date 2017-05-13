import smbus
import time

class I2CInt:
	address = 0x04
	bus = smbus.SMBus(1)
	def writeByte(self, byte):
		self.bus.write_byte(self.address, byte)
	def readNumber(self):
		return self.bus.read_byte(self.address)


class Socket:
	port: 4242
	nbPendingCo: 5
	serverSocket: None
	clientSocket: None
	clientAddress: None

	def init(self):
		self.serverSocket = socket.socket(
		    socket.AF_INET, socket.SOCK_STREAM)
		self.serverSocket.bind((socket.gethostname(), self.port))
		self.serverSocket.listen(self.nbPendingCo)
		(self.Clientsocket, self.Address) = self.Serversocket.accept()
	def read(self):
		chunks = []
		bytes_recd = 0
		while bytes_recd < MSGLEN:
			chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
			if chunk == '':
				raise RuntimeError("socket connection broken")
			chunks.append(chunk)
			bytes_recd = bytes_recd + len(chunk)
		return ''.join(chunks)

i2c = I2CInt();

var = int(input("Enter 1 - 9: "))

i2c.writeByte(var)

print ("RPI: Hi Arduino, I sent you ", var)

time.sleep(1)

number = i2c.readNumber();
print ("Arduino: Hey RPI, I received a digit ", number)
print
