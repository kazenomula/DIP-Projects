import cv2 as cv
import numpy
import numpy as np
import matplotlib.pyplot as plt
from numpy import zeros

img_raw = cv.imread("../resource/img.png")
img_gray = cv.cvtColor(img_raw, cv.COLOR_BGR2GRAY)
cv.waitKey(0)

w = img_gray.shape[0]
h = img_gray.shape[1]


pad_img = np.pad(img_gray, ((1, 1), (1, 1)), 'constant', constant_values=(0, 0))

def unfold_matrix(X, k):
    n, m = X.shape[0:2]
    xx = zeros(((n - k + 1) * (m - k + 1), k ** 2))
    row_num = 0

    def make_row(x):
        return x.flatten()

    for i in range(n - k + 1):
        for j in range(m - k + 1):
            xx[row_num, :] = make_row(X[i:i + k, j:j + k])
            row_num = row_num + 1
    return xx

kernel = [1,1,1,1,1,1,1,1,1]
xfold=unfold_matrix(pad_img, 3)
res = np.matmul(xfold,kernel)
res/=9
res1 = res.reshape(w,h)
res1 *=1./255

A=1.7
res2 = A*img_gray-res1
res2 *= 1./255
gp2 = [img_gray, res1, res2]
for i in range(3):
    tmp_img = gp2[i]
    plt.subplot(1,3,i+1)
    plt.imshow(tmp_img, cmap='gray')
plt.show()