print("hello")

from machine import Pin
import machine, neopixel

pwr = Pin(38, Pin.OUT)
led = Pin(39, Pin.OUT)

pwr.value(1)

np = neopixel.NeoPixel(machine.Pin(39), 1)

np[0] = (100, 0, 0) # set to red, full brightness
np.write()

print("v4")
