import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)


GPIO.output(16,1)
GPIO.output(40,1)
GPIO.output(37,1)
time.sleep(3)
GPIO.cleanup()
