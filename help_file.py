### Source: https://notenoughtech.com/raspberry-pi/raspberry-pi-camera-module-3/

##I strongly suggest Raspberry Pi OS with Desktop environment

## IMAGES ##

#testing, 1.. 2.. 3..
libcamera-hello

#give me preview window forever  (or use -t in ms)
libcamera-hello -t 0

#snapshot at full resolution - save file in current location
libcamera-jpeg -o test.jpg

#snap a picture with a preview window save image at selected resolution
libcamera-jpeg -o test.jpg -t 2000 --width 640 --height 480


## AF manipulation ##

#add to test AF before capture
--autofocus-on-capture	

# AF modes
--autofocus-mode default|manual|continous
--autofocus-range normal|micro|full 

#MF - 0= infinity or move the lens to the 1 / number position, so the value 2 would focus at approximately 0.5m
--lens-position 0


## VIDEO ##

#record 10 sec video as .h264 and save in current dir
libcamera-vid -t 10000 -o test.h264

# record 1080p@60
libcamera-vid --intra 60 --width 1920 --height 1080 -o test.h264

#as above but mjpeg file (compressed)
libcamera-vid -t 10000 --codec mjpeg -o test.mjpeg


## STREAM ##

#hey look, I can stream
libcamera-vid -t 0 --inline -o udp://<ip-addr>:<port>

#I'm also RTSP camera
libcamera-vid -t 0 --inline -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream1}' :demux=h264