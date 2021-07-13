import cv2
import numpy as np

BlackImage = np.zeros((512, 512))
coloredImage = np.zeros((512, 512, 3), np.uint8)
""" This a gray image, we can check that by printing the shape.
it will print only the shape, without any channel. if we want to create an image with a channel. we have to do it like below """

ImgWithChannel = np.zeros((512, 512, 3), np.uint8)
# ImgWithChannel[:] = 255, 234, 0       # Adding color to the image

""" Drawing a line """
coloredImage[200:300, 150:200] = 255, 0, 0
cv2.line(ImgWithChannel, (0, 0), (512, 512), (0, 255, 0), 3)
cv2.rectangle(ImgWithChannel, (200, 200), (350, 500), (0, 0, 255), 2)
cv2.circle(ImgWithChannel, (256, 256), 60, (255, 255, 0), 5)
cv2.putText(ImgWithChannel, " openCV ", (350, 350),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

""" print(BlackImage.shape)
print(ImgWithChannel.shape) """

cv2.imshow("Output 1", BlackImage)
cv2.imshow("Output 2", ImgWithChannel)
cv2.imshow("Color output", coloredImage)

cv2.waitKey(0)