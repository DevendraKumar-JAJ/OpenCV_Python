import cv2
import numpy as np

img=cv2.imread('img.jpg')
# () is allways odd
# 0 is sigmaX
# sigma is used to calculate kernel
# if sigma is 0 then it is calculated from kernel size
aspect_ratio=img.shape[1]/img.shape[0]
img=cv2.resize(img,(600,int(600/aspect_ratio)))
# sharping filter
kernel = np.array([[0, -1, 0], 
                   [-1, 5,-1], 
                   [0, -1, 0]])

sharpened = cv2.filter2D(img, -1, kernel)
cv2.imshow('Original',img)
cv2.imshow('Sharpened',sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('sharpened.jpg',sharpened)
# parameters
# ddepth: Desired depth of the destination image. If it is negative,
# it will be the same as the source image.
# kernel: Convolution kernel (or rather a correlation kernel),
# a single-channel floating point matrix. If you want to apply different kernels

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()  
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imshow('Original Video', frame)
    sharpened_frame = cv2.filter2D(frame, -2, kernel)
    mblur=cv2.bilateralFilter(sharpened_frame,9,75,75)
    
    cv2.imshow('Sharpened Video', mblur)
    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('sharpened_frame.jpg', mblur)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# to different channels, split the image and process them in a loop.
# anchor: Anchor of the kernel that indicates the relative position of a