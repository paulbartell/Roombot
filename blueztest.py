#cli commands
#bluez-simple-agent hci1 00:07:80:4B:F4:2B


import bluetooth

deviceId = '00:07:80:4B:F4:2B'

print "performing inquiry..."

nearby_devices = bluetooth.discover_devices(lookup_names = True)

print "found %d devices" % len(nearby_devices)

for addr, name in nearby_devices:
    if addr == deviceId:
		print addr

port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((deviceId, port))


#Send N command
sock.send(chr(int(0x80 + ord('M'))))
sock.send(chr(int(0x30)))
sock.send(chr(int(0x80 + ord('M')+ 0x30)))
#sock.recv(1)

# Sending B command would be ideal
sock.send(chr(int(0x80 + ord('B'))))
#sock.recv(24)
# receive 24 bytes.. loop every 10mS or so... or wait till start
for i in range(0,10000):
	print(ord(sock.recv(1)))
packets = []

#While True:
#	packets.append(sock.recv(1)) #append bytes received to our buffer
#	if len(packets) == 18:
#		#proces packets here

