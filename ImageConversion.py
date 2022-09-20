import cv2
import numpy as np
img = cv2.imread("Resources/imag.png")

# a matrix of size 5X5 and all values 1, value are unsigned int of 8 bit
kernel = np.ones((5,5),np.uint8)

# cvtColor() convert image into different color spaces

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

# Sketchy type, for Detection of edges
imgCanny = cv2.Canny(img,150,200)

# Dilation expands the image pixels i.e  make thicker,  basically to join line
# Kernel is just a matrix, that to we have to define sizeof and value of

imgDialation = cv2.dilate(imgCanny,kernel,iterations = 1)

# to make image thinner, opposite of dialation
imgEroded = cv2.erode(imgDialation,kernel,iterations =1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialeted Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)
