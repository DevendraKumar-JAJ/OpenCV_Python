import cv2

img=cv2.imread("img.jpg",1)

if img is not None:
  h,w,s=img.shape
  center=(w//2,h//2)
  rmatix=cv2.getRotationMatrix2D(center,45,1.0)
  rimg=cv2.warpAffine(img,rmatix,(h,w))
  cv2.imshow("Rotated",rimg)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  
  fimg=cv2.flip(img,-1)
  cv2.imshow("Flip",fimg)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  
  