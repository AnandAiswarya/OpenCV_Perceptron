from pickletools import uint8
import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3), dtype= 'uint8') #https://www.rapidtables.com/web/color/RGB_Color.html
#cv.imshow('Black', blank)
blank [200:300] = 0,255,0 #blank [200:300, 400:500]
cv.imshow('Green', blank)
cv.rectangle(blank, (0,0), (250,250),color=(0,0,255), thickness=2) #thickness = 2
cv.imshow('RedRect', blank)
# cv.circle(blank, (250,250), radius=40,color=(255,0,0), thickness= -1)
# cv.imshow('BlueCir', blank)
# cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), color=(255,255,255), thickness= 3)
# cv.imshow('line', blank)
# cv.putText(blank, 'Hello', (200,200), fontFace = cv.FONT_HERSHEY_DUPLEX, fontScale= 2, color= (0,0,0), thickness= 4)
# cv.imshow('text', blank)
cv.waitKey(0)
