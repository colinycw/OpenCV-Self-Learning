import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')

img = cv2.imread('Source/lena.jpg', 1)
_, mask = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
face = face_cascade.detectMultiScale(img, 1.3, 5)

for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_gray, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

cv2.imshow('Image', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
