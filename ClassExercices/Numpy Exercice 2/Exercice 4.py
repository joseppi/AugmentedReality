import numpy as np
import cv2

# Open an image and apply a vignetting effect on its borders.


# Load an image in grayscale
img = cv2.imread('Ellie.jpg',0)
cv2.imshow('ellie',img)

k = cv2.waitKey(0)

if k == 27:
    # Wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Wait for 's' key to save and exit
    cv2.imwrite('Ellie-grayscale.jpg',img)
    cv2.destroyAllWindows()
