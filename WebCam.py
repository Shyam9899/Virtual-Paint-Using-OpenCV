import cv2

# 0 for default camera
cap = cv2.VideoCapture(0)

# for breadth and height.....
frameWidth = 640
frameHeight = 480

# id no. of width is 3
cap.set(3,640)

# id no. of height is 4
cap.set(4,480)

# for brightness......
# id no. for brightness is 10
cap.set(10,100)

# video is a series of images so while loop
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break
