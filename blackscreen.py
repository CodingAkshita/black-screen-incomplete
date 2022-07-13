#importing
import cv2
import numpy as np

#Starting the video capture
video = cv2.VideoCapture(0)
image = cv2.imread('image.jpg')

while True:
    ret, frame = video.read()
    print(frame)
    
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
    
    #Creating an array of RGB
    upperBlack = np.array([104, 153, 70])
    lowerBlack = np.array([30, 30, 0])
    
    mask = cv2.inRange(frame, lowerBlack, upperBlack)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    f = frame - res
    #function to return frame or image if the value of f is 0
    f = np.where(f == 0, image, f)
    
    cv2.imshow("video", frame)
    cv2.imshow("mask", f)
    
       
video.release()    
cv2.destroyAllWindows()