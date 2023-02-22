import cv2
import numpy as np
img = cv2.imread('CHECKPOINT1.jpg')
lower = np.array([0, 0, 0], dtype=np.uint8)
upper = np.array([100, 100, 100], dtype=np.uint8)
mask = cv2.inRange(img, lower, upper)
masked_img = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Masked Image', masked_img)
print("RGB values of masked image:")
print(masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
