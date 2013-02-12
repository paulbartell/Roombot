#!/usr/bin/python

import pygame, sys,os
from pygame.locals import * 
import socket
import time
from bluetooth import *

class TestUI():

	def __init__(self):
		pygame.init()
		window = pygame.display.set_mode((60, 60)) 
		pygame.display.set_caption('Roombot controller') 
		screen = pygame.display.get_surface() 
		pygame.display.flip()
		self.state = [0,0,0,0,0,0,0,0]
		self.keyList = [K_UP, K_LEFT, K_RIGHT, K_PERIOD, K_SLASH, K_RETURN, K_RSHIFT, K_SPACE]
		
		uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
		service_matches = find_service( uuid = uuid, address = addr )
		
		if len(service_matches) == 0:
			print "couldn't find the SampleServer service =("
			sys.exit(0)
		
		first_match = service_matches[0]
		port = first_match["port"]
		name = first_match["name"]
		host = first_match["host"]
		
		print "connecting to \"%s\" on %s" % (name, host)
		
		# Create the client socket
		self.s=BluetoothSocket( RFCOMM )
		self.s.connect((host, port))



	def refreshState(self):
	
		for event in pygame.event.get(): 
			if event.type == QUIT: 
				print event
				sys.exit(0)
			elif event.type == KEYDOWN:
				try:
					bit = self.keyList.index(event.key)
					self.state[bit] = 1
					print "set bit on: " + str(bit)
				except ValueError:
					#Nothing happens here cause we dont care about that key
					pass
			elif event.type == KEYUP:
				try:
					bit = self.keyList.index(event.key)
					self.state[bit] = 0
					print "set bit off: " + str(bit)
				except ValueError:
					pass
					#Nothing happens here cause we dont care about that key
		self.s.send(bytearray(self.state))
		return

ui = TestUI()
while True:
	ui.refreshState()
	time.sleep(0.05) #set our loop rate// 20Hz
