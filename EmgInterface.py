import serial
import Queue

class EmgInterface():
	state = 0
	## use a queue eventually...
	def __init__(self,port,baudrate):
		self.serial = serial.Serial()
		self.serial.port = port
		self.serial.baudrate = baudrate
		self.serial.timeout = 10
		if(not self.serial.isOpen()):
			self.serial.open()

	def start(self):
		state = 1
		self.serial.flushInput()
		self.serial.write('B')


	def stop(self):
		state = 0
		self.serial.write('E')
		self.serial.flushInput()

	def close(self):
		self.serial.close()

	def readPacket(self):
		packet = self.serial.read(24)
		if(packet.count(0x00) == 4 and s.index(0x00) == 16):
			out = []
			chans = []
			for i in range(0,7):
				chan = 0b11100000 & packet[i*2]#Mask the channel number.. useful for making sure we are doing this right..
				ms = 0b11111 & packet[i*2]
				ls = packet[i*2 + 1]
				raw = (ms << 8) + ls
				fin = raw - 4096
				out.append(fin)
				chans.append(chan)

			print(chans)
			print(out)
			#for now we dont care about the rest of each packet...
		else:
			#Well crap.. lets try this again...
			self.stop()
			self.start()
	