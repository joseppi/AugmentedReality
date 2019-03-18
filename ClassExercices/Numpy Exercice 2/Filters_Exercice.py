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
img4 = cv2.imread('../img/sonic.jpg', cv2.IMREAD_GRAYSCALE)
rows, columns = img4.shape
canny = cv2.Canny(img4, columns, rows)
# ___BLUR___
blur4 = np.zeros(shape=(rows, columns))

kernel_blur = np.zeros((4, 4))
kernel_blur[0:4, 0:4] = 1.0/9.0

for i in range(1, rows - 2):
    for j in range(1, columns - 2):
        temp = img4[i-1:i+3, j-1:j+3] * kernel_blur
        pixel = temp.sum()
        blur4[i, j] = pixel

print("Finished Blur")

# __Direction data Init___
pixel_x = np.zeros(shape=(rows, columns))
pixel_y = np.zeros(shape=(rows, columns))


D = np.zeros(shape=(rows, columns))  # Direction
M = np.zeros(shape=(rows, columns))  # Maximum

# __SOBEL___
Gx = np.zeros(shape=(rows, columns))
Gy = np.zeros(shape=(rows, columns))

rows = rows - 1
columns = columns - 1

kernel_horizontal = np.array([[-1, 0, 1],
                              [-2, 0, 2],
                              [-1, 0, 1]])

kernel_vertical = np.array([[-1, -2, -1],
                            [0, 0, 0],
                            [1, 2, 1]])

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
print("Starting Direction")
# dir_list = [0, 45, 90, 135]
for i in range(1, rows):
    for j in range(1, columns):
        degree = np.arctan2(pixel_x[i][j], pixel_y[i][j]) * 180 / 3.14159262359939
        if 45.0 <= degree > 0.0:
            if degree > 22.5:
                D[i][j] = 45
            else:
                D[i][j] = 0
        elif 90.0 <= degree > 45.0:
            if degree > 67.5:
                D[i][j] = 90
            else:
                D[i][j] = 45
        elif 135.0 <= degree > 90.0:
            if degree > 112.5:
                D[i][j] = 135
            else:
                D[i][j] = 90

for i in range(1, rows):
    for j in range(1, columns):
        if D[i][j] == 0:
            left = G[i][j-1]
            right = G[i][j+1]
            if left > G[i][j] or right > G[i][j]:
                M[i][j] = 0.0
            else:
                M[i][j] = 255.0

        if D[i][j] == 45:
            right_top = G[i+1][j+1]
            left_down = G[i-1][j-1]
            if right_top > G[i][j] or left_down > G[i][j]:
                M[i][j] = 0
            else:
                M[i][j] = 255.0

        if D[i][j] == 90:
            top = G[i+1][j]
            down = G[i-1][j]
            #  print(top,down)
            if top > G[i][j] or down > G[i][j]:
                M[i][j] = 0
            else:
                M[i][j] = 255.0

        if D[i][j] == 135:
            top_left = G[i+1][j-1]
            down_right = G[i-1][j+1]
            if top_left > G[i][j] or down_right > G[i][j]:
                M[i][j] = 0
            else:
                M[i][j] = 255.0

print("Finish Direction")


#  Show Images
cv2.imshow('Original', img4)
cv2.imshow('Blur', np.uint8(blur4))
cv2.imshow('Gx', np.uint8(Gx))
cv2.imshow('Gy', np.uint8(Gy))
cv2.imshow('G', np.uint8(G))
cv2.imshow('Final_image', np.uint8(M))
cv2.imshow('Canny', canny)

k = cv2.waitKey(0)
