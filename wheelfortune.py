#ttp://my.hcoe.net/wp-content/uploads/2017/01/explorer_hat_workshop.pdf - fails
import explorerhat
from time import sleep
from random import randint

def wheel(channel, event):
	duration = randint(10,100)
	print (duration)
	explorerhat.motor.one.forward(50)
	sleep (duration)
	explorerhat.motor.one.stop()

explorerhat.touch.four.pressed(wheel)
