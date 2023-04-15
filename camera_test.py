from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(2)

camera.capture("test_image.jpg")
print("Done.")