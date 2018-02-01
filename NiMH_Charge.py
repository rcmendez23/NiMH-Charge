#example
import Adafruit_BBIO.GPIO as GPIO
import time

PIN12= "P9_12" #GPIO60
RELAY2 = "P9_11" #GPIO30
RELAY3 = "P9_13" #GPIO31

GPIO.setup(PIN12, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)
GPIO.setup(RELAY3, GPIO.OUT)
while True:
	print("Relay2 ON")
	GPIO.output(RELAY2, GPIO.HIGH)
	GPIO.output(RELAY3, GPIO.LOW)
	time.sleep(2) #Wait 2 sec
	print("Relay3 ON")
	GPIO.output(RELAY2, GPIO.LOW)
	GPIO.output(RELAY3, GPIO.HIGH)
	time.sleep(2) #Wait 2 sec
	
	'''
	print("OFF...")
	GPIO.output(PIN12, GPIO.LOW)
	print("delay...")
	time.sleep(5)
	print("ON...")
	GPIO.output(PIN12, GPIO.HIGH)
	print("delay...")
	time.sleep(5)
	'''
#GPIO.cleanup() #cleans up pins

