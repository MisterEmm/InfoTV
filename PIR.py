#!/usr/bin/python


import os

from time import sleep

from gpiozero import MotionSensor



pir = MotionSensor(4)


while True:
    
	if pir.motion_detected:
        
		os.system('sudo xscreensaver-command -deactivate &')
        
		sleep(15)
    
	else:
        
		sleep(0.1)
