import serial

class EmgInterface():
	def __init__(self,port,baud):
		self.ser = serial(port,baud)

	def start(self):
	
		# while self.sock == None:
# 			nearby_devices = bluetooth.discover_devices(lookup_names = True)
# 			for addr, name in nearby_devices:
#   		  		if addr == deviceId:
#    		 			self.sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#    		 			sock.connect((self.deviceId, self.port))
#    		 # send start command... how do we do this correctly.. ask them

	def stop(self):
		state = 0
		self.serial.write('E')
		self.serial.flushInput()

	def close(self):
		self.serial.close()

	def readPacket(self, packet):
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
	