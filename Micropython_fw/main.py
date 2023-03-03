import machine
import time

pin = machine.Pin(37, machine.Pin.OUT)

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('VM5035215', 'v67tjrzjRdje')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


i=0

do_connect()
while True:
	pin.value(1)
	time.sleep(0.2)
	pin.value(0)
	time.sleep(0.2)
	i=i+1
	print(str(i)+"," + str(i+10))
	


