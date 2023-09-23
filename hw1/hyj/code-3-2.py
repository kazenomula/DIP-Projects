import cv2 as cv
import matplotlib.pyplot as plt
import time

img_raw = cv.imread("../resource/Fig0308(a)(fractured_spine).tif", cv.IMREAD_GRAYSCALE)
# img_gray = cv.cvtColor(img_raw, cv.COLOR_BGR2GRAY)
img_gray = img_raw
cv.imshow('Gray', img_gray)

w = img_gray.shape[0]
h = img_gray.shape[1]
print(f"Image: w{w} x h{h} x {img_gray.dtype}")

def histogram(img):
    count = [0]*256
    vals = []
    for i in range(w):
        for j in range(h):
            vals.append(img[i][j])
            count[img[i][j]] += 1

    return vals, count

t0 = time.time()
tmp0, count0 = histogram(img_gray)
t1 = time.time()
print(f"TIME: histogram spent {t1-t0}s")

plt.hist(tmp0, bins=256)  # 自动统计
plt.title('histogram')
plt.xlabel('grayscale')
plt.ylabel('rate')
plt.show()

def histogram_equalization(img, count0):
    preSum0 = [0]*256
    preSum0[0] = count0[0]
    for i in range(1,256):
        preSum0[i] = preSum0[i-1] + count0[i]
    pixels = w*h

    tmp1 = []
    for i in range(w):
        for j in range(h):
            r = img_gray[i][j]
            img_gray[i][j] = 255 * preSum0[r] / pixels
            tmp1.append(img_gray[i][j])
    
    return tmp1


t0 = time.time()
tmp1 = histogram_equalization(img_gray, count0)
t1 = time.time()
print(f"TIME: histogram eq spent {t1-t0}s")

plt.hist(tmp1, bins=256)
plt.title('histogram')
plt.xlabel('grayscale')
plt.ylabel('rate')
plt.show()

cv.imshow('Gray', img_gray)
cv.waitKey(0)