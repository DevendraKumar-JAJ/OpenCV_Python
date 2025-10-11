import cv2
import numpy as np
img1=cv2.imread("img.jpg",cv2.IMREAD_GRAYSCALE)

img1=np.zeros((300,300),dtype="uint8")
img2=np.zeros((300,300),dtype="uint8")

cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2,(100,100),(275,275),255,-1)
cv2.imshow("Circle",img1)
cv2.imshow("Rectangle",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

bnot=cv2.bitwise_not(img1)
bor=cv2.bitwise_or(img1,img2)
band=cv2.bitwise_and(img1,img2)

cv2.imshow("NOT",bnot)
cv2.imshow("OR",bor)
cv2.imshow("AND",band)
cv2.waitKey(0)
cv2.destroyAllWindows()