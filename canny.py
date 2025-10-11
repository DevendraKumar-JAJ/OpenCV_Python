import cv2

img=cv2.imread("img.jpg",cv2.IMREAD_GRAYSCALE)

img=cv2.resize(img,(500,500))


canny=cv2.Canny(img,111,200,cv2.THRESH_BINARY)
cv2.imshow("Canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("canny.jpg",canny)