import numpy as np
import cv2

# Open an image and increase its contrast by applying the following formula on its pixels:
# final_color = (color - min) / (max - min), where min = 50, and max = 200. The resulting
# final color will need to be clamped to the range [0, 1] and rescaled to [0, 255].


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
