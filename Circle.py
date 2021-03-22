# Slide 16 https://docs.google.com/presentation/d/1j42b3UMDDCuHTfeI-qm-bjWx8r0dw_RUe3p5UrekRLg/edit#slide=id.gc62a6d4f43_0_0

import numpy as np
import math
import cv2

mat = np.full((800,800), 255, dtype=np.uint8)

for i in range(800):
    for j in range(800):
        if math.sqrt((400 - i)**2 + (400 - j)**2) <= 200:
            mat[i][j] = 0

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', mat)
cv2.waitKey(0)
cv2.destroyAllWindows()