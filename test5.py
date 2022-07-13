from __future__ import print_function
from dronekit import connect, VehicleMode
import time

import argparse

def ConnectMyCopter():
    parser = argparse.ArgumentParser(description='Example showing how to set and clear vehicle channel-override information.')
    parser.add_argument('--connect', 
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
    args = parser.parse_args()

    connection_string = args.connect
    sitl = None

    if not connection_string:
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = sitl.connection_string()

    print('Connecting to vehicle on: %s' % connection_string)
    vehicle = connect(connection_string, baud=921600, wait_ready=True)
    
    return vehicle

def arm():
    vehicle.mode = VehicleMode("MANUAL")
    vehicle.armed = True

def turnright():
    counter = 0
    while counter <= 10:
        vehicle.channels.overrides = {'1':1900}
        counter += 1
    
def turnleft():
    counter = 0
    while counter <= 10:
        vehicle.channels.overrides = {'1':1100}
        counter += 1
    
def forward():
    counter = 0
    while counter <= 10:
        vehicle.channels.overrides = {'3':1900}
        counter += 1

def backward():
    counter = 0
    while counter <= 10:
        vehicle.channels.overrides = {'3':1300}
        counter += 1
        
        
####MAIN FUNCTION
vehicle = ConnectMyCopter()
arm()


print("Channel values from RC Tx:", vehicle.channels)

# Access channels individually
print("Read channels individually:")
print(" Ch1: %s" % vehicle.channels['1'])
print(" Ch2: %s" % vehicle.channels['2'])
print(" Ch3: %s" % vehicle.channels['3'])
print(" Ch4: %s" % vehicle.channels['4'])
print(" Ch5: %s" % vehicle.channels['5'])
print(" Ch6: %s" % vehicle.channels['6'])
print(" Ch7: %s" % vehicle.channels['7'])
print(" Ch8: %s" % vehicle.channels['8'])
print("Number of channels: %s" % len(vehicle.channels))

'''counter = 0
while counter <= 10:
    vehicle.channels.overrides = {'3':1900}
    counter += 1'''

forward()
time.sleep(5)
turnright()
time.sleep(5)
turnleft()
#
    