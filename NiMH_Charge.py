#example
import Adafruit_BBIO.GPIO as GPIO
import time

PIN12= "P9_12"

GPIO.setup(PIN12, GPIO.OUT)
while True:
	GPIO.output(PIN12, GPIO.LOW)
	print("OFF...")
	time.sleep(5000)
	print("delay...")
	GPIO.output(PIN12, GPIO.HIGH)
	print("ON...")
	time.sleep(5000)
	print("delay...")
#GPIO.cleanup() #cleans up pins