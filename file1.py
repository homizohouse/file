Practical No : 0
Power  : 1, 2, 4, 17
Ground : 6, 9, 14, 20, 25, 30, 34, 39
I2C    : 3, 5
UART   : 8, 10
SPI    : 19, 21, 23, 24, 26


PRACTICAL NO: 01
AIM:	Displaying different LED patterns with Raspberry Pi.
Hardware Required:
•	Raspberry Pi 
•	Ethernet Cable / Wifi
•	USB Keyboard , USB Mouse Cables, Power Supply & HDMI cable
•	Jumper Wires (Female to Female)
•	Micro SD Card
•	LED (Light Emitting Diode)
Step 1: Basic Raspberry Pi Connections to be done 
Step 2: Right Click Create a NEW file with as extension .py as LED.py 
Step 3: Go to Raspberry Pi Symbol -> Programming -> Thonny and type the following code 
Step 4: LED Hardware Connection
LED 1
Long leg (+) → Pin 11
Short leg (-) → Pin 6 (Ground)

LED 2
Long leg (+) → Pin 13
Short leg (-) → Pin 14 (Ground)

Code:
import RPi.GPIO as GPIO
import time
numTimes = int(input("Enter total number of blinks: "))
speed = float(input("Enter length of each blink (seconds): "))
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		# Using board pin numbering
GPIO.setup(11, GPIO.OUT)			# LED 1 on Pin 11
GPIO.setup(13, GPIO.OUT)			# LED 2 on pin 13
def Blink(numTimes, speed):
    for i in range(numTimes):
        print("Iteration: ", i+1)
        GPIO.output(11, True)
        GPIO.output(13, True)
        time.sleep(speed)
        GPIO.output(11, False)
        GPIO.output(13, False)
        time.sleep(speed)
Blink(numTimes, speed)
GPIO.cleanup()
print("Done")



logic for 4 leds:

⭐ Use These Pins
LED	GPIO	Physical Pin
LED-1	GPIO17	Pin 11
LED-2	GPIO27	Pin 13
LED-3	GPIO22	Pin 15
LED-4	GPIO23	Pin 16
⭐ Cathode (Ground) Connection
You can connect cathodes like this:
LED-1 cathode → Pin 6 (GND)
LED-2 cathode → Pin 9 (GND)
LED-3 cathode → Pin 14 (GND)
LED-4 cathode → Pin 20 (GND

Code:
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# LED pin numbers
led1 = 11
led2 = 13
led3 = 15
led4 = 16

# setup pins as output
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

try:
    while True:

        # ⭐ PATTERN 1 : ALL LEDs BLINK TOGETHER (Simultaneous)
        GPIO.output(led1, True)
        GPIO.output(led2, True)
        GPIO.output(led3, True)
        GPIO.output(led4, True)
        time.sleep(1)

        GPIO.output(led1, False)
        GPIO.output(led2, False)
        GPIO.output(led3, False)
        GPIO.output(led4, False)
        time.sleep(1)


        # ⭐ PATTERN 2 : ODD LEDs BLINK (LED1 & LED3)
        GPIO.output(led1, True)
        GPIO.output(led3, True)
        time.sleep(1)

        GPIO.output(led1, False)
        GPIO.output(led3, False)
        time.sleep(1)


        # ⭐ PATTERN 3 : EVEN LEDs BLINK (LED2 & LED4)
        GPIO.output(led2, True)
        GPIO.output(led4, True)
        time.sleep(1)

        GPIO.output(led2, False)
        GPIO.output(led4, False)
        time.sleep(1)


        # ⭐ PATTERN 4 : RUNNING LED (Forward Sequence)
        GPIO.output(led1, True)
        time.sleep(0.5)
        GPIO.output(led1, False)

        GPIO.output(led2, True)
        time.sleep(0.5)
        GPIO.output(led2, False)

        GPIO.output(led3, True)
        time.sleep(0.5)
        GPIO.output(led3, False)

        GPIO.output(led4, True)
        time.sleep(0.5)
        GPIO.output(led4, False)


        # ⭐ PATTERN 5 : RUNNING LED (Reverse Sequence)
        GPIO.output(led4, True)
        time.sleep(0.5)
        GPIO.output(led4, False)

        GPIO.output(led3, True)
        time.sleep(0.5)
        GPIO.output(led3, False)

        GPIO.output(led2, True)
        time.sleep(0.5)
        GPIO.output(led2, False)

        GPIO.output(led1, True)
        time.sleep(0.5)
        GPIO.output(led1, False)


        # ⭐ PATTERN 6 : INCREASING STEP PATTERN
        GPIO.output(led1, True)
        time.sleep(0.5)

        GPIO.output(led2, True)
        time.sleep(0.5)

        GPIO.output(led3, True)
        time.sleep(0.5)

        GPIO.output(led4, True)
        time.sleep(1)

        GPIO.output(led1, False)
        GPIO.output(led2, False)
        GPIO.output(led3, False)
        GPIO.output(led4, False)
        time.sleep(1)


        # ⭐ PATTERN 7 : DECREASING STEP PATTERN
        GPIO.output(led1, True)
        GPIO.output(led2, True)
        GPIO.output(led3, True)
        GPIO.output(led4, True)
        time.sleep(1)

        GPIO.output(led4, False)
        time.sleep(0.5)

        GPIO.output(led3, False)
        time.sleep(0.5)

        GPIO.output(led2, False)
        time.sleep(0.5)

        GPIO.output(led1, False)
        time.sleep(1)


except KeyboardInterrupt:
    GPIO.cleanup()




 
PRACTICAL NO. 2
Aim:- Visitor Monitoring With Raspberry Pi and and Pi Camera (Image or Video)
Hardware Required:
•	Raspberry Pi 
•	Ethernet Cable / Wifi
•	USB Keyboard , USB Mouse Cables, Power Supply & HDMI cable
•	Micro SD Card
•	Camera
Step1 :- Go to terminal
Type command  sudo raspi-config
Go to interface option Enable settingSERIAL PORTSPII2C
Step 2 :-
 Type command  sudo raspi-config -->Then:
Go to Interface Options
Enable the camera
Exit the configuration.
to restart Raspberry Pi to monitoring a camera.
Step 3:- Type command  libcamera-hello
To check the camera is monitoring or not.
Step 4:- Type command  libcamera-still -o image.jpg
Click Image  Save in File Manager home/pi save as  image.jpg
Step 5:- Type command  libcamera-vid -o video.h264 -t 10000
Click Video  Save in File Manager home/Sneha save as  video h264
  
     
PRACTICAL NO: 03
AIM: Controlling Raspberry pi with Telegram Bot.
Step 1: Open Telegram Application in Mobile Phone.
Step 2: Search “botfather”.
Step 3: type “/start” in chat.
Step 4: Again type “/newbot” to create you account.
Step 5: You will get option to choose a name for your bot. Enter your name_bot.
Step 6: After creating your bot you will get your API bot token.
8050749118:AAFzQfBUcMfFtsQLKZC3r6dyPyolot8nrWk 
Step 7: Go to your Raspberry pi  Open command prompt and type this commands.
Command: sudo apt-get install python3-pip -y
Command: sudo apt install python3-venv
Command: python3 -m venv myenv
Command:  source myenv/bin/activate 
Command:  pip install telepot
Command:  pip install RPi.GPIO
Command:  git clone https://github.com/salmanfarisvp/TelegramBot.git
Command: cd TelegramBot
Open the Python file
Command: nano telegrambot.py
Insert the  token number that received in telegram find the line  bot=telepot.Bot('YOUR_TOKEN_HERE')
Replace it with  bot = telepot.Bot('8050749118:AAFzQfBUcMfFtsQLKZC3r6dyPyolot8nrWk')
Then save the file with ctrl+s and exit the code ctrl+x.
Code:
#coder :- Salman Faris
import sys
import time
import telepot
import RPi.GPIO as GPIO
#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Got command: %s' % command)
    if command == 'on':
       bot.sendMessage(chat_id, on(11))
    elif command =='off':
       bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('YOUR_TELEGRAM_BOT_TOKEN')
bot.message_loop(handle)
print('I am listening...')
while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
    
    except:
        print('Other error or exception occured!')
        GPIO.cleanup()

       (OR)

#coder :- Salman Faris

import sys
import time
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'on':
       bot.sendMessage(chat_id, on(11))
    elif command =='off':
       bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('8520626333:AAFqECBw3UrOp7ILDqf1DllQvd83mkuIzCg')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
    
    except:
        print('Other error or exception occured!')
        GPIO.cleanup()
 
Step 8: Run this code
Command: python3 telegrambot.py
 
Step 9: Type “on” and “off” in your telegram app to turn on and turn off your led.
 



Practical 4 
Aim: How to Install Windows 10 on the Raspberry Pi 4.
Hardware:
•	Raspberry Pi 4 (4GB or 8GB recommended, 2GB is possible but very slow).
•	Storage device:
	Option 1: MicroSD card (at least 32GB, Class 10)
	Option 2 (better): USB 3.0 SSD (faster and more reliable).
•	HDMI monitor, keyboard, mouse, power supply.
•	Optional: USB Ethernet adapter

Steps:
Step 1: Download the latest pre-release version of WoR tool https://www.worproject.ml/downloads and extract the files.

only Perform this then write all steps on paper 

Step 2: Prepare Windows 10 ARM64 ISO
1.	Go to UUPDump.net.
2.	Choose Windows 10 ARM64 build (choose latest stable).
3.	Download the script (zip file) and run it on your Windows PC.
	-It downloads required files directly from Microsoft and builds an ISO.
4.	At the end, you’ll have a Windows 10 ARM64 ISO file.

Step 3: Install WoR and Prepare the SD/SSD
1.	Insert your SD card or SSD into your Windows PC.
2.	Open WoR.exe (run as Administrator).
3.	Follow the wizard:
  	-Step 1: Select your device (SD/SSD).
 	-Step 2: Point to your Windows 10 ARM64 ISO.
 	-Step 3: Select your device type: Raspberry Pi 4.
	-Step 4: Provide the UEFI firmware and drivers.
 	-Step 5: Confirm installation settings.
4.	WoR will now flash the Windows image to your device.
	-This can take 30–60 minutes depending on storage speed.

Step 4: Booting Raspberry Pi 4
1.	Insert the prepared storage into your Raspberry Pi 4.
2.	Power it on → it will first load into the UEFI firmware screen.
3.	(Optional but recommended):
	-Go into UEFI settings.
	-Change Boot Order to make your SD/SSD the first boot option.
	-Save and reboot.
4.	Now, Windows 10 setup begins.
	-Select language, region, keyboard layout.
	-Create or skip Microsoft account.
	-Configure system preferences.
5.	For network access, use a USB to Ethernet or a compatible WiFi dongle.
6.	Install Microsoft Edge by double clicking on the Microsoft Edge desktop icon.

Final Output (Write in Journal)
Result:
Windows 10 ARM operating system was successfully installed and booted on the Raspberry Pi 4 using the WoR tool.

PRACTICAL NO: 05 
Aim: Raspberry Pi GPS Module interfacing
Wire Connection:
GPS Module	GPIO pin
VCC			Pin 2
GND			Pin 6
Tx			Pin 10

(If GPS module has RX pin, connect to Pin 8)

Setup:	Raspberry Pi Menu → Accessories → Terminal
STEP 1 :- (Create a virtual environment)	
1) Installing the venv module:-
	sudo apt install python3-venv     

2) Creating a new virtual environment. myenv is user-defined name
	python3 -m venv myenv 

3) Activate the Virtual Environment
source myenv/bin/activate

Enable UART Communication
sudo raspi-config
Go to:
Interface Options → Serial Port

4) It should look like :-  (myenv) pi@raspberrypi:- $
(If virtual environment is already created just activate the environment)
STEP 2 :- Enter the following commands one by one, pressing Enter after each.
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
sudo systemctl stop serial-getty@ttyS0.service
sudo systemctl disable serial-getty@ttyS0.service
sudo systemctl enable serial-getty@ttyAMA0.service
 
STEP 3:- Installing minicom
	sudo apt-get install minicom
 
STEP 4:- Installing pynmea2
	pip install pynmea2 --break-system-packages
STEP 5 :-
        pip install pyserial
	sudo cat /dev/ttyS0
You should see GPS NMEA data like:
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
$GPRMC,123520,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A
Press:
CTRL + C
to stop.
(This will run in the background. To stop this press ctrl + C). You will get the output.
The following steps are optional.
 
STEP 6 :-
Open Thonny → New file
Save as:
gps_read.py:- code:
import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio  #if error here use command:-  pip install Rpi.GPIO
gpio.setmode(gpio.BCM)
port = "/dev/ttyS0" # the serial port to which the pi is connected.
#create a serial object
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while 1:
    try:
        data = ser.readline()
        print(data)
    except:
	print("loading") 
#wait for the serial port to churn out data
 
    if data[0:6] == '$GPRMC':  
     	msg = pynmea2.parse(data)
 	print msg
	time.sleep(2)


          (OR)

import serial
import time
import string
import pynmea2

port = "/dev/serial0"

ser = serial.Serial(port, baudrate=9600, timeout=0.5)

while True:
    newdata = ser.readline().decode('utf-8', errors='ignore')

    if newdata.startswith("$GPRMC"):
        try:
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lng = newmsg.longitude

            gps = "Latitude = " + str(lat) + " and Longitude = " + str(lng)
            print(gps)

        except pynmea2.ParseError:
            continue


Step 8 – Run the Program
Run:
python3 gps_read.py

Step 9 – Output
Terminal will display GPS coordinates.
Example:
Latitude: 19.0760
Longitude: 72.8777
or raw NMEA data like:
$GPRMC,123520,A,4807.038,N,01131.000,E

Step 10 – Stop the Program
Press:
CTRL + C

STEP 11:-  To deactivate virtual environment
 	deactivate 

PRACTICAL NO: 06
Aim: Displaying Time over 4-Digit 7-Segment Display using Raspberry Pi.
Connection scheme Raspberry Pi
| TM1637 Pin | Raspberry Pi Pin |
| ---------- | ---------------- |
| GND        | Pin 14           |
| VCC        | Pin 4            |
| DIO        | Pin 18           |
| CLK        | Pin 16           |

Step 1: Open the terminal and enter the following command
pip install RPi.GPIO --break-system-packages
To control the LED, we use special script with pre-defined functions. Various function are available in the script, for example you can display numbers and adjust the intensity of the LEDs. Download the script with the command:
git clone https://github.com/bhoomikapansare/7Segment.git
Go inside the folder:
cd 7Segment

       (OR)
tml1637.py:-

import RPi.GPIO as GPIO
import time

# digit to segment mapping
SEGMENTS = (0x3f, 0x06, 0x5b, 0x4f,
            0x66, 0x6d, 0x7d, 0x07,
            0x7f, 0x6f)

BRIGHT_TYPICAL = 2

class TM1637:
    def __init__(self, brightness=BRIGHT_TYPICAL):
        self.clk = 23
        self.dio = 24
        self.brightness = brightness & 0x07
        self.doublepoint = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.clk, GPIO.OUT)
        GPIO.setup(self.dio, GPIO.OUT)

    def start(self):
        GPIO.output(self.clk, 1)
        GPIO.output(self.dio, 1)
        GPIO.output(self.dio, 0)
        GPIO.output(self.clk, 0)

    def stop(self):
        GPIO.output(self.clk, 0)
        GPIO.output(self.dio, 0)
        GPIO.output(self.clk, 1)
        GPIO.output(self.dio, 1)

    def write_byte(self, data):
        for i in range(8):
            GPIO.output(self.clk, 0)
            GPIO.output(self.dio, (data >> i) & 1)
            GPIO.output(self.clk, 1)

        GPIO.output(self.clk, 0)
        GPIO.setup(self.dio, GPIO.IN)
        ack = GPIO.input(self.dio)
        GPIO.setup(self.dio, GPIO.OUT)
        GPIO.output(self.clk, 1)
        return ack

    def SetBrightness(self, brightness):
        self.brightness = brightness & 0x07

    def ShowDoublepoint(self, on):
        self.doublepoint = on

    def Show(self, data):
        seg_data = []
        for i in range(4):
            seg = SEGMENTS[data[i]]
            if i == 1 and self.doublepoint:  # colon between digit 2 & 3
                seg |= 0x80
            seg_data.append(seg)

        self.start()
        self.write_byte(0x40)
        self.stop()

        self.start()
        self.write_byte(0xC0)
        for d in seg_data:
            self.write_byte(d)
        self.stop()

        self.start()
        self.write_byte(0x88 + self.brightness)
        self.stop()

    def Clear(self):
        self.Show([0, 0, 0, 0])


Open Python Editor
Open:
Raspberry Pi Menu → Programming → Thonny
Create a new file and save it as:
clock_display.py
Step 2: Type the following python program in Thonny
import time
import datetime
import RPi.GPIO as GPIO
import tm1637

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

display = tm1637.TM1637(clk=23, dio=24)
display.brightness(3)

try:
    while True:
        now = datetime.datetime.now()

        hour = now.hour
        minute = now.minute

        display.show([
            hour // 10,
            hour % 10,
            minute // 10,
            minute % 10
        ])

        display.show_doublepoint(now.second % 2)

        time.sleep(1)

except KeyboardInterrupt:
    display.clear()
    GPIO.cleanup()

                    OR
import sys
import time
import datetime
import RPi.GPIO as GPIO
import tml1637
GPIO.setmode(GPIO.BCM) # or GPIO.BOARD depending on your wiring
Display=tml1637.TM1637()
Display.Clear()
Display.SetBrightness(1)
while True:
    now=datetime.datetime.now()
    hour=now.hour
    minute=now.minute
    second=now.second
    currenttime=[int(hour/10), hour%10, int(minute/10), minute%10]
    Display.Show(currenttime)
    Display.ShowDoublepoint(second%2)
    time.sleep(1)


step 3: run the thonny
The 7-segment display will show current time like:

12:45

The colon (:) will blink every second.



PRACTICAL NO: 07
Aim: IOT base Web Controlled Home Automation using Raspberry Pi.
•Connection scheme Raspberry Pi
for 1 relay:- 
Relay Module	             RPi Pin
GND				6
VCC				2
IN1				26

If you use more relays:
Relay	Raspberry Pi Pin
IN1	Pin 26
IN2	Pin 24
IN3	Pin 21
IN4	Pin 19

Step1: Setup
Step2: Write Python code
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from time import sleep
relay_pin=26
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin,GPIO.OUT)
GPIO.output(relay_pin,1)
try:
    while True:
        GPIO.output(relay_pin,0)
        sleep(5)
        GPIO.output(relay_pin,1)
        sleep(5)
except KeyboardInterrupt:
    pass
    GPIO.cleanup()


Program for 2 Relays / LEDs
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

relay_pin1 = 26
relay_pin2 = 24

GPIO.setmode(GPIO.BOARD)

GPIO.setup(relay_pin1, GPIO.OUT)
GPIO.setup(relay_pin2, GPIO.OUT)

GPIO.output(relay_pin1, 1)
GPIO.output(relay_pin2, 1)

try:
    while True:
        GPIO.output(relay_pin1, 0)
        GPIO.output(relay_pin2, 1)
        sleep(1)

        GPIO.output(relay_pin1, 1)
        GPIO.output(relay_pin2, 0)
        sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

Program for 3 Relays / LEDs

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

relay_pin1 = 26
relay_pin2 = 24
relay_pin3 = 21

GPIO.setmode(GPIO.BOARD)

GPIO.setup(relay_pin1, GPIO.OUT)
GPIO.setup(relay_pin2, GPIO.OUT)
GPIO.setup(relay_pin3, GPIO.OUT)

GPIO.output(relay_pin1, 1)
GPIO.output(relay_pin2, 1)
GPIO.output(relay_pin3, 1)

try:
    while True:
        GPIO.output(relay_pin1, 0)
        GPIO.output(relay_pin2, 1)
        GPIO.output(relay_pin3, 0)
        sleep(1)

        GPIO.output(relay_pin1, 1)
        GPIO.output(relay_pin2, 0)
        GPIO.output(relay_pin3, 1)
        sleep(1)

        GPIO.output(relay_pin1, 0)
        GPIO.output(relay_pin2, 0)
        GPIO.output(relay_pin3, 1)
        sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

Program for 4 Relays:- 
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

relay1 = 26
relay2 = 24
relay3 = 21
relay4 = 19

GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.setup(relay3, GPIO.OUT)
GPIO.setup(relay4, GPIO.OUT)

try:
    while True:
        GPIO.output(relay1, 0)
        GPIO.output(relay2, 1)
        GPIO.output(relay3, 1)
        GPIO.output(relay4, 1)
        print("Relay 1 ON")
        time.sleep(2)

        GPIO.output(relay1, 1)
        GPIO.output(relay2, 0)
        GPIO.output(relay3, 1)
        GPIO.output(relay4, 1)
        print("Relay 2 ON")
        time.sleep(2)

        GPIO.output(relay1, 1)
        GPIO.output(relay2, 1)
        GPIO.output(relay3, 0)
        GPIO.output(relay4, 1)
        print("Relay 3 ON")
        time.sleep(2)

        GPIO.output(relay1, 1)
        GPIO.output(relay2, 1)
        GPIO.output(relay3, 1)
        GPIO.output(relay4, 0)
        print("Relay 4 ON")
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()



Step 3: Run the Program
Run the file in Thonny.


PRACTICAL NO: 08 
Aim: Oscilloscope
CMD commands:
•	sudo raspi-config (enable i2c)
•	pip install board --break-system-packages
•	sudo pip install drawnow --break-system-packages
•	sudo apt-get install -y i2c-tools python3-smbus
•	python3 -m pip install --upgrade --no-cache-dir adafruit-blinka adafruit-circuitpython-busdevice adafruit-circuitpython-ads1x15 --break-system-packages
ADS1115 Pin	Raspberry Pi Pin Number	Raspberry Pi Function
VDD				Pin 1				3.3V Power
GND				Pin 6				Ground
SDA				Pin 3				GPIO2 (SDA1 – I²C Data)
SCL				Pin 5				GPIO3 (SCL1 – I²C Clock)
Connection:

Run in cmd:
i2cdetect -y 1
You should see:
48
This confirms ADS1115 detected at address 0x48.

Open:
Raspberry Pi Menu → Programming → Thonny
Create a new file and save as:
oscilloscope.py
   
Code:
from collections import deque
import time
import board
import busio
import numpy as np
import matplotlib.pyplot as plt
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
from matplotlib.animation import FuncAnimation

# ================= SETTINGS =================
DURATION = 10                  # seconds of data
SAMPLE_RATE = 128         # ADS1115 valid: 8, 16, 32, 64, 128, 250, 475, 860
GAIN = 1                	 	# +/- 4.096V range
CHANNEL = 0            	# ADC channel (0-3)
I2C_ADDRESS = 0x48         # ADS1115 default address

# ============================================
# Setup I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize ADS1115
try:
    ads = ADS1115(i2c, address=I2C_ADDRESS)
    ads.data_rate = SAMPLE_RATE
    ads.gain = GAIN
    chan = AnalogIn(ads,CHANNEL )
    print(f"ADS1115 detected at address 0x{I2C_ADDRESS:02X}")
except Exception as e:
    print("Error initializing ADS1115:", e)
    print("Check wiring, I2C enable, and device address with 'i2cdetect -y 1'")
    exit(1)

# Setup buffer
num_samples = SAMPLE_RATE * DURATION
x = np.linspace(0, DURATION, num_samples)
y = deque([0] * num_samples, maxlen=num_samples)
# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(0, DURATION)
ax.set_ylim(-4.2, 4.2)  # for gain=1, range ±4.096V
ax.set_xlabel("Time [s]")
ax.set_ylabel("Voltage [V]")
ax.set_title("Raspberry Pi + ADS1115 Oscilloscope")
line, = ax.plot(x, y, lw=1)
# Update function
def update(frame):
    try:
        voltage = chan.voltage
    except Exception as e:
        print("I2C read error:", e)
        voltage = 0
    y.append(voltage)
    line.set_ydata(y)
    return line,
# Animation
anim = FuncAnimation(
    fig, update, frames=num_samples,
    interval=1000/SAMPLE_RATE, blit=True
)
plt.show()


           (OR)

from collections import deque
import time
import board
import busio
import numpy as np
import matplotlib.pyplot as plt
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
from matplotlib.animation import FuncAnimation

# ================= SETTINGS =================
DURATION = 10              # seconds shown on screen
SAMPLE_RATE = 128          # ADS1115: 8–860 SPS
GAIN = 1                   # ±4.096V
CHANNEL = 0                # A0
I2C_ADDRESS = 0x48
# ============================================

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)

# ADC setup
ads = ADS1115(i2c, address=I2C_ADDRESS)
ads.data_rate = SAMPLE_RATE
ads.gain = GAIN
chan = AnalogIn(ads, CHANNEL)

# Buffer
num_samples = SAMPLE_RATE * DURATION
x = np.linspace(0, DURATION, num_samples)
y = deque([0.0] * num_samples, maxlen=num_samples)

# Plot
fig, ax = plt.subplots()
ax.set_xlim(0, DURATION)
ax.set_ylim(-4.2, 4.2)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Voltage [V]")
ax.set_title("ADS1115 Software Oscilloscope")
ax.grid(True)

line, = ax.plot(x, y, lw=1)

# Update loop
def update(frame):
    try:
        voltage = chan.voltage
    except Exception:
        voltage = 0.0
    y.append(voltage)
    line.set_ydata(y)
    return line,

# Animation
ani = FuncAnimation(
    fig,
    update,
    interval=1000 / SAMPLE_RATE,
    blit=True
)

plt.show()



Run the program:
python3 oscilloscope.py

Output
A graph window will appear showing voltage vs time.
Example display:
Axis	Meaning
X-axis	Time (seconds)
Y-axis	Voltage (V)

The graph will update continuously like an oscilloscope.

If you connect a signal to A0, the waveform will change.



PRACTICAL NO: 09
Aim: Q1. Write a program to stored the data with the help of read and write operation using RFID module.
Connections:
RFID PN532        Raspberry Pi
-----------       -------------
VCC  --------->   Pin 2 (5V)
GND  --------->   Pin 6 (GND)
SDA  --------->   Pin 3 (GPIO2)
SCL  --------->   Pin 5 (GPIO3)

Channel Number	On/ Off
Channel 1		On
Channel 2		Off

Enter the following Commands: 
Command 1: sudo raspi-config (enable i2c)
Command 2: pip3 install adafruit-circuitpython-pn532 --break-system-packages

Open Thonny and create three Python files.

File 1
rfid_verify.py
File 2
rfid_write.py
File 3
rfid_read.py

Enter the following Python Programs:
Program 1(rfid_verify.py): to verify the card number
import board
import busio
from adafruit_pn532.i2c import PN532_I2C
i2c = busio.I2C(board.SCL, board.SDA)
pn532= PN532_I2C(i2c)
ic, ver, rev, support = pn532.firmware_version
print(f"successs! Found PN532 with Fireware: {ver}.{rev}")
print("Place your blue fob or white card on the red board...")
while True:
    uid= pn532.read_passive_target(timeout=0.5)
    if uid is not None:
        print(f"Found Tag! ID is : {[hex(i) for i in uid]}")

      
 
Program 2(rfid_write.py): Write the data
import board
import busio
from adafruit_pn532.i2c import PN532_I2C
# Setup I2C
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c)
print("--- NFC Writer ---")
text_to_write = input("Enter a small message to save to the card: ")
# Data must be exactly 16 bytes for a single block
# We pad the text with spaces if it's too short
data = text_to_write.ljust(16).encode() 
print("Now, place your white card on the reader...")
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is not None:
        try:
            # We use block 4 (Sector 1) to avoid messing with system blocks
            # This requires a 'default' key for Mifare cards
            key = b'\xFF\xFF\xFF\xFF\xFF\xFF'    
            if pn532.mifare_classic_authenticate_block(uid, 4, 0x60, key):
                pn532.mifare_classic_write_block(4, data)
                print(f"Success! '{text_to_write}' written to card.")
                break
            else:
                print("Authentication failed!")
        except Exception as e:
            print(f"Error: {e}")
            break
 
Program 3(rfid_read.py): Read the data
import board
import busio
from adafruit_pn532.i2c import PN532_I2C
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c)
print("Waiting for card to read stored data...")
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is not None:
        key = b'\xFF\xFF\xFF\xFF\xFF\xFF'
        if pn532.mifare_classic_authenticate_block(uid, 4, 0x60, key):
            data = pn532.mifare_classic_read_block(4)
            if data is not None:
                print(f"Stored Data: {data.decode().strip()}")
                break
Step 2 – Run Program 1 (Verify Card)
Run:
python3 rfid_verify.py
Place RFID card on sensor.
Output example:
Success! Found PN532 with Firmware: 1.6
Found Tag! ID is : ['0x4a','0x5b','0x3c','0x21']
This confirms the RFID module is working.

Step 3 – Run Program 2 (Write Data)
Run:
python3 rfid_write.py
It will ask message:
Enter a small message to save to the card:
Example:
Hello
Place RFID card on reader.
Output:
Success! 'Hello' written to card.
Now data is stored in the RFID card.

Step 4 – Run Program 3 (Read Data)
Run:
python3 rfid_read.py
Place the same card.
Output:
Stored Data: Hello
This shows the data saved in the card.

 

Q2. Write a program to display unique ID for the input data using RFID module.
Command: 
Command 1: sudo raspi-config (enable i2c)
Command 2: sudo reboot
Command 3: pip3 install adafruit-circuitpython-pn532 --break-system-packages
Command 3: sudo apt install -y libnfc-bin libnfc-dev libusb-dev libpcsclite-dev i2c-tools
Command 4: sudo nano /etc/nfc/libnfc.conf
Edit the code:
#Allow device auto-detection (default: true)
#Note: if this auto-detection is disabled, user has to set manually a device
#configuration using file or environment variable
allow_autoscan = false
#Allow intrusive auto-detection (default: false)
#Warning: intrusive auto-detection can seriously disturb other devices
#This option is not recommended, user should prefer to add manually his device.
#allow_intrusive_scan = false
#Set log level (default: error)
#Valid log levels are (in order of verbosity): 0 (none), 1 (error), 2 (info), 3 (debug)
#Note: if you compiled with --enable-debug option, the default log level is "debug"
#log_level = 1
#Manually set default device (no default)
#To set a default device, you must set both name and connstring for your device
#Note: if autoscan is enabled, default device will be the first device available in device list.

Scroll down and add these lines:
allow_autoscan = false
device.name = "PN532 over I2C" 
device.connstring = "pn532_i2c:/dev/i2c-1"

Save the file.
Ctrl + O
Enter
Ctrl + X
Command 5: i2cdetect -y 1 (optional put sudo)
Command 6: nfc-list
If module is working you will see something like:
NFC device: PN532 opened
UID (NFCID1): 04 A1 2B 6C

Open Thonny → New file.

Save as:

rfid_uid.py
Enter the following Python program in thonny.
import subprocess
import time
NAME = "Upasana"   # Put your name here
last_uid = None
try:
    while True:
        output = subprocess.getoutput("nfc-list")
        if "UID" in output:
            for line in output.splitlines():
                if "UID" in line:
                    uid = line.split(":")[1].strip().replace(" ", "")             
                    if uid != last_uid:
                        print(f"{NAME}: {uid}")
                        last_uid = uid
                    break
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped")

Paste your code and change the name if needed:
NAME = "Upasana"
Save the file.

Step 6 – Run the Program
Run the program:
python3 rfid_uid.py

Step 7 – Place RFID Card
Place the RFID card or blue keychain on the PN532 reader.
Output example:
Upasana: 04A12B6C7D
Meaning:
Name : UID of RFID card
Final Output (What you write in journal)
Upasana: 04A12B6C7D

The program displays the unique ID of the RFID tag.


Pracical No : 10
 Fingerprint Module Connections

| Fingerprint Pin | Color  | Connection to USB-TTL Converter |
| --------------- | ------ | ------------------------------- |
| 1: VCC          | Red    | Connect to **VCC (5V)**         |
| 2: GND          | Black  | Connect to **GND**              |
| 3: Tx           | Yellow | Connect to **Rx**               |
| 4: Rx           | White  | Connect to **Tx**               |

After this:

👉 Plug the USB-TTL converter into Raspberry Pi USB port.

#pip3 install pyfingerprint

Run this command:

ls /dev/ttyUSB*

You should see:

/dev/ttyUSB0

This means the fingerprint module is detected.

Create a new file finger.py in pyfingerprint directory
after creating the directory enter the command :- $ sudo nano finger.py
 
#write the code
import time 
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio 
print("Successfully imported fingerprint module" )
gpio.setwarnings(False) 
gpio.setmode(gpio.BCM) 
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0XFFFFFFFF, 0X00000000) 
except Exception as e:
    print('Exception Message :' + str(e)) 

def enrollFinger():
    print ('Enrolling Finger')
    time.sleep(3)
    print('Place Finger')
    while(f.readImage()==False):
        pass
    f.convertImage(0X01)
    result=f.searchTemplate()
    positionNumber = result[0]
    if (positionNumber >=0):
        print('Template already exists at position #'+str(positionNumber))
        time.sleep(2)
        return
    print('Remove finger')
    print('Waiting for same finger')
    time.sleep(3)
    while(f.readImage()==False):
        pass
    f.convertImage(0X02)
    if(f.compareCharacteristics()==0):
        print('Fingers do not match')
        time.sleep(2)
        return
    else:
        f.createTemplate()
        positionNumber=f.storeTemplate()
        print('Finger enrolled successfully')
        print('Stored at pos: ' +str(positionNumber))
        time.sleep(2) 
def searchFinger():
    try:
        print('Waiting for finger...')
        time.sleep(2)
        while(f.readImage()==False):
            time.sleep(4)
            return
        f.convertImage(0X01)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber==-1:
            print('No Match found')
            time.sleep(4)
            return False
        else:
            print('Found template at position ' + str(positionNumber))
            time.sleep(4)
            return True
    except Exception as e:
            print('Operation failed')
            print('Exception message: ' +str(e))
            exit(1)
    return

def deleteFinger():
    try:
        print('Waiting for finger...')
        time.sleep(2)
        while(f.readImage()==False):
            	time.sleep(4)
            	return
        f.convertImage(0X01)
        result = f.searchTemplate()
        positionNumber = result[0]
        if positionNumber==-1:
            	print('No Match found')
            	time.sleep(4)
            	return False
        else:
	if(f.deleteTemplate(positionNumber)==True):
            			print('Finger Deleted')
           	
time.sleep(4)
            return True
    except Exception as e:
            print('Operation failed')
            print('Exception message: ' +str(e))
            exit(1)
    return

time.sleep(1) 
 
print('Start') 
while True:
    	i = int(input("\nEnter :\n1.Enroll\n2.Search\n3.Delete\n4.Exit\n"));
    	if i==1:
        	enrollFinger()
    	elif i==2:
        	searchFinger()
    	elif i==3:
        	deleteFinger()
    	elif i==4:
		break
    	else:
        print("Invalid option !!!Enter Correct")


              (OR)

# fingerprint program starts

import time
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as gpio

print("Successfully imported fingerprint module")

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
except Exception as e:
    print('Exception Message: ' + str(e))
    exit(1)


def enrollFinger():
    print('Enrolling Finger')
    time.sleep(3)

    print('Place Finger')
    while f.readImage() == False:
        pass

    f.convertImage(0x01)
    result = f.searchTemplate()
    positionNumber = result[0]

    if positionNumber >= 0:
        print('Template already exists at position #' + str(positionNumber))
        time.sleep(2)
        return

    print('Remove finger')
    time.sleep(2)

    print('Place same finger again')
    while f.readImage() == False:
        pass

    f.convertImage(0x02)

    if f.compareCharacteristics() == 0:
        print('Fingers do not match')
        time.sleep(2)
        return

    f.createTemplate()
    positionNumber = f.storeTemplate()
    print('Finger enrolled successfully')
    print('Stored at position: ' + str(positionNumber))
    time.sleep(2)


def searchFinger():
    try:
        print('Waiting for finger...')
        time.sleep(2)

        while f.readImage() == False:
            pass

        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber == -1:
            print('No Match found')
            time.sleep(2)
            return False
        else:
            print('Found template at position ' + str(positionNumber))
            time.sleep(2)
            return True

    except Exception as e:
        print('Operation failed')
        print('Exception message: ' + str(e))
        exit(1)


def deleteFinger():
    try:
        print('Waiting for finger...')
        time.sleep(2)

        while f.readImage() == False:
            pass

        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]

        if positionNumber == -1:
            print('No Match found')
            time.sleep(2)
            return False
        else:
            if f.deleteTemplate(positionNumber):
                print('Finger Deleted')
                time.sleep(2)
                return True

    except Exception as e:
        print('Operation failed')
        print('Exception message: ' + str(e))
        exit(1)


time.sleep(1)

print('Start')

while True:
    i = int(input("\nEnter:\n1. Enroll\n2. Search\n3. Delete\n4. Exit\n"))

    if i == 1:
        enrollFinger()
    elif i == 2:
        searchFinger()
    elif i == 3:
        deleteFinger()
    elif i == 4:
        break
    else:
        print("Invalid option! Enter Correct")

# fingerprint program ends
 
enter the command in cmd:-
pip3 install pyfingerprint
$  python3 finger.py

Menu will appear:

1. Enroll Finger
2. Search Finger
3. Delete Finger
4. Exit
Step 7 – Enroll Fingerprint

Press:
1
Steps:
Place finger on sensor
Remove finger
Place same finger again
Output example:
Place finger on sensor...
Remove finger
Place same finger again
Finger enrolled successfully at position 0
Step 8 – Search Fingerprint

Press:
2
Place finger.
Output:
Finger matched at position 0
Step 9 – Delete Fingerprint

Press:
3
Place finger again.
Output:
Finger deleted
Final Output (Write in Journal)

✔ Fingerprint sensor successfully enrolls, searches, and deletes fingerprint templates using Raspberry Pi.



 




 






 


