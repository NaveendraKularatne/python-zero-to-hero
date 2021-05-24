import cv2
#Showing an image
img = cv2.imread("Resources/Lenna.png")
cv2.imshow("Image Output",img)

cv2.waitKey(0)