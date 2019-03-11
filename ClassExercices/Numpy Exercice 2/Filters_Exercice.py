import numpy as np
import cv2

# # -------------------Normalized Box Filter-----------------------------

# img = cv2.imread('lenna_noise.png', cv2.IMREAD_GRAYSCALE)
# img = np.float64(img) / 255.0
#
# blur = np.arange(0, 360000)
# blur = np.zeros(shape=(600, 600))
#
# kernel = np.zeros((3, 3))
# kernel[0:3, 0:3] = 1.0/9.0
#
#
# mat = np.zeros((3, 3))
# for i in range(1, 599):
#     for y in range(1, 599):
#         print_mat = img[i-1:i+2, y-1:y+2]
#         temp = img[i-1:i+2, y-1:y+2] * kernel
#         pixel = temp.sum()
#         blur[i, y] = pixel

# cv2.imshow('Image', np.uint8(blur * 255.0))

# # ----------------------Gaussian Filter----------------------------
# img2 = cv2.imread('lenna_noise.png', cv2.IMREAD_GRAYSCALE)
# img2 = np.float64(img2) / 255.0
#
# blur2 = np.arange(0, 360000)
# blur2 = np.zeros(shape=(600, 600))
#
# kernel2 = np.zeros((3, 3))
# # kernel
#
# # 1/4 /7 /4 /1
# # 4/16/26/16/4
# # 7/26/41/26/7
# # 4/16/26/16/4
# # 1/4 /7 /4 /1
#
# kernel2[0:3, 0:3] = 1.0/9.0
#
#
# mat = np.zeros((3, 3))
# for i in range(1, 599):
#     for y in range(1, 599):
#         print_mat = img2[i-1:i+2, y-1:y+2]
#         temp = img2[i-1:i+2, y-1:y+2] * kernel2
#         pixel = temp.sum()
#         blur2[i, y] = pixel
# # cv2.imshow('Image', np.uint8(blur2 * 255.0))
#
# # -------------------Median Filter----------------------------
# img3 = cv2.imread('lenna_noise.png', cv2.IMREAD_GRAYSCALE)
# img3 = np.float64(img) / 255.0
#
# blur3 = np.arange(0, 360000)
# blur3 = np.zeros(shape=(600, 600))
#
# kernel3 = np.zeros((3, 3))
# kernel3[0:3, 0:3] = 1.0/9.0
#
#
# mat = np.zeros((3, 3))
# for i in range(1, 599):
#     for y in range(1, 599):
#         print_mat = img[i-1:i+2, y-1:y+2]
#         temp = img[i-1:i+2, y-1:y+2] * kernel3
#         pixel = temp.sum()
#         blur3[i, y] = pixel
# # cv2.imshow('Image', np.uint8(blur * 255.0))

# -------------------Median Filter----------------------------
img4 = cv2.imread('lenna_noise.png', cv2.IMREAD_GRAYSCALE)
columns, rows = img4.shape
print(rows, columns)
Gx = np.zeros(shape=(rows, columns))

Gy = np.zeros(shape=(rows, columns))

kernel_horizontal = np.array([[-3, 0, 3],
                             [-10, 0, 10],
                             [-3, 0, 3]])

kernel_vertical = np.zeros((3, 3))
kernel_vertical[0, 0] = -3
kernel_vertical[0, 1] = -10
kernel_vertical[0, 2] = -3

kernel_vertical[1, 0] = 0
kernel_vertical[1, 1] = 0
kernel_vertical[1, 2] = 0

kernel_vertical[2, 0] = 3
kernel_vertical[2, 1] = 10
kernel_vertical[2, 2] = 3

for i in range(1, rows - 1):
    for j in range(1, columns - 1):
        temp = img4[i-1:i+2, j-1:j+2] * kernel_horizontal  # Create a temporal matrix that stores the result of the multiplication of the kernel and the image.
        pixel = temp.sum()  # Sum Everything inside that temporal matrix and create a pixel with the result
        Gx[i, j] = pixel  # Add the resulting pixel to a matrix called Gx

for i in range(1, rows - 1):
    for j in range(1, columns - 1):
        temp = img4[i-1:i+2, j-1:j+2] * kernel_vertical
        pixel = temp.sum()
        Gy[i, j] = pixel

G = np.sqrt(Gx**2 + Gy**2)
cv2.imshow('Gx', np.uint8(Gx))
cv2.imshow('Gy', np.uint8(Gy))
cv2.imshow('Final image', np.uint8(G))
k = cv2.waitKey(0)
