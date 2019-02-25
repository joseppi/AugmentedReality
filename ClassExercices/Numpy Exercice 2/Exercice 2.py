import cv2
import numpy as np
from matplotlib import pyplot as plt

# Open an image maintaining its original color format, cast it to contain floating point
# values, convert all pixels to range [0, 1], and show the image in a window.


# Load an image in grayscale
img = cv2.imread('Ellie.jpg')

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


cv2.imshow('ellie', img)

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Wait for 's' key to save and exit
    cv2.imwrite('Ellie-grayscale.jpg', img)
    cv2.destroyAllWindows()
