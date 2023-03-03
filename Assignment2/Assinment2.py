from m5stack import *  # import m5stack libraries
import unit  # import m5stack unit library 
import imu  # imports m5stack imu unit
from neopixel import NeoPixel
from time import *
from machine import Pin


imu0 = imu.IMU()
button_pin = Pin(32, Pin.IN)  # configure input on pin G32 (white wire)
neopixel_pin = Pin(27, Pin.OUT)  # create an output on pin G26
neopixel_strip = NeoPixel(neopixel_pin, 25)


sensor_timer = ticks_ms()  # create a timer variable and save current time
program_state = 'OFF' # variable to keep track of program state

digit_prepare1 = [
    3,3,3,3,3,
    3,3,3,3,3,
    3,3,2,3,3,
    3,3,3,3,3,
    3,3,3,3,3
]

digit_prepare2 = [
    3,3,3,3,3,
    3,2,2,2,3,
    3,2,3,2,3,
    3,2,2,2,3,
    3,3,3,3,3
]

digit_prepare3 = [
    2,2,2,2,2,
    2,3,3,3,2,
    2,3,3,3,2,
    2,3,3,3,2,
    2,2,2,2,2

    
]

digit_end1 = [
    3,3,3,3,3,
    3,2,2,2,3,
    3,2,3,2,3,
    3,2,2,2,3,
    3,3,3,3,3
]

digit_end2 = [
    3,3,3,3,3,
    3,3,3,3,3,
    3,3,3,3,3,
    3,3,3,3,3,
    3,3,3,3,3
]

#this is for preparation and the end

digit_1 = [
    0,0,0,0,1,
    0,0,0,1,1,
    0,0,3,1,1,
    0,1,1,1,1,
    1,1,1,1,1
]

digit_2 = [
    0,0,0,0,0,
    0,0,0,0,1,
    0,0,3,1,1,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_3 = [
    0,0,0,0,0,
    0,0,0,0,0,
    1,1,3,1,1,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_4 = [
    0,0,0,0,0,
    1,0,0,0,0,
    1,1,3,0,0,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_5 = [
    1,0,0,0,0,
    1,1,0,0,0,
    1,1,3,0,0,
    1,1,1,1,0,
    1,1,1,1,1
]

digit_6 = [
    0,0,1,1,1,
    0,1,1,1,1,
    1,1,3,1,1,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_7 = [
    0,0,0,0,1,
    0,1,1,1,1,
    1,1,3,1,1,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_8 = [
    0,0,0,0,0,
    1,1,1,1,1,
    1,1,3,1,1,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_9 = [
    1,0,0,0,0,
    1,1,1,1,0,
    1,1,3,1,1,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_10 = [
    1,1,1,0,0,
    1,1,1,1,0,
    1,1,3,1,1,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_11 = [
    0,0,0,0,0,
    0,0,0,0,1,
    0,0,3,1,1,
    0,0,1,1,1,
    0,1,1,1,1
]

digit_12 = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,3,0,1,
    0,1,1,1,1,
    0,1,1,1,1
]

digit_13 = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,3,0,0,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_14 = [
    0,0,0,0,0,
    0,0,0,0,0,
    1,0,3,0,0,
    1,1,1,0,0,
    1,1,1,1,1
]

digit_15 = [
    0,0,0,0,0,
    1,0,0,0,0,
    1,1,3,0,0,
    1,1,1,0,0,
    1,1,1,1,0
]

digit_16 = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,3,0,0,
    1,0,0,0,0,
    1,1,0,0,0
]

digit_17 = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,3,0,0,
    1,0,0,0,0,
    1,1,1,1,0
]

digit_18 = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,3,0,0,
    0,0,0,0,0,
    1,1,1,1,1
]

digit_19 = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,3,0,0,
    0,0,0,0,1,
    0,1,1,1,1
]

digit_20 = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,3,0,0,
    0,0,0,0,1,
    0,0,0,1,1
]

digit_21 = [
    1,1,1,1,1,
    1,1,1,1,1,
    1,1,3,1,1,
    1,1,1,1,1,
    1,1,1,1,1
]

digit_22 = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,3,0,0,
    0,0,0,0,0,
    0,0,0,0,0
]


# define some colors:
sky_color = (0,0,205)
ground_color = (170,79,19)
red_color = (255 ,0 ,0)
dot_color = (0,0,0)



# define a function to get color for a pixel:
def get_pixel_color(n):
    if(n == 0):
        return sky_color
    elif(n == 1):
        return ground_color
    elif(n == 2):
        return red_color
    else:
        return dot_color
    
# define a function to display a digit:
def display_digit(m):
    for i in range(25):
        if(m == 31):
            neopixel_strip[i] = get_pixel_color(digit_prepare1[i])
        elif(m == 32):
            neopixel_strip[i] = get_pixel_color(digit_prepare2[i])
        elif(m == 33):
            neopixel_strip[i] = get_pixel_color(digit_prepare3[i])
        elif(m == 34):
            neopixel_strip[i] = get_pixel_color(digit_end1[i])
        elif(m == 35):
            neopixel_strip[i] = get_pixel_color(digit_end2[i])
        #for preparation
        elif(m == 3):
            neopixel_strip[i] = get_pixel_color(digit_3[i])
        elif(m == 1):
            neopixel_strip[i] = get_pixel_color(digit_2[i])
        elif(m == 2):
            neopixel_strip[i] = get_pixel_color(digit_2[i])
        elif(m == 4):
            neopixel_strip[i] = get_pixel_color(digit_4[i])
        elif(m == 5):
            neopixel_strip[i] = get_pixel_color(digit_5[i])
        elif(m == 6):
            neopixel_strip[i] = get_pixel_color(digit_6[i])
        elif(m == 7):
            neopixel_strip[i] = get_pixel_color(digit_7[i])
        elif(m == 8):
            neopixel_strip[i] = get_pixel_color(digit_8[i])
        elif(m == 9):
            neopixel_strip[i] = get_pixel_color(digit_9[i])
        elif(m == 10):
            neopixel_strip[i] = get_pixel_color(digit_10[i])
        elif(m == 11):
            neopixel_strip[i] = get_pixel_color(digit_11[i])
        elif(m == 12):
            neopixel_strip[i] = get_pixel_color(digit_12[i])
        elif(m == 13):
            neopixel_strip[i] = get_pixel_color(digit_13[i])
        elif(m == 14):
            neopixel_strip[i] = get_pixel_color(digit_14[i])
        elif(m == 15):
            neopixel_strip[i] = get_pixel_color(digit_15[i])
        elif(m == 16):
            neopixel_strip[i] = get_pixel_color(digit_16[i])
        elif(m == 17):
            neopixel_strip[i] = get_pixel_color(digit_17[i])
        elif(m == 18):
            neopixel_strip[i] = get_pixel_color(digit_18[i])
        elif(m == 19):
            neopixel_strip[i] = get_pixel_color(digit_19[i])
        elif(m == 20):
            neopixel_strip[i] = get_pixel_color(digit_20[i])
        elif(m == 21):
            neopixel_strip[i] = get_pixel_color(digit_21[i])
        elif(m == 22):
            neopixel_strip[i] = get_pixel_color(digit_22[i])
    neopixel_strip.write()


while True:
    if(ticks_ms() > sensor_timer + 100):

        imu_x = imu0.acceleration[0]
        imu_z = imu0.acceleration[2]

        if(program_state == 'OFF'):
            if(button_pin.value() == 0):  # button_pin is low
                print('Starting the plane..')
                display_digit(31)
                sleep_ms(200)
                display_digit(32)
                sleep_ms(200)
                display_digit(33)
                sleep_ms(200)
                program_state = 'START'
                print('change program_state to ' + program_state)
        elif(program_state == 'START'):

            '''if(analog_val_adjusted < 0):
                analog_val_adjusted = 0
            analog_val_25 = map_value(analog_val_adjusted, 0, 4095, 0, 25)
            '''
            print( 'z is ' + str(imu_z))
            #print(analog_val_25)
            #print(f'{analog_val} {calibration_val}')
            #print('analog_val = ' + str(analog_val))
            #print(f'analog_val = {analog_val}')
            sleep_ms(100)
            if(0.2 > imu_x > -0.2):#middle
                if(-0.4 > imu_z > -0.7):
                    display_digit(3)
                elif(-0.1 > imu_z > -0.4):
                    display_digit(13)
                elif(-0.7 > imu_z > -0.9):
                    display_digit(8)
                elif(imu_z < -0.9):
                    display_digit(21)
                elif(-0.1 <imu_z < 0.3):
                    display_digit(18)
                elif(imu_z > 0.3):
                    display_digit(22)
            elif(-0.6 < imu_x < -0.2):#left1
                if(-0.4 > imu_z > -0.7):#normal
                    display_digit(2)
                elif(-0.1 > imu_z > -0.4):#up1
                    display_digit(12)
                elif(-0.7 > imu_z > -0.9):#down1
                    display_digit(7)
                elif(imu_z < -0.9):#down2
                    display_digit(21)
                elif(-0.1 <imu_z < 0.3):#up2
                    display_digit(17)
                elif(imu_z > 0.3):#up3
                    display_digit(22)
            elif(0.6 > imu_x > 0.2):#right1
                if(-0.4 > imu_z > -0.7):#normal
                    display_digit(4)
                elif(-0.1 > imu_z > -0.4):#up1
                    display_digit(14)
                elif(-0.7 > imu_z > -0.9):#down1
                    display_digit(9)
                elif(imu_z < -0.9):#down2
                    display_digit(21)
                elif(-0.1 <imu_z < 0.3):#up2
                    display_digit(19)
                elif(imu_z > 0.3):#up3
                    display_digit(22)
            elif(imu_x > 0.6):#right2
                if(-0.4 > imu_z > -0.7):#normal
                    display_digit(5)
                elif(-0.1 > imu_z > -0.4):#up1
                    display_digit(15)
                elif(-0.7 > imu_z > -0.9):#down1
                    display_digit(10)
                elif(imu_z < -0.9):#down2
                    display_digit(21)
                elif(-0.1 <imu_z < 0.3):#up2
                    display_digit(20)
                elif(imu_z > 0.3):#up3
                    display_digit(22)
            elif(imu_x < -0.6):#left2
                if(-0.4 > imu_z > -0.7):#normal
                    display_digit(1)
                elif(-0.1 > imu_z > -0.4):#up1
                    display_digit(11)
                elif(-0.7 > imu_z > -0.9):#down1
                    display_digit(16)
                elif(imu_z < -0.9):#down2
                    display_digit(21)
                elif(-0.1 <imu_z < 0.3):#up2
                    display_digit(16)
                elif(imu_z > 0.3):#up3
                    display_digit(22)
            
            '''
            if(2448 > analog_val > 1648):
                display_digit(3)
            elif(1648 > analog_val > 848):
                display_digit(2)
            elif(3248 > analog_val > 2448):
                display_digit(4)
            elif(analog_val < 848):
                display_digit(1)
            elif(analog_val > 3248):
                display_digit(5)
            '''

        if(button_pin.value() == 0):  # button_pin is low
            print('Shut down Engines..')
            display_digit(34)
            sleep_ms(100)
            display_digit(31)
            sleep_ms(100)
            display_digit(35)
            program_state = 'OFF'


        #sleep_ms(100)
        sensor_timer = ticks_ms()  # update sensor timer