import cv2
import os
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
os.chdir('C:\\Users\\MANOJKUMAR M MHETRE\\Desktop')

img = cv2.imread('Untitled.png',1)
print(img.shape)

###### original Image
face_detect = face.detectMultiScale(img,1.1,9)
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('name1',img)
cv2.waitKey()

############ resized image
resized = cv2.resize(img,(300,300))
face_detect1 = face.detectMultiScale(resized,1.1,9)
for (x,y,w,h) in face_detect1:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow('name2',resized)
cv2.waitKey()

def function_face(images):
    face_detect = face.detectMultiScale(images, 1.1, 9)

    for (x, y, w, h) in face_detect:
        cv2.rectangle(images, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('name3', images)
    cv2.waitKey()


a = function_face(cv2.imread('Untitled.png',0))