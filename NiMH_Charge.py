#example
import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.output("P9_14", GPIO.LOW)
sleep(1000)
GPIO.setup("P9_14", GPIO.OUT)
GPIO.output("P9_14", GPIO.HIGH)


#GPIO.cleanup() #cleans up pins