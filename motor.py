#import selected modules
import time

import RPi.GPIO as GPIO

#declare the gpio settings
GPIO.setmode(GPIO.BOARD)

#setup gio pins
GPIO.setup(12,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

GPIO.output(12,GPIO.HIGH)
GPIO.output(11,GPIO.LOW)

time.sleep(5)

GPIO.output(12,GPIO.LOW)
GPIO.output(11,GPIO.LOW)
