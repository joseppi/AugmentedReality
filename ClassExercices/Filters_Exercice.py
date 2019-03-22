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

# -------------------Canny Edge Detector Filter----------------------------
img4 = cv2.imread('img/sonic.jpg', cv2.IMREAD_GRAYSCALE)
assert img4 is not None
rows, columns = img4.shape
print(rows, columns)
canny = cv2.Canny(img4, 50, 100)

# ___BLUR___
blur4 = np.zeros(shape=(rows, columns))

kernel_blur = np.zeros((3, 3))
kernel_blur[0:3, 0:3] = 1.0/9.0

for i in range(1, rows - 1):
    for j in range(1, columns - 1):
        temp = img4[i-1:i+2, j-1:j+2] * kernel_blur
        pixel = temp.sum()
        blur4[i, j] = pixel

#  blur4 = cv2.GaussianBlur(img4, (3, 3), 1, 1)

print("Finished Blur")

# __Direction data Init___
pixel_x = np.zeros(shape=(rows, columns))
pixel_y = np.zeros(shape=(rows, columns))


D = np.zeros(shape=(rows, columns))  # Direction
M = np.zeros(shape=(rows, columns))  # Maximum
FM = np.zeros(shape=(rows, columns))  # Final Max

# __SOBEL___
Gx = np.zeros(shape=(rows, columns))
Gy = np.zeros(shape=(rows, columns))

rows = rows - 1
columns = columns - 1

kernel_horizontal = np.array([[1, 0, -1],
                              [2, 0, -2],
                              [1, 0, -1]])

kernel_vertical = np.array([[1, 2, 1],
                            [0, 0, 0],
                            [-1, -2, -1]])

# ___X___
for i in range(1, rows):
    for j in range(1, columns):
        temp = blur4[i-1:i+2, j-1:j+2] * kernel_horizontal  # Create a temporal matrix that stores the result of the multiplication of the kernel and the image.
        pixel = temp.sum()  # Sum Everything inside that temporal matrix and create a pixel with the result
        pixel_x[i, j] = pixel
        Gx[i, j] = pixel  # Add the resulting pixel to a matrix called Gx

print("Finished Gx")

# ___Y___
for i in range(1, rows):
    for j in range(1, columns):
        temp = blur4[i-1:i+2, j-1:j+2] * kernel_vertical
        pixel = temp.sum()
        pixel_y[i, j] = pixel
        Gy[i, j] = pixel

print("Finished Gy")

G = np.sqrt(Gx**2 + Gy**2)

# ___Direction___
# dir_list = [0, 45, 90, 135]
for i in range(1, rows):
    for j in range(1, columns):
        rad = np.arctan2(pixel_y[i][j], pixel_x[i][j])
        degree = rad * 180 / np.pi
        if degree < 0:
            degree = degree + 180

        if 45.0 > degree >= 0.0:
            if degree > 22.5:
                D[i][j] = 45.0
            else:
                D[i][j] = 0.0
        if 90.0 > degree >= 45.0:
            if degree > 67.5:
                D[i][j] = 90.0
            else:
                D[i][j] = 45.0
        if 135.0 > degree >= 90.0:
            if degree > 112.5:
                D[i][j] = 135.0
            else:
                D[i][j] = 90.0
        if 180 >= degree >= 135.0:
            if degree > 157.5:
                D[i][j] = 0.0
            else:
                D[i][j] = 135.0
print("Finish Direction")

for i in range(1, rows):
    for j in range(1, columns):
        if D[i][j] == 0:#
            left = G[i][j-1]
            right = G[i][j+1]
            if left > G[i][j] or right > G[i][j]:
                M[i][j] = 0.0
            else:
                M[i][j] = G[i][j]
        if D[i][j] == 90:
            top = G[i-1][j]
            down = G[i+1][j]
            if top > G[i][j] or down > G[i][j]:
                M[i][j] = 0.0
            else:
                M[i][j] = G[i][j]
        if D[i][j] == 45:
            right_top = G[i+1][j+1]
            left_down = G[i-1][j-1]
            if right_top >= G[i][j] or left_down >= G[i][j]:
                M[i][j] = 0.0
            else:
                M[i][j] = G[i][j]
        if D[i][j] == 135:
            top_left = G[i+1][j-1]
            down_right = G[i-1][j+1]
            if top_left >= G[i][j] or down_right >= G[i][j]:
                M[i][j] = 0.0
            else:
                M[i][j] = G[i][j]
print("Finish Max")
# Thresh Hold
for i in range(1, rows):
    for j in range(1, columns):
        if M[i][j] < 50.0:
            FM[i][j] = 0.0
        if M[i][j] > 150.0:
            FM[i][j] = 255.0
        if 150.0 < M[i][j] > 50.0:
            kernel_threshold = img4[i - 1:i + 2, j - 1:j + 2]
            if kernel_threshold.max() > 150.0:
                FM[i][j] = 255.0
            else:
                FM[i][j] = 0


#  Show Images
cv2.imshow('Original', np.uint8(img4))
cv2.imshow('G', np.uint8(G))
cv2.imshow('D', np.uint8(D))
cv2.imshow('M', np.uint8(M))
cv2.imshow('Final_image', np.uint8(FM))
cv2.imshow('Canny', canny)

k = cv2.waitKey(0)
