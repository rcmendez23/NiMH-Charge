#example
import Adafruit_BBIO.GPIO as GPIO
import time

PIN12= "P9_12"

GPIO.setup(PIN12, GPIO.OUT)
while True:
	GPIO.output(PIN12, GPIO.LOW)
	time.sleep(5000)
	GPIO.output(PIN12, GPIO.HIGH)

#GPIO.cleanup() #cleans up pins