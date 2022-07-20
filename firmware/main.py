import time
import board

i2c = board.I2C()
i2c.scan()

leftKeyboard = 20
rightKeyboard = 22
arrowKeyboard = 24
numberKeyboard = 26

