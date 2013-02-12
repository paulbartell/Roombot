#cli commands
#bluez-simple-agent hci1 00:07:80:4B:F4:2B


import bluetooth
import time
import binascii

deviceId = '00:07:80:4B:F4:2B'

print "performing inquiry..."

#nearby_devices = bluetooth.discover_devices(lookup_names = True)

#print "found %d devices" % len(nearby_devices)

#for addr, name in nearby_devices:
#    if addr == deviceId:
#		print addr

port = 1

sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((deviceId, port))
#sock.settimeout(1)
#Send N command

for j in range(0,100):
	vals = []
	for i in range(0,8):
		sock.send(chr(0x80 + ord(str(i))))

	for k in range(0,8):
		for l in range(0,5)
			packet[l] = sock.recv(1)
		msb = ord(packet[1]) << 8
		lsb = ord(packet[2])
		vals.append(lsb + msb)
	print vals


