import cv2

img = cv2.imread("Resources/motor.jpg")
ResizedImage = cv2.resize(img, (300, 257))      # Resizing the image
CroppedImage = img[10:300, 250:450]             # Cropping the image

print(img.shape)                # checking the dimensions of an image
print(ResizedImage.shape)

cv2.imshow("Output", img)
cv2.imshow("Resized Output", ResizedImage)
cv2.imshow("Cropped Output", CroppedImage)
cv2.waitKey(0)