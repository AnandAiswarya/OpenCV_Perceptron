from operator import truediv
import cv2 as cv
# img = cv.imread('images/cat.jpg')
# cv.imshow('Cat', img)
capture = cv.VideoCapture('images/Task Video.mp4') #pass 0 for webcam or 1 for ext cam
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('x'):
        break
capture.release()
cv.destroyAllWindows()
#cv.waitKey(1)