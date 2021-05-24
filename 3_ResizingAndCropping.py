import cv2
img = cv2.imread("Resources/motor.jpg")
print(img.shape)
cv2.imshow("Output", img)
cv2.waitKey(0)