import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros

img_raw = cv.imread("img_1.png")
img_gray = cv.cvtColor(img_raw, cv.COLOR_BGR2GRAY)

w = img_gray.shape[0]
h = img_gray.shape[1]
if w>272 or h>352:
    img_gray = cv.resize(img_gray,(272,352))

tes = [[j for j in range(256)] for i in range(256)]
tes = np.array(tes)



dot9 = [[255,255,255],[255,255,255],[255,255,255]]
dot8 = [[255,0,255],[255,255,255],[255,255,255]]
dot7 = [[255,0,255],[255,255,255],[255,255,0]]
dot6 = [[0,0,255],[255,255,255],[255,255,0]]
dot5 = [[0,0,255],[255,255,255],[0,255,0]]
dot4 = [[0,0,0],[255,255,255],[0,255,0]]
dot3 = [[0,0,0],[255,255,0],[0,255,0]]
dot2 = [[0,0,0],[255,255,0],[0,0,0]]
dot1 = [[0,0,0],[0,255,0],[0,0,0]]
dot0 = [[0,0,0],[0,0,0],[0,0,0]]
dots=[dot0,dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9]

def halftoning(X):
    x = X.shape[0]
    y = X.shape[1]
    xout = zeros((x*3+1, y*3+1))
    for i in range(x):
        for j in range(y):
            tmp=int(X[i][j]/25.6)
            xout[i*3:i*3+3, j*3:j*3+3] = dots[tmp]

    return xout

res = halftoning(img_gray)

cv.imshow('Gray',res)
cv.waitKey(0)


tes1 = halftoning(tes)
plt.subplot(1,2,1)
plt.imshow(tes,cmap='gray')
plt.subplot(2,2,2)
plt.imshow(tes1,cmap='gray')
plt.show()