import cv2

img=cv2.imread("img.jpg",1)
h,w=img.shape[:2]
if img is not None:
  # ystart:yend,xstart:xend
  cropedImg=img[h//2-400:h//2+400,w//2-250:w//2+250]
  h,w=cropedImg.shape[:2]
  (text_width, text_height), baseline = cv2.getTextSize("hello openCV", cv2.FONT_HERSHEY_TRIPLEX, 1, 2)
  textOnImg=cv2.putText(cropedImg,"Hello OpenCV",(w//2-text_width//2,50),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),2,cv2.LINE_4,False)
  print(text_width, text_height)
  cv2.imwrite("textOnImg.jpg",textOnImg)  
  cv2.imshow("Croped Img",textOnImg)
  cv2.imwrite("croped.jpg",textOnImg)
  cv2.waitKey(0)
  cv2.destroyAllWindows()