import math
import time

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

lcd.show_cursor(False)

lcd.message ('Welcome to Text\nAdventure V1.0!')
time.sleep(3.0)
lcd.clear()

lcd.message ('You wake up in a\nforest.)
time.sleep(2.5)
lcd.clear()

lcd.message('What do you do?')
time.sleep(1)
lcd.clear()
lcd.message('Select to choose\nDir to choose')
lcd.clear()

if lcd.is_pressed(UP)
