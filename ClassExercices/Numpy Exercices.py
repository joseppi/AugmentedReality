import numpy as np
import cv2

# 1. Create a vector of 10 floats (zeros)
arr = np.arange(0, 10)
for i in range(0, 10):
    arr[i] = 0

# print(arr)

# 2. Create a vector of 10 float (zeros) whose 5th element is one
arr2 = np.arange(0, 10)
for i in range(0, 10):
    if i == 4:
        arr2[i] = 1
    else:
        arr2[i] = 0

# print(arr2)

# 3. Create a vector of integers going from 10 to 49
arr3 = np.arange(0, 40)
for i in range(0, 40):
    int_in_arr = i
    arr3[i] = int_in_arr + 10

# print(arr3)

# 4. Create a matrix of 3x3 floats going from 1 to 9
matrix = np.arange(0,9)
matrix = matrix.reshape(3, 3)
num = 0
for i in range(0, 3):
    for y in range(0, 3):
        num = num + 1
        matrix[i, y] = num

# print(matrix)

# 5. Create a matrix of 3x3 floats going from 1 to 9 and flip it horizontally
matrix2 = np.arange(0,9)
matrix2 = matrix2.reshape(3, 3)
matrixh = np.arange(0,9)
matrixh = matrixh.reshape(3, 3)
num = 0
for i in range(0, 3):  # rows
    for y in range(0, 3):  # column
        num = num + 1
        matrix2[i, y] = num

for i in range(0, 3):  # rows
    for y in range(0, 3):  # column
        get_row_num = 2 - y
        matrixh[i, y] = matrix2[i, get_row_num]


# print(matrixh)

# 6. Create a matrix of 3x3 floats going from 1 to 9 and flip it vertically
matrix3 = np.arange(0, 9)
matrix3 = matrix2.reshape(3, 3)
matrixv = np.arange(0, 9)
matrixv = matrixh.reshape(3, 3)
num = 0
for i in range(0, 3):  # rows
    for y in range(0, 3):  # column
        num = num + 1
        matrix3[i, y] = num

for i in range(0, 3):  # rows
    for y in range(0, 3):  # column
        get_row_num = 2 - y
        matrixv[y, i] = matrix3[i, get_row_num]

# print(matrixv)

# 7. Create a 3x3 identity matrix
matrix4 = np.arange(0,9)
matrix4 = matrix4.reshape(3, 3)
num = 0
for i in range(0, 3):
    for y in range(0, 3):
        if i == y:
            matrix4[i, y] = 1
        else:
            matrix4[i, y] = 0

# print(matrix4)

# 8. Create a 3x3 matrix of random values
matrix5 = np.arange(0, 9)
matrix5 = matrix5.reshape(3, 3)
num = 0
for i in range(0, 3):
    for y in range(0, 3):
        matrix5[i, y] = np.random.randint(0, 100, 1)

# print(matrix5)

# 9. Create a random vector of 10 numbers and compute the mean value
arr4 = np.random.randint(0, 100, 10)
num_to_sum = 0
for i in range(0, 10):
    num_to_sum = num_to_sum + arr4[i]

num_to_sum = num_to_sum / 10

# print(arr4)
# print(num_to_sum)

# 10. Create a 10x10 array of zeros surrounded/framed by ones
arr5 = np.arange(0, 100)
arr5 = np.zeros(shape=(10, 10))

for i in range(0, 10):  # rows
    for y in range(0, 10):  # column
        if y == 0:
            arr5[i, y] = 1
        elif y == 9:
            arr5[i, y] = 1
        elif i == 0:
            arr5[i, y] = 1
        elif i == 9:
            arr5[i, y] = 1
# arr5 = np.ones((11,11))
# arr5 = arr5[1:-1,1:-1] = 0

# print(arr5)

# 11. Create a 5x5 matrix of rows from 1 to 5
arr6 = np.arange(0, 50)
arr6 = np.zeros(shape=(5, 5))
num2 = 0
for i in range(0, 5):  # rows
    num2 = 0
    for y in range(0, 5):  # column
        num2 = num2 + 1
        arr6[i][y] = num2

# print(arr6)
# 12. Create a 1-dimensional array of 9 random integers and reshape it to a 3x3 matrix of
# floats
matrix6 = np.arange(0, 9)
matrix6 = np.random.randint(0, 100, 9)
matrix6 = matrix5.reshape(3, 3)

# print(matrix6)

# 13. Create a 5x5 matrix of random values and subtract its average from it
matrix7 = np.arange(0, 25)
matrix7 = np.random.randint(0, 10, 25)
matrix7 = matrix7.reshape(5, 5)
num_to_sum2 = 0
for i in range(0, 5):  # rows
    for y in range(0, 5):  # column
        num_to_sum2 = num_to_sum2 + matrix7[i][y]

num_to_sum2 = num_to_sum2/9

# print(matrix7)
# print(num_to_sum2)

# 14. Create a 5x5 matrix of random values and subtract the average of each row to each row
matrix8 = np.arange(0, 25)
matrix8 = np.random.randint(0, 10, 25)
matrix8 = matrix8.reshape(5, 5)
num_to_sum3 = 0
for i in range(0, 5):  # rows
    for y in range(0, 5):  # column
        num_to_sum3 = num_to_sum3 + matrix8[i][y]

num_to_sum3 = num_to_sum3/9

# print(matrix8)

# 15. Create an array of 5x5 random values and return the value that is closer to 0.5
# matrix9 = np.arange(0,25)
# num3 = matrix9.flat
# num3 = np.abs(matrix9)

# 16. Make a 3x3 matrix of random numbers from 0 to 10 and count how many of them are > 5
# matRand4 = np.random.randint(0,10,9).reshape(3,3)
# vec4 = matRand4.reshape(9)
# vec4[vec4 > 5]

# 17. Create a horizontal gradient image of 64x64 that goes from black to white
# Load an image in something

mat = np.zeros((64, 64))
gradient = np.arange(0.0, 64.0)
gradient = gradient / 63.0# with this the gradient goes from 0 to 1
gradient = gradient * 255.0
mat += gradient
mat = np.uint8(mat)
# cv2.imshow("gradient", mat)


# 18. Create a vertical gradient image of 64x64 that goes from black to white
mat2 = np.zeros((64, 64))
gradient2 = np.arange(0.0, 64.0)
gradient2 = gradient2 / 63.0 # with this the gradient goes from 0 to 1
gradient2 = gradient2 * 255.0

mat2 += gradient2
mat2 = mat2.transpose()
mat2 = np.uint8(mat2)

# cv2.imshow("gradient2", mat2)

# 19. Create a 3-component white image of 64x64 pixels and set the blue component to zero
# (the result should be yellow)
yellow_img = np.uint8(np.ones((64, 64, 3)))  # bgr
yellow_img[0:, 0:, 0] = 0
yellow_img *= 255

#  cv2.imshow("Yellow", yellow_img)

# 20. Create a 3-component white image of 64x64 pixels, set the blue component of the
# top-left part to zero (the result should be yellow) and the red component of the
# bottom-right part to zero (the result should be cyan
yellow_img = np.uint8(np.ones((64, 64, 3)))  # bgr
yellow_img[0:32, 0:32, 0] = 0
yellow_img[32:64, 32:64, 2] = 0
yellow_img *= 255

#  cv2.imshow("Yellow", yellow_img)

# 21. Open an image and insert black horizontal scan lines at 50%
yellow_img = np.uint8(np.ones((64, 64, 3)))  # bgr
yellow_img[:, ::2, :] = [0, 0, 0]
yellow_img *= 255

#  cv2.imshow("Yellow", yellow_img)

# 22. Open an image and insert black vertical scan lines at 50%
yellow_img = np.uint8(np.ones((64, 64, 3)))  # bgr
yellow_img[::2, :, :] = [0, 0, 0]
yellow_img *= 255

cv2.imshow("Yellow", yellow_img)

cv2.waitKey(0)
