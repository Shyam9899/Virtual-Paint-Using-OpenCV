import cv2

# VideoCapture() is a function in cv2 library to read video, in
# argument section we write path of image where video is present

cap = cv2.VideoCapture("Resources/video.mp4")

# video is a series of images so while loop
while True:
     success, img = cap.read()
     cv2.imshow("Video",img)
# wait for delay and looks for 'q' to break the loop
     if cv2.waitKey(1) & 0xFF == ord('q'):
      break
