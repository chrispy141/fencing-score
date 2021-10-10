#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
from FencingFunctions import *

HIT_PIN = 4

# Create my app

url = getUrl()

# Read in calibration value
def processTouch(touchTime, noTouchTime):
	
	if touchDetected:
		if touchTime == 300:
			print("reset")
			reset(url, "Goat")
		else:
			if touchTime == 50:
				print("remove touch")
				removeTouch(url, "Goat")
			else:
				if noTouchTime > 20:
					touch(url, "Goat")


if __name__ == "__main__":
	id = "Goat"
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(HIT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	touchTime = 0
	noTouchTime = 9999
	lastHitState=True
	touchDetected = False
	while True:
		hit_state = GPIO.input(HIT_PIN)

		#touch detected	
		if (hit_state == False):
			touchDetected = True
			if lastHitState == True: #new touch
				touchTime = 0;
			else:
				touchTime = touchTime + 1		
			processTouch(touchTime, noTouchTime)
			noTouchTime = 0
		#no touch detected
		if (hit_state == True):
			touchDetected = False
			touchTime = 0
			if lastHitState == False: #touch just released
				noTouchTime = 0;
			else:
				noTouchTime = noTouchTime + 1		
		lastHitState=hit_state

			
		time.sleep(0.02)



 
