import cv2
import os
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
os.chdir('C:\\Users\\MANOJKUMAR M MHETRE\\Desktop')

img = cv2.imread('Untitled.png',1)
print(img.shape)

###### original Image - Face and Eye detection #################
eye_detect = eye.detectMultiScale(img,1.1,9)
face_detect = face.detectMultiScale(img,1.1,9)
for (x,y,w,h) in eye_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('name1',img)
cv2.waitKey()

########### Eye Detection #################

os.chdir('C:\\pythonProject')
img1 = cv2.imread('jaya.jpg',1)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
face_detect = eye.detectMultiScale(gray,1.1,9)
for (x,y,w,h) in face_detect:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('name2',img1)
cv2.waitKey()
