# Necessary library
import pyfirmata

comport='COM5'
board=pyfirmata.Arduino(comport)
led=board.get_pin('d:13:o')

def led(total):
    if total==0:
    	# This is the case when user want to turn of the light
        light.write(0)
    elif total==1:
    	# In this case, user can turn on the 
        light.write(1)