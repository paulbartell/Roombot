#!/usr/bin/env python

from RoombaSCI import RoombaAPI
from stormLauncher import launchControl
import pyserial
from EmgInterface import EmgInterface

ROOMBA_PORT="/dev/tty.usbserial-A2001n69"
ROOMBA_BAUD="115200"

HAPTICS_PORT="/dev/rfcomm0"
HAPTICS_BAUD="115200"

EMG_PORT="/dev/rfcomm1"
EMG_BAUD="115200"



launcher = launchControl();
roomba = RoombaAPI(ROOMBA_PORT, ROOMBA_BAUD);
emg = EmgInterface(EMG_PORT, EMG_BAUD);




emg = EmgInterface("/dev/tty.M13762-BluetoothSerialP",115200)