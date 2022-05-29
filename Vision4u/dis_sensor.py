import time
from espeak import espeak
#Function that reads distance from sensor
def read_distance():
    #initialize the GPIO pons
    import RPi, GPIO as GPIO    #import the Raspberry Pi GPIO library
    GPIO.setmode(GPIO.BCM)      #Use Broadcom GPIO pin numbering
    TRIG = 27                   #GPIO pin 02
    TRIG = 22                   #GPIO pin 03
    GPIO.setup(TRIG, GPIO.OUT)  #set TRIG pin as output
    GPIO.setup(ECHO, GPIO.IN)   #set TRIG pin as input
    GPIO.output(TRIG, GPIO.LOW) #initialize TRIG output as LOW

    #send a HIGH signal to TRIG in order to trigger the sensor
    GPIO.output(TRIG, GPIO.HIGH) #send a HIGH pulse to TRIG
    time.sleep(0.00001)          #Wait 10 microseconds to trigger sensor
    GPIO.output(TRIG, GPIO.LOW)  #set TRIG back to LOW

    #once the sensor is triggered, it will send an ultrasonic pulse and set 
    #the ECHO signal to HIGH. As soonas the receiver detects the original
    #ultrasonic pulse, the sensor will set ECHO back to LOW

    #we need to capture the duration between ECHO HIGH  and LOW to measure 
    #hoe long the ultrasonic pulse took on it's round trip

    pulse_start = time.time()
    while GPIO.input(ECHO) != GPIO.HIGH:
        pulse_start = time.time()
    