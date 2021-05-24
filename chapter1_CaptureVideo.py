import cv2
#Importing and showing a video
cap = cv2.VideoCapture("Resources/Video.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video Output",img)
    if cv2.waitKey(1) & 0xFF ==ord('a'):
        break