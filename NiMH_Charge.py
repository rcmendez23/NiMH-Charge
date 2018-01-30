#example
import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_14", GPIO.OUT)
for i in range(5):
  GPIO.output("P9_14", GPIO.LOW)
  time.sleep(1000)
  GPIO.output("P9_14", GPIO.HIGH)


#GPIO.cleanup() #cleans up pins