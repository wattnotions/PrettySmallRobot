import machine
import time
from umqtt.robust import MQTTClient



led = machine.Pin(37, machine.Pin.OUT)

mb1 = machine.Pin(6, machine.Pin.OUT)
mb2 = machine.Pin(7, machine.Pin.OUT)

ma1 = machine.Pin(4, machine.Pin.OUT)
ma2 = machine.Pin(5, machine.Pin.OUT)

but = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

def left_track_dir(dir):
    if dir==1: #forward
        mb1.value(0)
        mb2.value(1)
    else: #reverse
        mb1.value(1)
        mb2.value(0)
        
        
def right_track_dir(dir):
    if dir==1: #forward
        ma1.value(1)
        ma2.value(0)
    else: #reverse
        ma1.value(0)
        ma2.value(1)
        
def straight():
    left_track_dir(1)
    right_track_dir(1)

def reverse():
    left_track_dir(0)
    right_track_dir(0)
    
def right():
    left_track_dir(1)
    right_track_dir(0)
    
def left():
    left_track_dir(0)
    right_track_dir(1)
        
def motors_off():
    mb1.value(0)
    mb2.value(0)
    ma1.value(0)
    ma2.value(0)

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



def motor_test():
    i=0
    motor_script=False
    while True:
        if but.value()==0:
            led.on()
            motor_script=True
        else:
            led.off()
            
        if motor_script==True:
            straight()
            time.sleep(2)
            right()
            time.sleep(2)
            
            straight()
            time.sleep(2)
            right()
            time.sleep(2)
            
            straight()
            time.sleep(2)
            right()
            time.sleep(2)
            
            straight()
            time.sleep(2)
            right()
            time.sleep(2)
            
            motors_off()
            motor_script=False

    


def mqtt_send():
    c = MQTTClient("", 'raspberrypi.local', user='', password='')
    c.connect()
    while True:

        
        c.publish(b"testTopic", b'Howiye')
        print("Sent howiye")
        time.sleep(10)
        
    
def sub_cb(topic, msg):
    print((topic, msg))
    if msg==b"l":
        left()
    if msg==b"r":
        right()
    if msg==b"u":
        straight()
    if msg==b"d":
        reverse()
    if msg==b"s":
        motors_off()
    
def mqtt_receive():
    c = MQTTClient("", 'raspberrypi.local', user='', password='')
    c.connect()
    c.DEBUG = True
    c.set_callback(sub_cb)
    
    print("New session being set up")
    c.subscribe(b"testTopic")
    
    while 1:
        c.wait_msg()

    c.disconnect()

led.off()
motors_off()
while(but.value()==1):
    pass

led.on()
do_connect()
mqtt_receive()
    
    
    