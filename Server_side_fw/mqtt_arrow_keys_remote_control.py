import keyboard
import paho.mqtt.client as paho
from sshkeyboard import listen_keyboard
broker="localhost"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)


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
