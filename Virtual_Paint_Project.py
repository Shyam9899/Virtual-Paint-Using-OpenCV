import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)

cap.set(15,frameWidth)
cap.set(15,frameHeight)
cap.set(10,150)

# orange, purple, green  ->  set of color we want to detect
myColor = [[5,107,0,19,255,255],[133,56,0,159,156,255],[57,76,0,100,255,255]]

myColorValues = [[51,153,255],[255,0,255],[0,255,0]]  ## BGR

myPoints = []  ##[x,y,coloId]

# function to find different color
def findColor(img,myColor,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColor:
        # taking first 3 no. of myColor in lower as they denote min value of HSV
        lower = np.array([color[0:3]])
        # taking next 3 no. of myColor in upper as they denote max value of HSV
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
        # here, imshow(), will show 3 different window as we have 3 defined 3 different color
        # in myColor list
        # cv2.imshow(str(color[0]),mask)
    return newPoints
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h, = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)

            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
  success, img = cap.read()
  imgResult = img.copy()
  newPoints = findColor(img,myColor,myColorValues)
  if len(newPoints)!=0:
      for newP in newPoints:
          myPoints.append(newP)
  if len(myPoints)!=0:
      drawOnCanvas(myPoints,myColorValues)


  cv2.imshow("Result",imgResult)
  if cv2.waitKey(1) & 0xFF == ord('q'):
      break



