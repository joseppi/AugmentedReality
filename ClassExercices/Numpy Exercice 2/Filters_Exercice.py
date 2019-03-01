import numpy as np
import cv2

img = cv2.imread('lenna_noise.png', cv2.IMREAD_GRAYSCALE)

img = np.float64(img) / 255.0
print('The shape of the image is {}'.format(img.shape))
print('The num of dimensions of the image is {}'.format(len(img.shape)))
print('The internal type of the image is {}'.format(img.dtype))
# blur = cv2.blur(img, (16, 1))
# 11. Create a 5x5 matrix of rows from 1 to 5
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
cv2.imshow('Image', np.uint8(blur * 255.0))
# cv2.imshow('Image', np.uint8(img * 255.0))

k = cv2.waitKey(0)
