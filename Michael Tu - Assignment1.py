from neopixel import NeoPixel
from time import *
from machine import Pin
from m5stack import *


neo_board = Pin(27, Pin.OUT)
neo_pin = Pin(26, Pin.OUT)
neo_strip2 = NeoPixel(neo_board, 25)
neo_strip = NeoPixel(neo_pin, 30)#neo_strip is assign this neopixel a name. the number just type in and it is the amount you use
button_pin = Pin(39, Pin.IN, Pin.PULL_UP) #create Button input on pin G26 (yellow wire)

'''neo_strip[0] = (255, 0, 0) #use list, index of the pixel I want to change'''

while True:
    if(button_pin.value() == 0):
        for i in range (51):
            for pixel_index in range (2):
                neo_strip[pixel_index] = (5*i, 0, 5*i)
                neo_strip.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (2):
                neo_strip[pixel_index] = (255-5*i, 0, 255-5*i)
                neo_strip.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (4):
                neo_strip[pixel_index] = (5*i, 5*i, 0)
                neo_strip.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (4):
                neo_strip[pixel_index] = (255-5*i, 255-5*i, 0)
                neo_strip.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (8):
                neo_strip[pixel_index] = (0, 5*i, 5*i)
                neo_strip.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (8):
                neo_strip[pixel_index] = (0, 255-5*i, 255-5*i)
                neo_strip.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
    else: 
        for i in range (51):
            for pixel_index in range (5):
                neo_strip2[pixel_index] = (5*i, 0, 5*i)
                neo_strip2.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (5):
                neo_strip2[pixel_index] = (255-5*i, 0, 255-5*i)
                neo_strip2.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (15):
                neo_strip2[pixel_index] = (5*i, 5*i, 0)
                neo_strip2.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (15):
                neo_strip2[pixel_index] = (255-5*i, 255-5*i, 0)
                neo_strip2.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (25):
                neo_strip2[pixel_index] = (0, 5*i, 5*i)
                neo_strip2.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)
        for i in range (51):
            for pixel_index in range (25):
                neo_strip2[pixel_index] = (0, 255-5*i, 255-5*i)
                neo_strip2.write() #send data to the strip
            sleep_ms(10)
        sleep_ms(10)

