import cv2

import sys
import os
print(os.getcwd())

os.chdir('C:\\Users\\MANOJKUMAR M MHETRE\\Desktop')

img = cv2.imread('Untitled.png',1)
print(img.shape)
cv2.imshow('name',img)
cv2.waitKey(0)

resized = cv2.resize(img,(300,300))
print(resized.shape)
cv2.imshow('name1',resized)
cv2.waitKey(0)


resized1 = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
print(resized1.shape)
cv2.imshow('name2',resized1)
cv2.waitKey(0)


resized2 = cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2)))
print(resized2.shape)
cv2.imshow('name2',resized2)
cv2.waitKey(0)

