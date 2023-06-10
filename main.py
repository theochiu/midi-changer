from machine import Pin, UART
from time import sleep, sleep_ms

from lcd import *
from Effect import Effect

# led_pin_nums = [32, 33, 25, 26]

midi_cc = 0xb0
midi_delay_ms = 130


def setup_leds(pin_nums):
    res = []
    for pin_num in pin_nums:
        p = Pin(pin_num, Pin.OUT)
        p.on()  # default all effects on
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
    p.irq(handler=None)  # disable interrupt
    sleep_ms(100)
    p.irq(button_pressed, Pin.IRQ_FALLING)  # re-enable

    if p.value() != 0:
        return

    # identify which button was pressed
    for effect in effects:
        if effect.pin_num == int(str(p)[4:-1]):
            break
    
    print(effect.name)

    # toggle corresponding LED
#     new_val = not leds[i].value()
#     leds[i].value(new_val)  

    # do midi
    midi_msg = bytes([midi_cc, effect.cc_num, 0])

    midi_handle.write(midi_msg)
    sleep_ms(midi_delay_ms)

    if (effect.pressed):  # turn off needs double
        midi_handle.write(midi_msg)
        sleep_ms(midi_delay_ms)

    effect.pressed = not effect.pressed

    # home button
    midi_handle.write(bytes([midi_cc, 20, 0]))
    
    # LCD
#     lcd.clear()
#     if effect.pressed:
#         status = "on"
#     else:
#         status = "off"
#     lcd.message(f"{effect.name} {status}")


def setup_button(pin_num, pullup):
    if pullup:
        p = Pin(pin_num, Pin.IN, Pin.PULL_UP)
    else:
        p = Pin(pin_num, Pin.IN)

    p.irq(button_pressed, Pin.IRQ_FALLING)


# noinspection PyArgumentList
def setup_midi():
    handle = UART(1, baudrate=31250, bits=8, parity=None, stop=1, tx=17)
    return handle


def setup_effects():
    res = []
    
    res.append(Effect("Drive", 7, 25))
    res.append(Effect("Comp", 5, 26))
    res.append(Effect("EQ", 10, 27))
    res.append(Effect("NG", 11, 14))
    res.append(Effect("FX A", 6, 35, False))
    res.append(Effect("FX B", 12, 32))
    res.append(Effect("Delay", 13, 33))
    res.append(Effect("Reverb", 14, 36, False))
    
    for effect in res:
        setup_button(effect.pin_num, effect.pullup)
    
    return res


if __name__ == "__main__":
    # setup lcd
#     lcd = CharLCD()
#     lcd.message('Startup ', 2)
#     lcd.set_line(1)
#     lcd.message('success', 2)

    # setup effects
#     effects = setup_effects()

    # setup led and buttons
#     leds = setup_leds(led_pin_nums)
    effects = setup_effects()
    
    

    # setup midi
    midi_handle = setup_midi()
