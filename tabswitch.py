#!/usr/bin/python


import os

from time import sleep

import RPi.GPIO as GPIO


sleep(15)


GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    if ( GPIO.input(26) == 1):
        
			os.system('sudo xdotool search --onlyvisible --class "chromium" windowfocus && xdotool key ctrl+Tab') 
        
			sleep(1)
    
		elif ( GPIO.input(6) == 1):
        
			os.system('sudo xdotool search --onlyvisible --class "chromium" windowfocus && xdotool key F5') 
        
			sleep(1)
    
		else:
        
			sleep(0.1)