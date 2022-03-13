

import cv2 as cv

img = cv.imread('images/cat.jpg')
def rescaleimg(img, scale = 0.5):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(img, dimensions, interpolation= cv.INTER_AREA)
reimg = rescaleimg(img)
cv.imshow('ResizedImg', reimg)

gray = cv.cvtColor(reimg, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)