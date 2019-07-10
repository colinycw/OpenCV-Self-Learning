import cv2

img = cv2.imread('Source/walking.png', -1) # 1 - colored, 0 - gray-scaled, -1 - unchanged

print(img)

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF # & 0xFF documentation recommended

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()