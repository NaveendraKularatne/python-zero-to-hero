import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

image = cv2.imread("Resources/Lenna.png")                       # Original Image
GrayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)             # Gray Image
BlurImage = cv2.GaussianBlur(image, (13, 13), 0)                # Blue Image
CannyImage = cv2.Canny(image, 150, 150)                         # Canny Image
DilatedImage = cv2.dilate(CannyImage, kernel, iterations=1)     # Dilated Image
ErodedImage = cv2.erode(DilatedImage, kernel, iterations=1)     # Eroted Image

cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", GrayImage)
cv2.imshow("Blur Image", BlurImage)
cv2.imshow("Canny Image", CannyImage)
cv2.imshow("Dilated Image", DilatedImage)
cv2.imshow("Eroded Image", ErodedImage)

cv2.waitKey(0)
