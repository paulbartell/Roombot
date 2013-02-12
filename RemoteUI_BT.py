#!/usr/bin/env python

import socket
import time
import struct
from bluetooth import *


class RemoteUI_BT:

	def __init__(self):
		server_sock=BluetoothSocket( RFCOMM )
		server_sock.bind(("",PORT_ANY))
		server_sock.listen(1)

		port = server_sock.getsockname()[1]

		uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

		advertise_service( server_sock, "SampleServer",
							service_id = uuid,
		                   	service_classes = [ uuid, SERIAL_PORT_CLASS ],
 		                 	profiles = [ SERIAL_PORT_PROFILE ], 
#  		                 	protocols = [ OBEX_UUID ] 
    		                )
                   
		print "Waiting for connection on RFCOMM channel %d" % port

		self.s, client_info = server_sock.accept()
		print "Accepted connection from ", client_info
		
		self.state = [0,0,0,0,0,0,0,0]

	def refreshState(self):
		st = self.s.recv(8)
		self.state = list(struct.unpack('BBBBBBBB', st))

#ui = RemoteUI()
#while True:
#	ui.refreshState()
#	print ui.state