import cv2
import numpy as np

# Open an image maintaining its original color format, cast it to contain floating point
# values, convert all pixels to range [0, 1], and show the image in a window.


# Load an image in grayscale
img = cv2.imread('Ellie.jpg')

thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1]

cv2.imshow('ellie_hello', thresh1)

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Wait for 's' key to save and exit
    cv2.imwrite('Ellie-grayscale.jpg', img)
    cv2.destroyAllWindows()
