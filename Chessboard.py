# Slide 16 https://docs.google.com/presentation/d/1j42b3UMDDCuHTfeI-qm-bjWx8r0dw_RUe3p5UrekRLg/edit#slide=id.gc62a6d4f43_0_0

import numpy as np
import cv2

mat = np.full((800,800), 255, dtype = np.uint8)

for i in range(800):
    for j in range(800):
        if(int(i/100)%2 == 0 and int(j/100)%2 == 0) or (int(i/100)%2 != 0 and int(j/100)%2 != 0):
            mat[i][j] = 0

#Logic: We have a completely white 800 * 800 block in which we need blocks of black. We can achieve this by checking if the digit at 100th place is even or odd
#and use the above to make alt blocks. While doing (i/100) the default output is float which needs to be converted to int to check for condition. 

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', mat)
cv2.waitKey(0)
cv2.destroyAllWindows()