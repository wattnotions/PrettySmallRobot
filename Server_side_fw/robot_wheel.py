
import paho.mqtt.client as paho

import serial

ser=serial.Serial('COM7')  # open serial port

broker="raspberrypi.local"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)

shift_up=0
shift_down=0
accel=0
brake=0
wheel=0


while True:
    line=ser.readline().decode("utf-8") 
    data=line.split(",")
    
    shift_up_old = shift_up
    shift_down_old = shift_down
    accel_old = accel
    brake_old = brake
    wheel_old = wheel
    
    shift_up = data[0]
    shift_down = data[1]
    accel = data[2]
    brake = data[3]
    wheel = data[4].strip()
    
    
    if shift_up_old != shift_up:
        ret = client1.publish("testTopic","s_up,"+shift_up)
        
    if shift_down_old != shift_down:
        ret = client1.publish("testTopic","s_down,"+shift_down)
        
    if accel_old != accel:
        ret = client1.publish("testTopic","accel,"+accel)
    
    if brake_old != brake:
        ret = client1.publish("testTopic","brake,"+brake)
        
    if wheel_old != wheel:
        ret = client1.publish("testTopic","wheel,"+wheel)
    

    

def press(key):
    if key == "up":
        print("up pressed")
        ret= client1.publish("testTopic","u")
    elif key == "down":
        print("down pressed")
        ret= client1.publish("testTopic","d")
    elif key == "left":
        print("left pressed")
        ret= client1.publish("testTopic","l")
    elif key == "right":
        print("right pressed")
        ret= client1.publish("testTopic","r")
    elif key == "space":
        print("right pressed")
        ret= client1.publish("testTopic","s")

listen_keyboard(on_press=press)
