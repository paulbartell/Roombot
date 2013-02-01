#!/usr/bin/env python

import socket
import time
import struct

class RemoteUI:

	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #start udp socket
		self.s.bind(("127.0.0.1",5000))
		self.state = [0,0,0,0,0,0,0,0]

	def refreshState(self):
		st, addr = self.s.recvfrom(8)
		self.state = list(struct.unpack('BBBBBBBB', st))

#ui = RemoteUI()
#while True:
#	ui.refreshState()
#	print ui.state