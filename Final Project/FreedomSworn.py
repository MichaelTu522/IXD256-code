from machine import Pin, ADC
from m5stack import *  # import m5stack libraries
from time import *
from neopixel import NeoPixel
from micropython import const
import struct
import bluetooth
import unit  # import m5stack unit library 
import imu  # imports m5stack imu unit

imu0 = imu.IMU()
sensor_timer = ticks_ms()  # create a timer variable and save current time
button_pin1 = Pin(39, Pin.IN)
neopixel_pin = Pin(23, Pin.OUT)  # create an output on pin G21
neopixel_strip = NeoPixel(neopixel_pin, 25)
button_blue = Pin(26, Pin.IN)
button_red = Pin(32, Pin.IN)

acc_y = 0
acc_y_prev = 0

def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if (v < out_min):  
        v = out_min 
    elif (v > out_max): 
        v = out_max
    return int(v)

def ble_irq(event, data):
    global conn_handle
    if event == 1:
        print("connect")
        conn_handle = data[0]
    else:
        print("event:", event, data)


ble = bluetooth.BLE()
ble.active(1)
ble.irq(ble_irq)

UUID = bluetooth.UUID

F_READ = bluetooth.FLAG_READ
F_WRITE = bluetooth.FLAG_WRITE
F_READ_WRITE = bluetooth.FLAG_READ | bluetooth.FLAG_WRITE
F_READ_NOTIFY = bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY

ATT_F_READ = 0x01
ATT_F_WRITE = 0x02

hid_service = (
    UUID(0x1812),  # Human Interface Device
    (
        (UUID(0x2A4A), F_READ),  # HID information
        (UUID(0x2A4B), F_READ),  # HID report map
        (UUID(0x2A4C), F_WRITE),  # HID control point
        (UUID(0x2A4D), F_READ_NOTIFY, ((UUID(0x2908), ATT_F_READ),)),  # HID report / reference
        (UUID(0x2A4D), F_READ_WRITE, ((UUID(0x2908), ATT_F_READ),)),  # HID report / reference
        (UUID(0x2A4E), F_READ_WRITE),  # HID protocol mode
    ),
)

# fmt: off
HID_REPORT_MAP = bytes([
    0x05, 0x01,     # Usage Page (Generic Desktop)
    0x09, 0x06,     # Usage (Keyboard)
    0xA1, 0x01,     # Collection (Application)
    0x85, 0x01,     #     Report ID (1)
    0x75, 0x01,     #     Report Size (1)
    0x95, 0x08,     #     Report Count (8)
    0x05, 0x07,     #     Usage Page (Key Codes)
    0x19, 0xE0,     #     Usage Minimum (224)
    0x29, 0xE7,     #     Usage Maximum (231)
    0x15, 0x00,     #     Logical Minimum (0)
    0x25, 0x01,     #     Logical Maximum (1)
    0x81, 0x02,     #     Input (Data, Variable, Absolute); Modifier byte
    0x95, 0x01,     #     Report Count (1)
    0x75, 0x08,     #     Report Size (8)
    0x81, 0x01,     #     Input (Constant); Reserved byte
    0x95, 0x05,     #     Report Count (5)
    0x75, 0x01,     #     Report Size (1)
    0x05, 0x08,     #     Usage Page (LEDs)
    0x19, 0x01,     #     Usage Minimum (1)
    0x29, 0x05,     #     Usage Maximum (5)
    0x91, 0x02,     #     Output (Data, Variable, Absolute); LED report
    0x95, 0x01,     #     Report Count (1)
    0x75, 0x03,     #     Report Size (3)
    0x91, 0x01,     #     Output (Constant); LED report padding
    0x95, 0x06,     #     Report Count (6)
    0x75, 0x08,     #     Report Size (8)
    0x15, 0x00,     #     Logical Minimum (0)
    0x25, 0x65,     #     Logical Maximum (101)
    0x05, 0x07,     #     Usage Page (Key Codes)
    0x19, 0x00,     #     Usage Minimum (0)
    0x29, 0x65,     #     Usage Maximum (101)
    0x81, 0x00,     #     Input (Data, Array); Key array (6 bytes)
    0xC0,           # End Collection
])
# fmt: on

# register services
ble.config(gap_name="FreedormSworn")
handles = ble.gatts_register_services((hid_service,))
print(handles)
h_info, h_hid, _, h_rep, h_d1, _, h_d2, h_proto = handles[0]

# set initial data
ble.gatts_write(h_info, b"\x01\x01\x00\x02")  # HID info: ver=1.1, country=0, flags=normal
ble.gatts_write(h_hid, HID_REPORT_MAP)  # HID report map
ble.gatts_write(h_d1, struct.pack("<BB", 1, 1))  # report: id=1, type=input
ble.gatts_write(h_d2, struct.pack("<BB", 1, 2))  # report: id=1, type=output
ble.gatts_write(h_proto, b"\x01")  # protocol mode: report

# advertise
adv = (
    b"\x02\x01\x06"
    b"\x03\x03\x12\x18"  # complete list of 16-bit service UUIDs: 0x1812
    b"\x03\x19\xc1\x03"  # appearance: keyboard
    b"\x0c\x09MP-keyboard"  # complete local name
)
conn_handle = None
ble.gap_advertise(100_000, adv)

'''
# key codes:
0x04	Keyboard a and A
...
0x1D	Keyboard z and Z
0x1E	Keyboard 1 and !
0x1F	Keyboard 2 and @
0x20	Keyboard 3 and #
0x21	Keyboard 4 and $
0x22	Keyboard 5 and %
0x23	Keyboard 6 and ^
0x24	Keyboard 7 and &
0x25	Keyboard 8 and *
0x26	Keyboard 9 and (
0x27	Keyboard 0 and )
0x28	Keyboard Return (ENTER)
0x29	Keyboard ESCAPE
0x2A	Keyboard DELETE (Backspace)
0x2B	Keyboard Tab
0x2C	Keyboard Spacebar
0x2D	Keyboard - and (underscore)
0x2E	Keyboard = and +
0x2F	Keyboard [ and {
0x30	Keyboard ] and }
0x31	Keyboard \ and |
0x32	Keyboard Non-US # and ~
0x33	Keyboard ; and :
0x34	Keyboard ' and "
0x35	Keyboard Grave Accent and Tilde
0x36	Keyboard, and <
0x37	Keyboard . and >
0x38	Keyboard / and ?
0x39	Keyboard Caps Lock
0x3A	Keyboard F1
0x3B	Keyboard F2
0x3C	Keyboard F3
0x3D	Keyboard F4
0x3E	Keyboard F5
0x3F	Keyboard F6
0x40	Keyboard F7
0x41	Keyboard F8
0x42	Keyboard F9
0x43	Keyboard F10
0x44	Keyboard F11
0x45	Keyboard F12
0x46	Keyboard PrintScreen
0x47	Keyboard Scroll Lock
0x48	Keyboard Pause
0x49	Keyboard Insert
0x4A	Keyboard Home
0x4B	Keyboard PageUp
0x4C	Keyboard Delete Forward
0x4D	Keyboard End
0x4E	Keyboard PageDown
0x4F	Keyboard RightArrow
0x50	Keyboard LeftArrow
0x51	Keyboard DownArrow
0x52	Keyboard UpArrow
0x53	Keypad Num Lock and Clear
0x54	Keypad /
0x55	Keypad *
0x56	Keypad -
0x57	Keypad +
0x58	Keypad ENTER
0x59	Keypad 1 and End
0x5A	Keypad 2 and Down Arrow
0x5B	Keypad 3 and PageDn
0x5C	Keypad 4 and Left Arrow
0x5D	Keypad 5
0x5E	Keypad 6 and Right Arrow
0x5F	Keypad 7 and Home
0x60	Keypad 8 and Up Arrow
0x61	Keypad 9 and PageUp
0x62	Keypad 0 and Insert
0x63	Keypad . and Delete
'''
# once connected use the following to send reports
def send_char(char):
    if char == " ":
        mod = 0
        code = 0x2C
    elif ord("a") <= ord(char) <= ord("z"):
        mod = 0
        code = 0x04 + ord(char) - ord("a")
    elif ord("A") <= ord(char) <= ord("Z"):
        mod = 2
        code = 0x04 + ord(char) - ord("A")
    elif char == "0":
        mod = 0
        code = 0x27
    elif ord("1") <= ord(char) <= ord("9"):
        mod = 0
        code = 0x1E + ord(char) - ord("1")
    else:
        assert 0
    ble.gatts_notify(conn_handle, h_rep, struct.pack("8B", mod, 0, code, 0, 0, 0, 0, 0))
    ble.gatts_notify(conn_handle, h_rep, b"\x00\x00\x00\x00\x00\x00\x00\x00")


def send_str(st):
    for c in st:
        send_char(c)


E_Attack1 = [
    0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0,0,0,0
]

E_Attack2 = [
    0,0,0,0,0,0,0,2,2,2,2,3,3,3,2,2,2,2,0,0,0,0,0,0,0
]

E_Attack3 = [
    1,1,1,1,1,1,1,2,2,2,2,3,3,3,2,2,2,2,1,1,1,1,1,1,1
]

Q_Attack1 = [
    0,0,0,0,0,0,0,0,0,0,0,6,6,6,0,0,0,0,0,0,0,0,0,0,0
]

Q_Attack2 = [
    0,0,0,0,0,0,0,5,5,5,5,6,6,6,5,5,5,5,0,0,0,0,0,0,0
]

Q_Attack3 = [
    4,4,4,4,4,4,4,5,5,5,5,6,6,6,5,5,5,5,4,4,4,4,4,4,4
]

Normal_Attack = [
    6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6
]

red_color = (255,0,100)
orange_color = (255, 20, 0)
yellow_color = (255, 255, 0)
blue_color =(150, 0, 255)
sky_color = (0, 0, 255)
cyan_color = (0,255,255)
dot_color = (0,0,0)


# define a function to get color for a pixel:
def get_pixel_color(n):
    if(n == 1):
        return red_color
    elif(n == 2):
        return orange_color
    elif(n == 3):
        return yellow_color
    if(n == 4):
        return blue_color
    elif(n == 5):
        return sky_color
    elif(n == 6):
        return cyan_color
    else:
        return dot_color

def display_digit(m):
    for i in range(25):
            if(m == 1):
                neopixel_strip[i] = get_pixel_color(E_Attack1[i])
            if(m == 2):
                neopixel_strip[i] = get_pixel_color(E_Attack2[i])
            if(m == 3):
                neopixel_strip[i] = get_pixel_color(E_Attack3[i])
            if(m == 4):
                neopixel_strip[i] = get_pixel_color(Q_Attack1[i])
            if(m == 5):
                neopixel_strip[i] = get_pixel_color(Q_Attack2[i])
            if(m == 6):
                neopixel_strip[i] = get_pixel_color(Q_Attack3[i])
            if(m == 7):
                neopixel_strip[i] = get_pixel_color(Normal_Attack[i])                           
    neopixel_strip.write()





while True:
    if (button_blue.value() == 0):
                if (conn_handle != None):
                    send_char('0')
                    print('Attack!')
                    display_digit(7)
                    sleep_ms(100)
    if (button_red.value() == 0):
                if (conn_handle != None):
                    send_char('e')
                    print('E Attack')
                    display_digit(1)
                    sleep_ms(200) 
                    display_digit(2)
                    sleep_ms(200) 
                    display_digit(3)
                    sleep_ms(700) 

    if(ticks_ms() > sensor_timer + 100):
                    
        if (button_pin1.value() == 1):
                        acc_x = imu0.acceleration[0]
                        acc_y_prev = acc_y  # save the last acc_y value
                        acc_y = imu0.acceleration[1]  # get the new acc_y value
                        acc_z = imu0.acceleration[2]
                        #print("y is " + str(acc_y))
                        acc_y_diff = acc_y - acc_y_prev
                        print('acc_y difference: ', acc_y_diff)
                        color_value_255 = map_value(acc_y_diff, -2, 2, -10, 10)
                        if(acc_y_diff > 0.5 or acc_y_diff < -0.5):
                            if (conn_handle != None):
                                print('Attack!')
                                send_char('0')
                                sleep_ms(300)
                        if(color_value_255 > 0):
                            color_value_255 == 0 - color_value_255
                            print(color_value_255)
                        for pixel_index in range(25):
                            neopixel_strip[pixel_index] = (0, color_value_255, color_value_255)
                        neopixel_strip.write()
        elif (button_pin1.value() == 0):
                    send_char('q')
                    print('Q Attack') 
                    display_digit(4)
                    sleep_ms(200) 
                    display_digit(5)
                    sleep_ms(200) 
                    display_digit(6)
                    sleep_ms(700)  
        sensor_timer = ticks_ms()