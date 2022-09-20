import cv2
import numpy as np
# we will show how many corner it has and area of the shapes

def getContours(img):
    # to retrieve to outer contour corner
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # all contours get saved in contours variable
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # here print func. print all the area that get detected
        print(area)
        # to ignore noise
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # to approximate the corner of edges, and expecting closed perimeter
            peri = cv2.arcLength(cnt,True)
            print(peri)

            # approximating corner of contour
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            print(len(approx))

            # we  get no. of sides
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objCor == 3: ObjectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio>0.95 and aspRatio <1.05 : ObjectType = "Square"
                else: ObjectType = "Rectangle"
            elif objCor>4 : ObjectType = "Circle"
            else: ObjectType = "None"

            # forming rectangle shapes around contour
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            # putting name of shape on contour
            cv2.putText(imgContour,ObjectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_PLAIN,0.8,(0,0,0),1)


img = cv2.imread("Resources/cont.jpg")
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)


imgBlank = np.zeros_like(img)
cv2.imshow("Output",img)
cv2.imshow("ImageGray",imgGray)
cv2.imshow("ImageBlur",imgBlur)
cv2.imshow("ImageCanny",imgCanny)
cv2.imshow("ImageBlank",imgBlank)
cv2.imshow("ImageContour",imgContour)
cv2.waitKey(0)
