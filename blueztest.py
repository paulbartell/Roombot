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
sock.send(chr(int('11101110',2)))
sock.recv(18)

# Sending B command would be ideal
sock.send(chr(int('01000010',2)))
sock.recv(24)
# receive 24 bytes.. loop every 10mS or so... or wait till start


