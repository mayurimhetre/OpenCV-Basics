import cv2
import time


vid = cv2.VideoCapture(0)
check,frame = vid.read()
print(check)
print(frame)
time.sleep(1)
cv2.imshow('name1',frame)

vid.release()
cv2.waitKey(0)