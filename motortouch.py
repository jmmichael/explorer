#loosely based on https://learn.pimoroni.com/tutorial/tanya/halloween-explorer-hat-eyes
import explorerhat
from time import sleep

f=10

try:
	while True:
		if explorerhat.touch.five.is_pressed():
			explorerhat.motor.one.forward(f)
			explorerhat.light.red.on()
			sleep (5)
			explorerhat.motor.one.stop()
			explorerhat.light.red.off()
			
		elif explorerhat.touch.six.is_pressed():
			explorerhat.motor.one.forward(f+90)
			explorerhat.light.green.pulse(0.2,0.2,0.5,0.2)
			sleep (5)
			explorerhat.light.green.off()
			

except KeyboardInterrupt:
    pass
    
#finally:
#	GPIO.cleanup
