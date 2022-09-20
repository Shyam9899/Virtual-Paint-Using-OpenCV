import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)


while True:
  img = cv2.imread("Resources/imag.png")

# The HSV or Hue, Saturation, and value of a given object is the color space associated with the object in OpenCV.
# The Hue in HSV represents the color, Saturation in HSV represents the greyness, and Value in HSV represents the
# brightness. It is mostly used for color segmentation purpose.
  imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# here we get access to real time value of HSV
  h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
  h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
  s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
  s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
  v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
  v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
  print(h_min,h_max,s_min,s_max,v_min,v_max)

  lower = np.array([h_min,s_min,v_min])
  upper = np.array([h_max,s_max,v_max])

# defining lower and upper value of color ranges for masking purpose
  mask = cv2.inRange(imgHSV,lower,upper)
  imgResult = cv2.bitwise_and(img,img,mask = mask)

  cv2.imshow("Output", img)
  cv2.imshow("HSV", imgHSV)
  cv2.imshow("Mask", mask)
  cv2.imshow("imgResult", imgResult)


  cv2.waitKey(1)