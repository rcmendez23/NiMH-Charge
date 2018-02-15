#Program that determines when NiMH batteries have reached 10V.
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import timeit
import time
import smtplib #email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PIN12 = "P9_12" #GPIO60
RELAY1 = "P9_17" #GPIO4
RELAY2 = "P9_11" #GPIO30
RELAY3 = "P9_13" #GPIO31
ADC1 = "P9_33" #AIN4

global time_elapsed #run time of program, how long battery takes to get to 10V

email = "nimh.charge@gmail.com" #email to send and recieve notification
pwd = "bu0y$0Lar7"  
path = '/srv/NiMH_Data/voltage_data.txt' #os.system.join("srv","NiMH_Data", "voltage_data.txt") #get file path
v_datafile = open(path, "w") #open file to write
#Set up pins
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)
GPIO.setup(RELAY3, GPIO.OUT)
ADC.setup()

#Functions
#Turns relay of choice ON
def relayOn(relay_num):
	print("Relay1 ON")
	GPIO.output(relay_num, GPIO.HIGH) 
	
#Turns relay of choice OFF
def relayOff(relay_num):
	print("Relay1 OFF")
	GPIO.output(relay_num, GPIO.LOW) 

#Calculate voltage
def calc_Voltage():
	global voltage 
	adc_data = ADC.read(ADC1) #get raw data from adc pin
	voltage = (adc_data * 1.8*9)*(12.59/12.78) #convert to volts

def write_Data(v_datafile):
	v_datafile.write(str(voltage)) #write voltages to data file

#Send Email	
def notification(time_elapsed):
	path = '/srv/NiMH_Data/voltage_data.txt' #path of data file
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(email,pwd)
	msg = MIMEMultipart()
	msg['Subject'] = 'NiMH Charge Program Status' #subject of email
	msg['From'] = email #sender's email address
	msg['To'] = email #reciever email addr
	msg.preamble = "NiMH Charge Program Completed. Time Elapsed is " + str(time_elapsed) + " sec" #message of email
	fp = open(path, 'rb') #get voltage data file
	txtFile = MIMEText(fp.read()) #read file
	msg.attach(txtFile) #attach file to email
	server.sendmail(email, email, msg.as_string()) #From, To, Body
	server.quit()
	
#----Main----#
#Get user email and password
while True:
	relayOn(RELAY1) #Turn on relay 1
	calc_Voltage() #compute voltage, print it, send it to text file
	write_Data(v_datafile) #write data to voltage_data.txt
	print("Voltage: " + str(voltage)) #print out voltage to user
	if voltage <= 10.0:
		relayOff(RELAY1) #Turn off relay 1 if the voltage goes down to 10V
		print("Relay OFF...Reached 10V")
		time_elapsed = timeit.timeit() #keep track of time elapsed
		print("Time Elapsed: " + str(time_elapsed)) 
		notification(time_elapsed) #Send email notification
		#v_datafile.close() #close data file
		break
	time.sleep(5) #take voltage reading every 5 minutes
relayOff(RELAY1)
exit() #exit program
#GPIO.cleanup() #cleans up pins

