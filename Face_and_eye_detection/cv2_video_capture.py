import time
import cv2
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')
video = cv2.VideoCapture(0)

a = 1

while True:
    a = a+1
    check, frame = video.read()
    face_detect = face.detectMultiScale(frame, 1.1, 9)
    eye_detect = eye.detectMultiScale(frame, 1.1, 9)
    for (x, y, w, h) in face_detect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (x, y, w, h) in eye_detect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('name', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(a)
video.release()

