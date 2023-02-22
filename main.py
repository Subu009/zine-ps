import cv2
import numpy as np
img=cv2.imread('CHECKPOINT1.png',1)
print(img)
cv2.imshow('image that is sampled (checpoint 1)',img)
cv2.waitKey(0)
print(img.shape)
B,G,R=img[0,0]
i=0
j=0
while R!=255:
    B,G,R=img[i,j]
    i=i+1
    j=j+1

print("the rgb values of the given image are:",R,",",G,",",B)