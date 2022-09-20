import cv2
import numpy as np

# detecting faces
# we will create lots of positive faces and negative faces and train cascade file to detect faces
# but here, we do not use that but a trained file provided by opencv to detect faces
# it is cascade classifier

faceCascade = cv2.CascadeClassifier("Resources/haarCascade_Frontal_default.txt")
img = cv2.imread("Resources/cont.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Output",img)

cv2.waitKey(0)
