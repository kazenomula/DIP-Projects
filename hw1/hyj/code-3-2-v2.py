import cv2 as cv
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
    for i in range(w):
        for j in range(h):
            count[img[i][j]] += 1

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


# def histogram_equalization(img, count0):
#     preSum0 = [0]*256
#     preSum0[0] = count0[0]
#     for i in range(1,256):
#         preSum0[i] = preSum0[i-1] + count0[i]
#     pixels = w*h

#     for i in range(w):
#         for j in range(h):
#             r = img[i][j]
#             img[i][j] = 255 * preSum0[r] / pixels
    

# t0 = time.time()
# histogram_equalization(img_gray, count0)
# t1 = time.time()
# print(f"TIME: equalization spent {t1-t0}s")

# cv.imshow('Gray', img_gray)

# t0 = time.time()
# count1 = histogram(img_gray)
# t1 = time.time()
# print(f"TIME: histogram spent {t1-t0}s")

# plt.bar(range(256), count1)
# plt.title('histogram')
# plt.xlabel('grayscale')
# plt.ylabel('rate')
# plt.show()

# cv.waitKey(0)