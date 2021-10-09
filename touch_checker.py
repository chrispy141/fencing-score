#/bin/python3
import time
import RPi.GPIO as GPIO
from FencingFunctions import *

HIT_PIN = 5 

# Create my app

# Read in calibration value

if __name__ == "__main__":
	id = "goat"
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(HIT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	touchTime = 0
	noTouchTime = 9999
	lastHitState=True
	while True:
		hit_state = GPIO.input(HIT_PIN)

		#touch detected	
		if (hit_state == False):
			noTouchTime = 0
			if lastHitState == True: #new touch
				touchTime = 0;
			else:
				touchTime = touchTime + 1		
		#no touch detected
		if (hit_state == True):
			touchTime = 0
			if lastHitState == False: #touch just released
				noTouchTime = 0;
			else:
				touchTime = touchTime + 1		
		print("Touch Time: " + str(touchTime))
		print("Non Touch Time: " + str(noTouchTime))
		time.sleep(0.02)



 
