import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

img = cv2.imread('Source/messi5.jpg', 0)

canny = cv2.Canny(img, 0, 0)

'''titles = ['image', 'Canny']
images = [img, canny]

for i in range(len(titles)):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])

plt.show()'''

cv2.namedWindow('Canny')

cv2.createTrackbar('CannyX', 'Canny', 0, 500, nothing)
cv2.createTrackbar('CannyY', 'Canny', 0, 500, nothing)

while(1):
    cv2.imshow('Canny', canny)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    cx = cv2.getTrackbarPos('CannyX', 'Canny')
    cy = cv2.getTrackbarPos('CannyY', 'Canny')

    canny = cv2.Canny(img, cx, cy)

cv2.destroyAllWindows()