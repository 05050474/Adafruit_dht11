#!/usr/bin/env python3
import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
while True:
	if (GPIO.input(23)==1):
		print('Turn on the switch')
		time.sleep(1)
	if(GPIO.input(23)==0):
		print('Turn off the switch')
		time.sleep(1)
