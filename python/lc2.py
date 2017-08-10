from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=20, en=6,
                       d4=5, d5=7, d6=8, d7=11,
                       cols=16, lines=2)
lcd.clear()
# display text on LCD display \n = new line
lcd.message("Richard's Pi\n ENTER TEXT HERE!")
sleep(3)
# scroll text off display
for x in range(0, 16):
    lcd.move_right()
    sleep(.1)
sleep(3)
# scroll text on display
for x in range(0, 16):
    lcd.move_left()
    sleep(.1)
