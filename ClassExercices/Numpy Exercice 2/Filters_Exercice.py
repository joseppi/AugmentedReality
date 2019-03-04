import numpy as np
import cv2

# -------------------Normalized Box Filter-----------------------------

img = cv2.imread('lenna_noise.png', cv2.IMREAD_GRAYSCALE)
img = np.float64(img) / 255.0
print('The shape of the image is {}'.format(img.shape))
print('The num of dimensions of the image is {}'.format(len(img.shape)))
print('The internal type of the image is {}'.format(img.dtype))

blur = np.arange(0, 360000)
blur = np.zeros(shape=(600, 600))

kernel = np.zeros((3, 3))
kernel[0:3, 0:3] = 1.0/9.0


mat = np.zeros((3, 3))
for i in range(1, 599):
    for y in range(1, 599):
        print_mat = img[i-1:i+2, y-1:y+2]
        temp = img[i-1:i+2, y-1:y+2] * kernel
        pixel = temp.sum()
        blur[i, y] = pixel
# cv2.imshow('Image', np.uint8(blur * 255.0))

# ----------------------Gaussian Filter----------------------------
img2 = cv2.imread('lenna_noise.png', cv2.IMREAD_GRAYSCALE)
img2 = np.float64(img2) / 255.0

blur2 = np.arange(0, 360000)
blur2 = np.zeros(shape=(600, 600))

kernel2 = np.zeros((3, 3))
# kernel

# 1/4 /7 /4 /1
# 4/16/26/16/4
# 7/26/41/26/7
# 4/16/26/16/4
# 1/4 /7 /4 /1

kernel2[0:3, 0:3] = 1.0/9.0


mat = np.zeros((3, 3))
for i in range(1, 599):
    for y in range(1, 599):
        print_mat = img2[i-1:i+2, y-1:y+2]
        temp = img2[i-1:i+2, y-1:y+2] * kernel2
        pixel = temp.sum()
        blur2[i, y] = pixel
# cv2.imshow('Image', np.uint8(blur2 * 255.0))

# -------------------Median Filter----------------------------
img = cv2.imread('lenna_noise.png', cv2.IMREAD_GRAYSCALE)
img = np.float64(img) / 255.0
print('The shape of the image is {}'.format(img.shape))
print('The num of dimensions of the image is {}'.format(len(img.shape)))
print('The internal type of the image is {}'.format(img.dtype))

blur = np.arange(0, 360000)
blur = np.zeros(shape=(600, 600))

kernel = np.zeros((3, 3))
kernel[0:3, 0:3] = 1.0/9.0


mat = np.zeros((3, 3))
for i in range(1, 599):
    for y in range(1, 599):
        print_mat = img[i-1:i+2, y-1:y+2]
        temp = img[i-1:i+2, y-1:y+2] * kernel
        pixel = temp.sum()
        blur[i, y] = pixel
# cv2.imshow('Image', np.uint8(blur * 255.0))
k = cv2.waitKey(0)


