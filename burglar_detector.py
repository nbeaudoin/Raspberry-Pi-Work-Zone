# import the necessary libraries
from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep

# create objects that refer to a button,
# a motion, sensor, and the PiCamera
button = Button(2)
pir = MotionSensor
camera = PiCamera

# start the camera
camera.rotation = 180
camera.start_preview()

# create image names
i = 0

# stop the camera when the push button is pressed
def stop_camera():
    camera.stop_preview()
    # exit the program

# take a photo when motion is detected
def take_photo():
    global image 
    i = i + 1
    camera.capture('/home/pi/Desktop/image_%s.jpg' % i)
    print('A photo has been taken')
    sleep(10)

# assign a function that runs when the button is pressed
button.when_pressed = stop_camera
# assign a function that runs when motion is detected
pir.when_motion = take_photo

pause()