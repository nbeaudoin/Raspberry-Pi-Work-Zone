from gpiozero import LED
from time import sleep

led = LED(25)

delay = 1

while True:
	# set LED on for delay time
	led.on()
	print('LED set to on')
	sleep(delay)

	# set LED off dor delay time
	led.off()
	print('LED set to off')
	sleep(delay)
