#https://projects.raspberrypi.org/en/projects/explorer-hat-buggy
#https://projects.raspberrypi.org/en/projects/explorer-hat-buggy
import explorerhat
from time import sleep
from guizero import App, PushButton

def forwards():
    explorerhat.motor.one.forward(100)#6 is minimum
    sleep (5)
    explorerhat.motor.one.stop()
def backwards():
    explorerhat.motor.one.backward(100)
    sleep (5)
    explorerhat.motor.one.stop()
    
app = App("Contoller")

drive = Pushbutton (app, forwards, text= "Forwards")
reverse = Pushbutton (app, backwards, text= "Backwards")
