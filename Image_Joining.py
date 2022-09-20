import cv2
import numpy as np

img = cv2.imread("Resources/imag.png")

#  have some limitations, *)- img size can not be changed and one BGR and Gray img can not be added
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Output", img)
cv2.imshow("Horizontal", imgHor)
cv2.imshow("Vertical", imgVer)

cv2.waitKey(0)
