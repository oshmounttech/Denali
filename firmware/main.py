import time
import board
import busio
import adafruit_tsl2591
from microcontroller import Pin

def is_hardware_I2C(scl, sda):
    try:
        p = busio.I2C(scl, sda)
        p.deinit()
        return True
    except ValueError:
        return False
    except RuntimeError:
        return True

def get_unique_pins():
    exclude = ['NEOPIXEL', 'APA102_MOSI', 'APA102_SCK']
    pins = [pin for pin in [
        getattr(board, p) for p in dir(board) if p not in exclude]
            if isinstance(pin, Pin)]
    unique = []
    for p in pins:
        if p not in unique:
            unique.append(p)
    return unique


for scl_pin in get_unique_pins():
    for sda_pin in get_unique_pins():
        if scl_pin is sda_pin:
            continue
        if is_hardware_I2C(scl_pin, sda_pin):
            print("SCL pin:", scl_pin, "\t SDA pin:", sda_pin)

i2c = board.I2C()
leftKeyboard = 20
rightKeyboard = 22
arrowKeyboard = 24
numberKeyboard = 26

while not i2c.try_lock():
    pass

print("I2C addresses found:", [hex(device_address) for device_address in i2c.scan()])

i2c.unlock()

tsl2591 = adafruit_tsl2591.TSL2591(i2c)

while True:
    print("Lux:", tsl2591.lux)
    time.sleep(0.5)