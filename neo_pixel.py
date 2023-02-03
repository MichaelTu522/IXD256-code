from neopixel import NeoPixel
from time import *
from machine import Pin

neo_pin = Pin(26, Pin.OUT)
neo_strip = NeoPixel(neo_pin, 30)#neo_strip is assign this neopixel a name. the number just type in and it is the amount you use

'''neo_strip[0] = (255, 0, 0) #use list, index of the pixel I want to change'''

while True:
    for i in range (51):
        for pixel_index in range (16):
            neo_strip[pixel_index] = (5*i, 5*i, 255-i)
            neo_strip.write() #send data to the strip
        sleep_ms(10)
    sleep_ms(500)
    for i in range (255):
        for pixel_index in range (16):
            neo_strip[pixel_index] = (255-5*i, 255-5*i, i)
            neo_strip.write() #send data to the strip
        sleep_ms(10)
    sleep_ms(10)
