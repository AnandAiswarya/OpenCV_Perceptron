import cv2 as cv
img = cv.imread('images/cat.jpg')
def rescaleimg(img, scale = 0.3):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(img, dimensions, interpolation= cv.INTER_AREA)
reimg = rescaleimg(img)
#grey
gray = cv.cvtColor(reimg, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
#blur
blur = cv.GaussianBlur(reimg, (7,7),0, borderType= cv.BORDER_DEFAULT)
cv.imshow('gblur', blur)
#edge
canny = cv.Canny(blur,125,175)
cv.imshow('edge', canny)
#dilate
dilated = cv.dilate(canny, (5,5), iterations=1)
cv.imshow('dilated',dilated)
#erode
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('erode',eroded)
#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
cv.waitKey(0)