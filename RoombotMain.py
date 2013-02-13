#!/usr/bin/env python

from RoombaSCI import RoombaAPI
from stormLauncher import launchControl
from EmgInterface import EmgInterface
import time
#from TestUI import TestUI
from RemoteUI_BT import RemoteUI_BT
from copy import deepcopy
from serial import Serial

#ROOMBA_PORT="/dev/ttyAMA0"
ROOMBA_PORT = "/dev/tty.usbserial-A2001n69"
ROOMBA_BAUD="115200"

HAPTICS_PORT="/dev/tty.RN42-755F-SPP"
HAPTICS_BAUD="115200"



#EMG_PORT="/dev/rfcomm1"
#EMG_BAUD="115200"

launcher = launchControl()
roomba = RoombaAPI(ROOMBA_PORT, ROOMBA_BAUD)

haptics = Serial(HAPTICS_PORT, HAPTICS_BAUD)

#emg = EmgInterface(EMG_PORT, EMG_BAUD);
#emg = EmgInterface("/dev/tty.M13762-BluetoothSerialP",115200)

ui = RemoteUI()

#State variable [forward,left,right,vacuum on,vacuum off,m-up,m-down,m-fire]


roomba.connect()
#roomba.safe() #set safe control mode ///Use other mode
roomba.full()

def processState(state,oldstate):
	if state[0:3] == [0,0,0]: #roomba stop condition
		roomba.stop()
		print "stop"
	if state[0] == 1 and oldstate[0] == 0: #Go forward
		roomba.forward()
		print "forward"
	if state[1] == 1 and oldstate[1] == 0: #Go left
		roomba.left()
	if state[2] == 1 and oldstate[2] == 0: #Go Right
		roomba.right()
	if state[3] == 1 and oldstate[3] == 0: #Vacuum on
		roomba.motors(0b00000111)
	if state[3] == 0 and oldstate[3] == 1: #Vacuum on -stop
		pass
	if state[4] == 1 and oldstate[4] == 0: #Vacuum off
		roomba.motors(0b00000000)
	if state[4] == 0 and oldstate[4] == 1: #vacuum off - stop
		pass
	if state[5] == 1 and oldstate[5] == 0: # turret up
		launcher.turretUp()
		print "up"
	if state[5] == 0 and oldstate[5] == 1: # turret up stop
		launcher.turretStop()
	if state[6] == 1 and oldstate[6] == 0: # turret down
		launcher.turretDown()
		print "down"
	if state[6] == 0 and oldstate[6] == 1: # turret down stop
		launcher.turretStop()
	if state[7] == 1 and oldstate[7] == 0: #turret fire
		launcher.turretFire()
	if state[7] == 0 and oldstate[7] == 1: #turret fire stop
		pass
	print "got to the end"
	return
	
	
# Main loop

def hapticFeedback():
	s = roomba.sensors
	bumpl = s.bumps.left
	bumpr = s.bumps.right
	dl = s.proximity.dataList
	proxl = dl[0] << 8 + dl[1]
	proxfl = dl[2] << 8 + dl[3]
	proxcl = dl[4] << 8 + dl[5]
	proxr = dl[10] << 8 + dl[11]
	proxfr = dl[8] << 8 + dl[9]
	proxcr = dl[6] << 8 + dl[7]
	
	#box up sensor data [l, cl, cr, r, lb, rb]
	#prox data is between 0 and 4096
	#bumper data is digital
	
	MAXVAL = 4096
	
	proxl = (int) (((proxl + proxcl)/2)/(7*MAXVAL))#average left-most sensors
	proxcl = (int) (proxcl / (7*MAXVAL))
	proxr = (int) (((proxr + proxfr)/2)/(7*MAXVAL))
	proxcr = (int) (proxcr / (7*MAXVAL))
	
	haptics.writelines(str([proxl, proxcl, proxr, proxcr, bumpl, bumpr]).strip('[]'))
	print([proxl, proxcl, proxr, proxcr, bumpl, bumpr])
	
	
	

oldstate = [0,0,0,0,0,0,0,0]
state = [0,0,0,0,0,0,0,0]


while True:
	ui.refreshState()
	state = ui.state
	print oldstate
	print ui.state
	print "\n"
	if not (state == oldstate):
		processState(state,oldstate)
		print "state transition performed"
	oldstate = deepcopy(ui.state)
	time.sleep(0.01) #loop rate 100Hz
	

