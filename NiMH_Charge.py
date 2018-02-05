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

def relayOn():
	print("Relay1 ON")
	GPIO.output(RELAY1, GPIO.HIGH) 
	time.sleep(2) #Wait 2 sec
	adc_data = ADC.read(ADC1)
	voltage = (adc_data * 1.8*9)*(12.59/12.78) 
	print("Voltage: ")
	print(voltage)

def relayOff():
	print("Relay1 OFF")
	GPIO.output(RELAY1, GPIO.LOW) 
	time.sleep(2) #Wait 2 sec
	adc_data = ADC.read(ADC1)
	voltage = (adc_data * 1.8*9)*(12.59/12.78) 
	print("Voltage: ")
	print(voltage)
	
#Main
while True:
	for i in range 50:
		relayOn()
		if i%2 == 0:
			relayOff()
	

	
	
	
#GPIO.cleanup() #cleans up pins

