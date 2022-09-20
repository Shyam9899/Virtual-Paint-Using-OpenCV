import cv2
import numpy as np

img = cv2.imread("Resources/imag.png")

# print in order height,width and a no. like 3 for BGR
print(img.shape)

# can increase the pixel but not quality
imgResize = cv2.resize(img,(2000,1500))
print(imgResize.shape)

# first height then width
imgCropped = img[0:200][100:200]

cv2.imshow("Image",img)
cv2.imshow("ImageResize",imgResize)
cv2.imshow("ImageCropped",imgCropped)

cv2.waitKey(0)