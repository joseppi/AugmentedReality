import numpy as np
import cv2

# Open an image maintaining its original color format and print its internal data type, its
# shape, its number of dimensions, and show it in a window.

# Load an image in grayscale
img = cv2.imread('Ellie.jpg')
cv2.imshow('ellie', img)

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Wait for 's' key to save and exit
    cv2.imwrite('Ellie-grayscale3.jpg',img)
    cv2.destroyAllWindows()
