import machine
import time
from umqtt.robust import MQTTClient



led = machine.Pin(37, machine.Pin.OUT)

mb1 = machine.Pin(6, machine.Pin.OUT)
mb2 = machine.Pin(7, machine.Pin.OUT)

ma1 = machine.Pin(4, machine.Pin.OUT)
ma2 = machine.Pin(5, machine.Pin.OUT)


mb1pwm = machine.PWM(ma1)
mb2pwm = machine.PWM(ma2)

ma1pwm = machine.PWM(mb1)
ma2pwm = machine.PWM(mb2)

but = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

def set_pwm(pwm):
    mapwm.duty(pwm)
    mbpwm.duty(pwm)

def left_track_dir(dir, pwm):
    if dir==1: #forward
        mb1pwm.duty(0)
        mb2pwm.duty(pwm)
    else: #reverse
        mb1pwm.duty(pwm)
        mb2pwm.duty(0)
        
        
def right_track_dir(dir,pwm):
    if dir==1: #forward
        ma1pwm.duty(pwm)
        ma2pwm.duty(0)
    else: #reverse
        ma1pwm.duty(0)
        ma2pwm.duty(pwm)
        
def straight(pwm):
    left_track_dir(1,pwm)
    right_track_dir(1,pwm)

def reverse(pwm):
    left_track_dir(0,pwm)
    right_track_dir(0,pwm)
    
def right(pwm):
    
    
    left_track_dir(1,pwm)
    right_track_dir(0,pwm)
    
def left(pwm):
    left_track_dir(0,pwm)
    right_track_dir(1,pwm)
    
    
def drive(dir, pwm, wheel_ang):
    
    turn_ratio = (1-(abs(wheel_ang)/100))
    if wheel_ang>0:
        left_pwm = pwm
        right_pwm = pwm*turn_ratio
    elif wheel_ang<0:
        right_pwm = pwm
        left_pwm = pwm*turn_ratio
    elif wheel_ang==0
        right_pwm = pwm
        left_pwm = pwm
        
    print(str(left_pwm) + "   " + str(right_pwm))   
    left_track_dir(dir, int(left_pwm))
    right_track_dir(dir, int(right_pwm))
        
def motors_off():
    mb1pwm.duty(0)
    mb2pwm.duty(0)
    ma1pwm.duty(0)
    ma2pwm.duty(0)

def wifi_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('VM5035215', 'v67tjrzjRdje')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
 


def mqtt_send():
    c = MQTTClient("", 'raspberrypi.local', user='', password='')
    c.connect()
    while True:

        
        c.publish(b"testTopic", b'Howiye')
        print("Sent howiye")
        time.sleep(10)
        

def sub_cb(topic, msg):
    print((topic, msg))
    
    global line
    line=msg.decode("utf-8").strip()
    
    
    


led.off()
motors_off()
#quit()
#while(but.value()==1):
#    pass

led.on()
print("in program")
wifi_connect()



def main(server="raspberrypi.local"):
    dir=1
    shift_up=0
    shift_down=0
    gear=5
    pwm=1000
    c = MQTTClient("umqtt_client", server )
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"testTopic")
    while True:
        if True:
            # Blocking wait for message
            old_shift_up = shift_up
            old_shift_down = shift_down
            
            c.wait_msg()
            data=line.split(",")
    
            shift_up = int(data[0])
            shift_down = int(data[1])
            accel = int(data[2])
            brake = int(data[3])
            wheel = int(data[4])
            print(wheel)
            
            if (old_shift_up!=shift_up) or (old_shift_down!=shift_down):
                if shift_up: gear+=1
                if shift_down: gear-=1
                if gear < 5 : gear=5
                if gear > 10: gear = 10
                pwm = gear*100
                
            
            
            if shift_down: dir=-1
            if accel: drive(dir, pwm, wheel)
            if not accel               : motors_off()
            if brake                   : motors_off()
               

    c.disconnect()


if __name__ == "__main__":
    main()


    
    
    