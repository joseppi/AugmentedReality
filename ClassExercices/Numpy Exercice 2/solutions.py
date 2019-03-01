import cv2
import numpy as np


def ex1():
    print('Ex1 - Open an image maintaining its original color format'
          'and print its internal data type, its shape, its number of'
          'dimensions, and show it')
    img = cv2.imread('Ellie.jpg', cv2.IMREAD_ANYCOLOR)
    print('The shape of the image is {}'.format(img.shape))
    print('The num of dimensions of the image is {}'.format(len(img.shape)))
    print('The internal type of the image is {}'.format(img.dtype))
    cv2.imshow('ellie', img)
    cv2.waitKey(0)


def ex2():
    print('Ex2 - Open an image maintaining its original color format'
          'cast it to floats, convert it to range [0, 1] and show it')
    img = cv2.imread('img/sonic.jpg', cv2.IMREAD_ANYCOLOR)
    img = np.float64(img) / 255.0
    cv2.imshow('Image', np.uint8(img * 255.0))
    cv2.waitKey(0)


def ex3():
    print('Ex3 - Create a binary image (0s and 1s) from an image file and show it')
    img = cv2.imread('img/sonic.jpg', cv2.IMREAD_GRAYSCALE)
    threshold = 125
    img = np.float64(img > threshold)
    cv2.imshow('Image', np.uint8(img * 255))
    cv2.waitKey(0)


def ex4():
    print('Ex4 - Open an image and apply a vignetting effect on its borders')
    img = cv2.imread('img/sonic.jpg', cv2.IMREAD_ANYCOLOR)
    img = np.float64(img)
    height, width, _ = img.shape
    centeri = height / 2
    centerj = width / 2
    radius = np.sqrt(width*width + height*height) / 2.0
    for i in range(0, height):
        for j in range(0, width):
            dist = np.sqrt((centeri - i)**2 + (centerj - j)**2)
            vignetting_factor = 1.0 - (dist / radius)**2
            img[i, j] *= vignetting_factor
    cv2.imshow('Image', np.uint8(img))
    cv2.waitKey(0)


def ex5():
    print("Ex5 - Open an image and invert its colors")
    img = cv2.imread('img/sonic.jpg', cv2.IMREAD_ANYCOLOR)
    img[:] = 255 - img
    cv2.imshow('Image', img)
    cv2.waitKey(0)


def ex6():
    print("Ex6 - Open an image and tint it 50% with blue")
    img = cv2.imread('img/sonic.jpg', cv2.IMREAD_ANYCOLOR)
    img = np.float64(img)
    blue = np.array([255.0, 0.0, 0.0]).reshape((1, 1, 3))
    img = 0.5 * img + 0.5 * blue
    cv2.imshow('Image', np.uint8(img))
    cv2.waitKey(0)
    pass


def ex7():
    print("Ex7 - Open an image and increase the contrast by applying the"
          "following formula on its pixels: col = (col - min) / (max - min),"
          "where min=50 and max=200. Clamp values so they are in the range [0,1]"
          ", and rescale them to range [0,255] before showing it.")
    img = cv2.imread('img/sonic.jpg', cv2.IMREAD_ANYCOLOR)
    img = np.float64(img)
    min = 50
    max = 200
    img = (img - min) / (max - min)
    img = np.clip(img, 0.0, 1.0)
    cv2.imshow('Image', np.uint8(img * 255.0))
    cv2.waitKey(0)
    pass


def execute():
    ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    pass
