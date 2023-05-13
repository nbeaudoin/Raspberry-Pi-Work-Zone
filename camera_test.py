from picamera import PiCamera
import time

camera = PiCamera()
time.sleep(3)

camera.capture("test_image.jpg")
print("Done.")