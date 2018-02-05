#example
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

PIN12= "P9_12" #GPIO60
RELAY1 = "P9_17" #GPIO4
RELAY2 = "P9_11" #GPIO30
RELAY3 = "P9_13" #GPIO31
ADC1 = "P9_33" #AIN4
adc_data = 0.00
voltage = 0.00

GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)
GPIO.setup(RELAY3, GPIO.OUT)
ADC.setup()

while True:
	print("Relay1 ON")
	GPIO.output(RELAY1, GPIO.HIGH) 
	time.sleep(2) #Wait 2 sec
	adc_data = ADC.read(ADC1)
	voltage = adc_data * 1.8*9 #1.8V
	print("Voltage: ")
	print(voltage)
	#print("adc_data: ")
	#print(adc_data)

#GPIO.cleanup() #cleans up pins

