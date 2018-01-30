#example
import Adafruit_BBIO.GPIO as GPIO
import time

PIN12= "P9_12"

GPIO.setup(PIN12, GPIO.OUT)
while True:
	print("OFF...")
	GPIO.output(PIN12, GPIO.LOW)
	print("delay...")
	time.sleep(5)
	print("ON...")
	GPIO.output(PIN12, GPIO.HIGH)
	print("delay...")
	time.sleep(5)
#GPIO.cleanup() #cleans up pins