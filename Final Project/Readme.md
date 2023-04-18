# Michael Tu - Final Project
## Freedom Sworn & Magic Glove


## Introduction   

In the final project, there was three different ideas in my initial thoughts:
### A pair of Magic Gloves which can vibrate when receiving different feedback
![Magic Gloves](../Final%20Project/Images/MagicGloves.png) 
### A Magic Wand which could use motion to control different smart furnitures
![Magic Wand](../Final%20Project/Images/MagicWand.png) 
### A Music Keyboard to control the character playing instruments in the game "Genshin Impact"
![Magic Keyboard](../Final%20Project/Images/MagicKeyboard.png) 

After the first round of critic, I was thinking about:
## Why not just combine all of them together?

### That's why I came up with both of my final ideas:
## A sword and A Glove to play the game "Genshin Impact"
![Final Concept Sketch](../Final%20Project/Images/FinalConceptSketch.png) 

For the sword, I want it to be the sword used by my favorite male character: Kaedehara Kazuha
![Kazuha and his sword](../Final%20Project/Images/Kazuha.png) 
And the name of the sword is "Freedom Sworn"

For the glove, I still want to combine the vibration feedback. Moreover, by adding sensors like Bent Sensor and Pressure Sensor, I can make the glove control multiple motions like Walking, Run, and Jump, which could be useful when playing the game.

## Implementation   
During my development, I was thinking about how I could apply all those ingredients in all the concept I had, so I just tried to apply all of them.

### The Hardware Part includes:
* 2 Atom Matrix (Using their 25-Pixel Screen and 3-Axis Accelerator Mainly)
* A bent / Pressure Sensor for The Magic Glove
* A Pressure Sensor for The Magic Glove
* A LED Light Strip for The FreedomSworn
* A Dual-Button Pack for The FreedomSworn

### The Software Part Includes:
* Circuit Python

### The Integrations Include:
* UIFlow
* Bluetooth
* NeoPixel
* IMU

### The Enclosure Part Includes
* Laser Cut Sword(Self Sketch and Redesign from Genshin Impact)
* A Left-Hand Anqier Winter Glove

## Schematic diagram

# The Diagram for FreedomSworn 
![Diagram for FreedomSworn](../Final%20Project/Images/FreedomSwornDiagram.png) 
# The Diagram for MagicGlove
![Diagram for MagicGlove](../Final%20Project/Images/MagicGloveDiagram.png) 

## Making Process / Hardware Wiring
![Kazuha and his sword](../Final%20Project/Images/Process.png) 

### Firmware and Codes 

[Code for FreedomSworn](../Final%20Project/FreedomSworn.py) 

[Code for Magic Glove](../Final%20Project/MagicGlove.py) 

For the glove, the Command of "JUMP" and "Vibration" is like:
``` Python  
if (analog_val <= 4000): #If the button Press is detected
            if (conn_handle != None):
                send_char(' ') #Space Character for Jump
                print('Jump!')
                motor_pwm.duty(50) #Turn on the motor for 50ms
                display_digit(1) #Start the "JUMP" Animation
                sleep_ms(100)
                motor_pwm.duty(0)
                display_digit(2)
                sleep_ms(100)
                motor_pwm.duty(50)
                display_digit(3)
                sleep_ms(100)
                motor_pwm.duty(0)
                display_digit(4)
                sleep_ms(100)
                display_digit(5)
                sleep_ms(100)
                display_digit(16)
                sleep_ms(100)
```

I also made some preparation for the "JUMP" and "RUN" Animations
``` Python 
jump_1 = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,1,0,0,
    0,0,0,0,0,
    0,0,0,0,0
]

jump_2 = [
    0,0,0,0,0,
    0,0,1,0,0,
    0,1,0,1,0,
    0,0,1,0,0,
    0,0,0,0,0
]

jump_3 = [
    0,0,1,0,0,
    0,1,0,1,0,
    1,0,0,0,1,
    0,1,0,1,0,
    0,0,1,0,0
]

jump_4 = [
    0,1,0,1,0,
    1,0,0,0,1,
    0,0,0,0,0,
    1,0,0,0,1,
    0,1,0,1,0
]

jump_5 = [
    1,0,0,0,1,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
    1,0,0,0,1
]

blank = [
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0,
    0,0,0,0,0
]
run_color = (123,194,97)
jump_color = (255, 255, 20)
dot_color = (0,0,0)

# define a function to get color for a pixel:
def get_pixel_color(n):
    if(n == 1):
        return jump_color
    elif(n == 2):
        return run_color
    else:
        return dot_color

def display_digit(m):
    for i in range(25):
            if(m == 1):
                neopixel_strip[i] = get_pixel_color(jump_1[i])
            if(m == 2):
                neopixel_strip[i] = get_pixel_color(jump_2[i])
            if(m == 3):
                neopixel_strip[i] = get_pixel_color(jump_3[i])
            if(m == 4):
                neopixel_strip[i] = get_pixel_color(jump_4[i])
            if(m == 5):
                neopixel_strip[i] = get_pixel_color(jump_5[i])
            if(m == 6):
                neopixel_strip[i] = get_pixel_color(run_1[i])
            if(m == 7):
                neopixel_strip[i] = get_pixel_color(run_2[i]) 
            if(m == 8):
                neopixel_strip[i] = get_pixel_color(run_3[i]) 
            if(m == 9):
                neopixel_strip[i] = get_pixel_color(run_4[i]) 
            if(m == 10):
                neopixel_strip[i] = get_pixel_color(run_5[i]) 
            if(m == 11):
                neopixel_strip[i] = get_pixel_color(run_5[i])
            if(m == 12):
                neopixel_strip[i] = get_pixel_color(run_6[i]) 
            if(m == 13):
                neopixel_strip[i] = get_pixel_color(run_7[i]) 
            if(m == 14):
                neopixel_strip[i] = get_pixel_color(run_8[i]) 
            if(m == 15):
                neopixel_strip[i] = get_pixel_color(run_9[i]) 
            if(m == 16):
                neopixel_strip[i] = get_pixel_color(blank[i])                           
    neopixel_strip.write()
```

For the sword, I also did the "Send Char" Function to make the attack, meanwhile, the character is Attacking, and the light strip would also be turned on. The brightness of the strip is depending on how much force you used to do the attack.

The code is like this:
``` Python  
if (analog_val <= 4000): #If the button Press is detected
            if (conn_handle != None):
                send_char(' ') #Space Character for Jump
                print('Jump!')
                motor_pwm.duty(50) #Turn on the motor for 50ms
                display_digit(1) #Start the "JUMP" Animation
                sleep_ms(100)
                motor_pwm.duty(0)
                display_digit(2)
                sleep_ms(100)
                motor_pwm.duty(50)
                display_digit(3)
                sleep_ms(100)
                motor_pwm.duty(0)
                display_digit(4)
                sleep_ms(100)
                display_digit(5)
                sleep_ms(100)
                display_digit(16)
                sleep_ms(100)
```acc_x = imu0.acceleration[0]
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
```

### Software & Integrations 

Since I didn't use the IFTTT and AdafruitIO, the most important part for me is the Bluetooth, the function to apply is also complicated
``` Python
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
```

### Enclosure / Mechanical Design   

The design of the sword is originally from the Game: Genshin Impact and the sword "Freedom Sworn"

![FreedomSworn](../Final%20Project/Images/FreedomSworn.jpg) 

What I did it to redesign it in order to fit the hardwares which I wanted to apply into the sword.
In order to fit the Dual-Button, The LED Strip and cables into it, I tried three times and successfully managed them at last.

Here's my design graph in illustrator

![FreedomSwornAI](../Final%20Project/Images/AIFile.png) 

For the glove, I tried to find a cool-looking glove, and it took me a long time to manage different cables to make the glove work...

### Here are the showcases of the glove and sword:

![FreedomSwornShowCase](../Final%20Project/Images/ShowCase1.png) 
![GloveShowCase](../Final%20Project/Images/ShowCase2.png) 


## Project outcome  

From this project, not only did I learn how to write programs better, but I also did I enhanced my skill of designing and making hand-made stuff. For the programming part, I now have the ability to know micro python better, to understand how different devices connect together, and how those devices are able to connect to the Internet. It is really important for me to understand all of those things before I push my interactive design to the next level. For the hand-making part, this is my first time making a "Real-Sword", from the first version to the final outcome, I understood how could I make a real hand-made prototype and get through troubles. Meanwhile, improving my hand-made skill is also beneficial for me to do my own physical interaction projects in the future.

## Conclusion  

This term is the first term I really got a feeling of how to learn and write codes, before finishing the final project, I never thought I can push those three ideas so far. Because of this, I think this project really gives me the opportunity to do a design that combines physical and digital interactions together. And moreover, I also feel happy that I could create something real for the game I love and make them work!

## Project references  

Links for Freedom Sworn Exploration:
https://genshin-impact.fandom.com/wiki/Freedom-Sworn

Links for ideas of Vibration Gloves
https://www.youtube.com/watch?v=NJwFG0EoS7E
