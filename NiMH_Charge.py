#Program that determines when NiMH batteries have reached 10V.
import Adafruit_BBIO.GPIO as GPIO
import timeit
import time
import smtplib

PIN12= "P9_12" #GPIO60
RELAY1 = "P9_17" #GPIO4
RELAY2 = "P9_11" #GPIO30
RELAY3 = "P9_13" #GPIO31
ADC1 = "P9_33" #AIN4
adc_data = 0.00 #raw adc pin data
voltage = 0.00 #voltage of battery
i = 0 #counter
time_elapsed = 0 #run time of program, how long battery takes to get to 10V
email = "nimh.charge@gmail.com" #email to send and recieve notification
pwd = "bu0y$0Lar7"  

#Set up pins
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)
GPIO.setup(RELAY3, GPIO.OUT)
ADC.setup()

#Open file to write	
v_datafile = open("voltage_data.txt", "w") 

#Functions
#Turns relay of choice ON
def relayOn(relay_num):
	print("Relay1 ON")
	GPIO.output(relay_num, GPIO.HIGH) 
	
#Turns relay of choice OFF
def relayOff(relay_num):
	print("Relay1 OFF")
	GPIO.output(relay_num, GPIO.LOW) 

def process_Data():
	adc_data = ADC.read(ADC1) #get raw data from adc pin
	voltage = (adc_data * 1.8*9)*(12.59/12.78) #convert to volts
	print("Voltage: " + str(voltage)) #print out voltage to user
	v_datafile.write(voltage) #write voltages to data file

#Send Email	
def notification():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email,pwd)
	msg = "NiMH Charge Program Completed"
	server.sendmail(email, email, msg) #From, To, Body
	server.quit()
	
#----Main----#
#Get user email and password
	

while True:
	relayOn(RELAY1) #Turn on relay 1
	time.sleep(5) #take voltage reading every 5s
	process_Data() #compute voltage, print it, send it to text file
	if voltage <= 10:
		relayOff(RELAY1) #Turn off relay 1 if the voltage goes down to 10V
		print("Relay OFF...Reached 10V")
		print("Time Elapsed: " str(time_elapsed)) 
		time_elapsed = timeit.timeit() #keep track of time elapsed
		notification() #Send email notification
		v_datafile.close() #close data file
		exit() #exit program

#GPIO.cleanup() #cleans up pins

