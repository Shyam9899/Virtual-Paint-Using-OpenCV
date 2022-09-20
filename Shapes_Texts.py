import cv2
import numpy as np

# a matrix of size 5X5 and all values 1, value are unsigned int of 8 bit
img = np.zeros((512,512,3),np.uint8)
print(img.shape)

# colors the whole image to blue(255), [:] means whole image
# to draw the line on image
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

# to draw rectangle, cv2.FILLED fill the rectangle with the given color
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)

# to draw circle
cv2.circle(img,(450,50),30,(255,255,0),2)

cv2.putText(img,"OPENCV ",(300,200),cv2.FONT_HERSHEY_PLAIN,1,(0,150,0),2)

cv2.imshow("Image",img)

cv2.waitKey(0)

