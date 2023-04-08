from gpizero imoprt PMWLED, MCP3008
from time import sleep

# create an object called pot that referst o MCP3008 channel 0
pot = MCP3008

# create a PWMLEd object called led that refers to GPIO 17
led = PWMLED(17)

while True:
		# pot.value accesses the current pot reading
		if(pot.value < 0.001):
			# if the pot value is very small, the led is turned off
			led.value = 0
		else:
			# change led brightness according to the pot value
			led.value = pot.value
		# print the pot value
		print(pot.value)
		# pause for 0.1 seconds
		sleep(0.1) 