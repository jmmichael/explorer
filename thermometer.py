#https://learn.pimoroni.com/tutorial/explorer-hat/making-a-minecraft-thermometer
import explorerhat

def temp():
    explorerhat.analog.one.read()
print (temp())
