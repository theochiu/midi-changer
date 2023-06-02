import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

lcd_rs = digitalio.DigitalInOut(board.TX)
lcd_en = digitalio.DigitalInOut(board.D21)

lcd_4 = digitalio.DigitalInOut(board.D14)
lcd_5 = digitalio.DigitalInOut(board.D32)
lcd_6 = digitalio.DigitalInOut(board.D15)
lcd_7 = digitalio.DigitalInOut(board.D33)

lcd_columns = 16
lcd_rows = 2

lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_4, lcd_5, lcd_6, lcd_7,
    lcd_columns, lcd_rows
)

lcd.home
lcd.message = "Hello world\n"
lcd.display = True
