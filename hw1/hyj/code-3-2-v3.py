import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

img_raw = cv.imread("../resource/Fig0308(a)(fractured_spine).tif", cv.IMREAD_GRAYSCALE)
img_gray = img_raw
cv.imshow('Gray', img_gray)

w = img_gray.shape[0]
h = img_gray.shape[1]
print(f"Image: w{w} x h{h} x {img_gray.dtype}")

def histogram(img):
    count = [0]*256
    flat_img = img.flatten()  # 将二维图像数组逻辑展平成一维

    for pixel_value in flat_img:
        count[pixel_value] += 1

    return count

t0 = time.time()
count0 = histogram(img_gray)
t1 = time.time()
print(f"TIME: histogram spent {t1-t0}s")

plt.bar(range(256), count0)
plt.title('histogram')
plt.xlabel('grayscale')
plt.ylabel('rate')
plt.show()


def histogram_equalization(img, count0):
    pixels = img.size  # 图像中的总像素数
    cdf = np.cumsum(count0)  # 计算累积分布函数

    img = cdf[img] * 255 // pixels  # 应用均衡化公式

    return img

t0 = time.time()
histogram_equalization(img_gray, count0)
t1 = time.time()
print(f"TIME: equalization spent {t1-t0}s")

cv.imshow('Gray', img_gray)

t0 = time.time()
count1 = histogram(img_gray)
t1 = time.time()
print(f"TIME: histogram spent {t1-t0}s")

plt.bar(range(256), count1)
plt.title('histogram')
plt.xlabel('grayscale')
plt.ylabel('rate')
plt.show()

cv.waitKey(0)