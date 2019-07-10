import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Source/messi5.jpg', cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

edges = cv2.Canny(img, 100, 200)

titles = ['image', 'Laplacian', 'SobelX', 'SobelY', 'SobelCombined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, edges]

for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.xticks([]), plt.yticks([])
    plt.title(titles[i])

plt.show()