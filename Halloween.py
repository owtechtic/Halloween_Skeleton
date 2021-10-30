import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
#identify GPIO pins
speaker = 14
eyes = 15
pedal = 18
Ccw = 23
Cw = 24
TRIG =25
ECHO = 8

GPIO.setup(speaker ,GPIO.OUT)
GPIO.setup(eyes ,GPIO.OUT)
GPIO.setup(pedal ,GPIO.IN)
GPIO.setup(Cw, GPIO.OUT)
GPIO.setup(Ccw, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

input = GPIO.input(pedal)
c=0
#look for pedal loop
while True:
    if (GPIO.input(pedal)):
        GPIO.output(eyes, GPIO.HIGH)
        GPIO.output(speaker, GPIO.HIGH)
        if c==0:
            os.system('mpg321 /home/pi/Desktop/skelly/SK1.mp3 &')
        if c==1:
            os.system('mpg321 /home/pi/Desktop/skelly/SK2.mp3 &')
        if c==2:
            os.system('mpg321 /home/pi/Desktop/skelly/SK3.mp3 &')
        if c==3:
            os.system('mpg321 /home/pi/Desktop/skelly/SK4.mp3 &')
        c=c+1
        if c==4:
            c=0
        time.sleep(6)
        os.system('mpg321 /home/pi/Desktop/skelly/Candy.mp3 &')
        time.sleep(4)
       
        GPIO.output(speaker, GPIO.LOW)
        GPIO.output(eyes, GPIO.LOW)
        GPIO.output(Cw,GPIO.HIGH)         
        GPIO.output(Ccw,GPIO.LOW) 
        
        
        distance=1000
        C2=0
        #Look for candy in sensor 
        while distance > 3.7:
            GPIO.output(TRIG, GPIO.LOW)
            time.sleep(.5)
            GPIO.output(TRIG, GPIO.HIGH)
            time.sleep(.1)
            GPIO.output(TRIG, GPIO.LOW)
            while GPIO.input(ECHO)==0:
                pulse_start=time.time()
            while GPIO.input(ECHO)==1:
                pulse_end=time.time()
            pulse_duration = pulse_end-pulse_start
            distance = pulse_duration *17150
            distance = round(distance,2)
            print(distance)
            #if candy is not seen after a few loops wiggle the plate
            if C2>10:
                GPIO.output(Cw,GPIO.LOW)         
                GPIO.output(Ccw,GPIO.LOW)
                time.sleep(.5)
                GPIO.output(Cw,GPIO.LOW)         
                GPIO.output(Ccw,GPIO.HIGH)
                time.sleep(1.5)
                GPIO.output(Cw,GPIO.LOW)         
                GPIO.output(Ccw,GPIO.LOW)
                time.sleep(.5)
                GPIO.output(Cw, GPIO.HIGH)
                GPIO.output(Ccw, GPIO.LOW)
                C2=0
            C2=C2+1
            print(C2)
        c1 = 0
        time.sleep(1)
        GPIO.output(Cw,GPIO.LOW)         
        GPIO.output(Ccw,GPIO.LOW)
        time.sleep(1)
        GPIO.output(Cw,GPIO.LOW)         
        GPIO.output(Ccw,GPIO.HIGH)
        time.sleep(2.5)
        GPIO.output(eyes, GPIO.LOW)
        GPIO.output(Cw,GPIO.LOW)         
        GPIO.output(Ccw,GPIO.LOW)