# NiMH-Charge
BY REBECCA MENDEZ
---------------------------------------------------------------------------
This is a Python program on BeagleBone Black (BBB) which detects the charge state of NiMH batteries. Currently, to test the program,
the battery is discharged using a relay board which is activated by one of the BBB GPIO pins. The BBB ADC Pin reads in the voltage of the batteries and once they reach 10V, the program ends and an email is sent with the data attached as a text file.  

The program uses the Adafruit BBIO library to control GPIO Pins of BBB and an ADC Pin.

Email is sent using smtplib when program finishes.
