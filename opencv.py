import cv2
import time
import threading
from datetime import datetime

# open video0
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)


# set width and height
width = 1280
height = 800
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


# set fps
# cap.set(cv2.CAP_PROP_FPS, 30)
image_path = 'resim1.png'
directory = 'C:/Users/User/Desktop/opencv'


ret, frame = cap.read()


def printit():
    print("Hello, World!")
    t = time.localtime(time.time())
    hour = t.tm_hour
    min = t.tm_min
    sec = t.tm_sec
    tt = str(hour)+"."+str(min)+"."+str(sec)
    cv2.imwrite(tt+".png", frame)
    cv2.imwrite(tt+".png",frame,cv2.COLOR_BGR2GRAY)
    threading.Timer(5.0, printit).start()
printit()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        # Display the resulting frame
        cv2.circle(center=(640,400),thickness=1,radius=5,img=frame,color=(0,255,0))
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()