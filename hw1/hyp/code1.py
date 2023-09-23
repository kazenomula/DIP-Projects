import cv2 as cv
import matplotlib.pyplot as plt

img_raw = cv.imread("../resource/Fig0308(a)(fractured_spine).tif")
img_gray = cv.cvtColor(img_raw, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',img_gray)
cv.waitKey(0)

w = img_gray.shape[0]
h = img_gray.shape[1]

count = [0 for i in range(256)]
tmp = []
for i in range(w):
    for j in range(h):
        tmp.append(img_gray[i][j])
        count[img_gray[i][j]] += 1

plt.hist(tmp,bins=256)
plt.title('histogram')
plt.xlabel('grayscale')
plt.ylabel('rate')
plt.show()

count1 = [0 for i in range(256)]
tmp1 = []
for i in range(w):
    for j in range(h):
        sum = 0
        for k in range(img_gray[i][j]):
            sum += count[k]
        img_gray[i][j] = 255*sum/(w*h)
        tmp1.append(img_gray[i][j])
        count1[img_gray[i][j]] += 1
cv.imshow('Gray', img_gray)
cv.waitKey(0)
plt.hist(tmp1,bins=256)
plt.title('histogram')
plt.xlabel('grayscale')
plt.ylabel('rate')
plt.show()

