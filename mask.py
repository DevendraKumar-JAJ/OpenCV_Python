import cv2 
import numpy as np
image = cv2.imread('b.PNG')
mask = np.zeros(image.shape[:2], dtype=np.uint8)
h,w=mask.shape[:2]
cv2.circle(mask, (h//2,w//2), min(h,w)//2-20, 255, -1)

# Apply mask
masked_image = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
