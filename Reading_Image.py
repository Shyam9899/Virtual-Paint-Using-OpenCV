import cv2

# imread() is a function in cv2 library to read an image, in
# argument section we write path of image where image is present
img = cv2.imread("Resources/imag.png")

# imshow() is func. in cv2 to display image, 1st argument is "Window name" and second is name of image
cv2.imshow("Output",img)

#  to delay we use waitKey() function, 0 means infinite time, 1 means 1ms
cv2.waitKey(0)


