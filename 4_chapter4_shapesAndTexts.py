import cv2
import numpy as np

BlackImage = np.zeros((512, 512))
""" This a gray image, we can check that by printing the shape.
it will print only the shape, without any channel. if we want to create an image with a channel. we have to do it like below """

ImgWithChannel = np.zeros((512, 512, 3), np.uint8)
# ImgWithChannel[:] = 255, 234, 0       # Adding color to the image

""" Drawing a line """
cv2.line(ImgWithChannel, (0, 0), (512, 512), (0, 255, 0), 3)

""" print(BlackImage.shape)
print(ImgWithChannel.shape) """

cv2.imshow("Output 1", BlackImage)
cv2.imshow("Output 2", ImgWithChannel)

cv2.waitKey(0)