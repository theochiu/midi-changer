
from machine import Pin
from time import sleep, sleep_ms

from lcd import *

do_rotate = True
led_pin_nums = [23, 22, 14, 32]
button_pin_nums = [19, 16, 17, 21]
leds = []
buttons = []


def setup_leds(pin_nums):
    res = []
    for pin_num in pin_nums:
        p = Pin(pin_num, Pin.OUT)
        p.off()
        res.append(p)
    return res

def led_sweep(leds):
    for led_pin in leds:
        sleep(0.25)
        led_pin.on()
        
def led_rotate(leds):
    for led_pin in leds:
        sleep(0.25)
        led_pin.on()
    for led_pin in leds:
        sleep(0.25)
        led_pin.off()

def button_pressed(p):
    
    # debounce
    # (turn off interrupt, and check for stable value in 20 ms)
    p.irq(handler=None)# disable interrupt
    sleep_ms(20)
    p.irq(button_pressed, Pin.IRQ_FALLING) # re-enable
    
    if p.value() != 0:
        return
    
    # identify which button was pressed
    i = buttons.index(p)
    
    # disable rotation
    global do_rotate
    do_rotate = False

    
    # middle dual press case
    if i == 1 and buttons[2].value() == 0:
        led_rotate(leds)

    
    # toggle corresponding LED
    new_val = not leds[i].value()
    leds[i].value(new_val)
    

    

def setup_buttons(pin_nums):
    res = []
    for pin_num in pin_nums:
        p = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        p.irq(button_pressed, Pin.IRQ_FALLING)
        res.append(p)
    return res    
    
if __name__ == "__main__":

    # main here
    lcd = CharLCD()
    lcd.message('Hello', 2)
    lcd.set_line(1)
    lcd.message('World!', 2)

    # leds = setup_leds(led_pin_nums)
    # buttons = setup_buttons(button_pin_nums)
    #
    # while True:
    #     if (do_rotate):
    #         led_rotate(leds)
    
        
    