from gpiozero import PWMLED, MCP3008
from time import sleep

# create an object called pot that refers to MCP3008 channel 0
pot = MCP3008(0)

# create a PWMLED object called led that refers to GPIO 17
led = PWMLED(17)

while True:
	# pot.value accesses the current pot reading
	if(pot.value < 0.001):
		# turn off
		led.value = 0
	else:
		# change led brightness according to pot value
		led.value = pot.value
	
	print(pot.value)
	sleep(0.1)