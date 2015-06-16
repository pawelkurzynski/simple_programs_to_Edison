#!/usr/bin/env python
#
# Edison Example for using the Grove - LCD RGB Backlight (http://www.seeedstudio.com/wiki/Grove_-_LCD_RGB_Backlight)


import time,sys
import mraa


# this device has two I2C addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

bus = mraa.I2c(0)
#bus.address(0x62)


# set backlight to (R,G,B) (values from 0..255 for each)
def setRGB(r,g,b):
    bus.address(0x62)
    bus.writeReg(0,0)
    bus.writeReg(1,0)
    bus.writeReg(0x08,0xaa)
    bus.writeReg(0x04,r)
    bus.writeReg(0x03,g)
    bus.writeReg(0x02,b)

# send command to display (no need for external use)
def textCommand(cmd):
    bus.address(0x3e)
    bus.writeReg(0x80,cmd)

# set display text \n for second line(or auto wrap)
def setText(text):
    textCommand(0x01) # clear display
    time.sleep(.05)
    textCommand(0x08 | 0x04) # display on, no cursor
    textCommand(0x28) # 2 lines
    time.sleep(.05)
    count = 0
    row = 0
    for c in text:
        if c == '\n' or count == 16:
            count = 0
            row += 1
            if row == 2:
                break
            textCommand(0xc0)
            if c == '\n':
                continue
        count += 1
        bus.address(0x3e)
        bus.writeReg(0x40,ord(c))


# example code
if __name__=="__main__":
    setText("Hello world\nThis is an LCD test")
    setRGB(0,128,64)
    for c in range(0,255):
        setRGB(c,255-c,0)
        time.sleep(0.01)
    setRGB(0,255,0)
    setText("Bye bye, this should wrap onto next line")
