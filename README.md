# NiMH-Charge
BY REBECCA MENDEZ
Northeastern University NUMONET Lab
---------------------------------------------------------------------------
This is a Python program to run on BeagleBone Black (BBB) which detects the charge state of NiMH batteries. Currently, to test the program, the battery is discharged using a relay board which is activated by one of the BBB GPIO pins. The BBB ADC Pin reads in the voltage of the batteries and once they reach 10V, the program ends and an email is sent with the data attached as a text file.
The program uses the *Adafruit BBIO Library* to control GPIO Pins of BBB and an ADC Pin.
Email is sent using smtplib when program finishes.

# Setup
### 1. Connect to your BeagleBone Black (BBB) with a USB cable to your PC and connect it to the internet using an Ethernet Cable. 
### 2. On a PC, use PuTTY or other client to SSH to the BBB.
    a. How to SSH using PuTTY
Try 192.168.7.2 as IP
### 3. Make sure Git is installed on the BBB by executing `git` in the command line.
### 4. Create a new folder in `/srv` called `git`.
`cd /srv`

In `/srv` execute `mkdir git`
### 5. Create a folder `NiMH_Data` in `/srv`
In `/srv` execute `mkdir NiMH_Data`
### 6. Clone the `NiMH-Charge.git` repository into `/srv/git`
### 7. Set up GPIO Pins on BBB
In `/sys/class/gpio` execute `ls`. This will show all the gpio pins exported. New BBBs do not have all gpio pins exported yet.

`NiMH-Charge.py` uses the following GPIO Pins as denoted by the following lines of code:
```
RELAY1 = "P9_17" #GPIO4
RELAY2 = "P9_11" #GPIO30
RELAY3 = "P9_13" #GPIO31
ADC1 = "P9_33" #AIN4
```
The variables in all-caps store strings that the Adafruit BBIO Library understands as a physical pin location on the BBB. Next to the hashtag (#) are comments stating the GPIO Pin number associated with that pin on the BBB. ADC1 is an analog to digital converter pin.
For setting up the GPIO pin, we care only about the GPIO Pin number next to the hashtag (#). This is the BBBs identifier for each GPIO pin. You could pick any GPIO pin on your BBB as long as you change the above lines of code.

We will activate `GPIO4` which is `RELAY1`. You only need one relay for this program.

Navigate to the specific gpio folder of the gpio pin we want to activate. 

In `/sys/class/gpio` execute `cd gpio4`

In `/sys/class/gpio/gpio4` execute `echo 4 > export`

Go back to `/sys/class/gpio` by executing `cd ..`

In `/sys/class/gpio` execute `ls` to confirm that `gpio4` is now on the list.
