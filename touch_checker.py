#/bin/python3
import time
import RPi.GPIO as GPIO
from FencingFunctions import *

HIT_PIN = 5 
DEC_PIN = 4

# Create my app

# Read in calibration value

if __name__ == "__main__":
	id = "goat"
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(HIT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(DEC_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	timeSinceTouch=0
	timeSinceDec=0
	decCount=0
	while True:
		hit_state = GPIO.input(HIT_PIN)
		dec_state = GPIO.input(DEC_PIN)
		if (hit_state == False ): 
			if (timeSinceTouch > 50):
				timeSinceTouch = 0
				touch(id)
				print("hit")
		if (dec_state == False):
			if timeSinceDec > 10:
				decCount = decCount + 1
				
				if decCount > 3:
					timeSinceDec=0
					reset(id)
					decCount=0		
					print("reset")
			if timeSinceDec > 50:
				timeSinceDec=0
				decCount=0		
				removeTouch(id)
				print("remove touch")
		timeSinceTouch = timeSinceTouch + 1
		timeSinceDec = timeSinceDec + 1
		time.sleep(0.02)



 
