#!/usr/bin/env python

import socket
import time

class UISend:

	def __init__(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #start udp socket

	def refreshState(self):
		dta = bytearray([1,1,1,0,0,0,0,0])
		print self.s.sendto(dta, ("127.0.0.1", 5000))

ui = UISend()
while True:
	ui.refreshState()
	time.sleep(1)
