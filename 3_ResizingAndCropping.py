import cv2

img = cv2.imread("Resources/motor.jpg")
ResizedImage = cv2.resize(img, (300, 257))

print(img.shape)
print(ResizedImage.shape)

cv2.imshow("Output", img)
cv2.imshow("Resized Output", ResizedImage)
cv2.waitKey(0)