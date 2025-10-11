import cv2
img=cv2.imread('img.jpg')
# () is allways odd
# 0 is sigmaX
# sigma is used to calculate kernel
# if sigma is 0 then it is calculated from kernel size  
aspect_ratio=img.shape[1]/img.shape[0]
img=cv2.resize(img,(600,int(600/aspect_ratio)))
# average blur

gblur=cv2.GaussianBlur(img,(9,9),3)
cv2.imshow('Original',img)
cv2.imshow('Gaussian Blurred',gblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('gblur.jpg',gblur)

# median blur
# it is very effective in removing salt and pepper noise
mblur=cv2.medianBlur(img,9)
cv2.imshow('Median Blurred',mblur)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('mblur.jpg',mblur)

# bilateral filter
# it is very effective in removing noise while keeping edges sharp
bfilter=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral Filtered',bfilter)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('bfilter.jpg',bfilter)

# parameters
# d: Diameter of each pixel neighborhood that is used during filtering.
# If it is non-positive, it is computed from sigmaSpace.
# sigmaColor: Filter sigma in color space. A larger value of the parameter means that
# farther colors within the pixel neighborhood (see sigmaSpace) will be mixed together,
# resulting in larger areas of semi-equal color.
# sigmaSpace: Filter sigma in coordinate space. A larger value of the parameter means that
# farther pixels will influence each other as long as their colors are close enough
# (see sigmaColor). When d>0, it specifies the neighborhood size regardless of sigmaSpace.
# Otherwise, d is proportional to sigmaSpace.
# Note: For a color image, the filtering is applied to each channel
# independently, but the neighborhood is selected based on Euclidean
# distance in the color space.