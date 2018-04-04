# NiMH-Charge
BY REBECCA MENDEZ
Northeastern University NUMONET Lab
---------------------------------------------------------------------------
This is a Python program to run on BeagleBone Black (BBB) which detects the charge state of NiMH batteries. Currently, to test the program, the battery is discharged using a relay board which is activated by one of the BBB GPIO pins. The BBB ADC Pin reads in the voltage of the batteries and once they reach 10V, the program ends and an email is sent with the data attached as a text file.
The program uses the Adafruit BBIO library to control GPIO Pins of BBB and an ADC Pin.
Email is sent using smtplib when program finishes.

# Setup
### 1. Connect to your BeagleBone Black (BBB) with a USB cable to your PC and connect it to the internet using an Ethernet Cable. 
### 2. On a PC, use PuTTY or other client to SSH to the BBB.
    a. How to SSH using PuTTY
Try 192.168.7.2 as IP
### 3. Make sure Git is installed on the BBB by executing `git` in the command line.
### 4. Create a new folder in `/srv` called `git`.
`cd /srv`

In `/srv` execute mkdir git
### 5. Create a folder `NiMH_Data` in `/srv`
### 6. Clone the `NiMH-Charge.git` repository into `/srv/git`
### 7. Set up GPIO Pins on BBB
In `/sys/class/gpio` execute `ls`. This will show all the gpio pins exported. New BBBs do not have all gpio pins exported yet.
Navigate to the specific gpio folder of the gpio pin we want to activate.
The program uses the following GPIO Pins:

In `/sys/class/gpio` execute `echo 4 > export`
In `/sys/class/gpio` execute `ls` to confirm that `gpio4` is now on the list.


