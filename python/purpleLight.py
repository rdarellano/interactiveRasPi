import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)

GPIO.output(15,1)
GPIO.output(16,1)
GPIO.output(40,1)
GPIO.output(37,1)
GPIO.output(22,1)
GPIO.output(13,1)
GPIO.output(33,1)
GPIO.output(32,1)

time.sleep(3)
GPIO.cleanup()

