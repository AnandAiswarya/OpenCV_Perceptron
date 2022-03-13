import cv2 as cv
img = cv.imread('images/cat.jpg')
def rescaleimg(img, scale = 0.5):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(img, dimensions, interpolation= cv.INTER_AREA)
cv.imshow('Img', img)
cv.imshow('ResizedImg', rescaleimg(img))
cv.waitKey(0)