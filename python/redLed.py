__author__ = 'Pawel'
import mraa
import time

led = mraa.Gpio(2)
led.dir(mraa.DIR_OUT)

while True:
    led.write(1)
    time.sleep(0.5)
    led.write(0)
    time.sleep(0.5)

