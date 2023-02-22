import cv2
import numpy as np

cap = cv2.imread('CHECKPOINT1.png')
cap = cv2.resize(cap, (340, 480))
cv2.imshow('image that is sampled (checpoint 1)',cap)
cv2.waitKey(0)
for x in range(0, 340, 1):
    for y in range(0, 480, 1):
        color = cap[y, x]
        b,g,r=color
        if b!=255 or g!=255 or r!=255:
            print (color)
            break