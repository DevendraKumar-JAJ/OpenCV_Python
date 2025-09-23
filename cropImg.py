import cv2

img=cv2.imread("img.jpg",1)

if img is not None:
  # ystart:yend,xstart:xend
  h,w=img.shape[:2]
  cropedImg=img[h//2-400:h//2+400,w//2-250:w//2+250]
  cv2.imshow("Croped Img",cropedImg)
  cv2.imwrite("croped.jpg",cropedImg)
  cv2.waitKey(0)
  cv2.destroyAllWindows()