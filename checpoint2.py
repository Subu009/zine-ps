import cv2
import numpy as np
img = cv2.imread('checkpoint2.png',0)
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT,1,70,minRadius=0,maxRadius=)
if circles is not None:
    circles=np.uint16(np.around(circles))
    max_radius=0
    largest_circle=None
    for i in circles:
        x,y,r=i
        if r>max_radius:
            max_radius=r
            largest_circle=(x,y,r)

    output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.circle(output_img, (largest_circle[0], largest_circle[1]), largest_circle[2], (0, 0, 255), 2)
    cv2.imshow("Largest Circle", output_img)
    cv2.waitKey(0)
else:
    print("No circles found in the image.")