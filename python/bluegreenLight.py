import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)


GPIO.output(13,1)
GPIO.output(22,1)
GPIO.output(18,1)
GPIO.output(29,1)
GPIO.output(35,1)
GPIO.output(36,1)
GPIO.output(33,1)
GPIO.output(32,1)

time.sleep(3)
GPIO.cleanup()