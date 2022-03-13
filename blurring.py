import cv2 as cv

reimg = cv.imread('images/duck.jpg')


# Averaging
average = cv.blur(reimg, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(reimg, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(reimg, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(reimg, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)