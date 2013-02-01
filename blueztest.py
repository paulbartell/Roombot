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
	

