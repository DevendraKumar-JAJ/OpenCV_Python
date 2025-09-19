import cv2

# Load grayscale image
gray_img = cv2.imread("h.png", cv2.IMREAD_GRAYSCALE)

# Apply a colormap (e.g., JET, VIRIDIS, etc.)
colored_img = cv2.applyColorMap(gray_img, cv2.COLORMAP_COOL)

# Save or show the result
cv2.imwrite("colorized.jpg", colored_img)
colored_img=cv2.resizeWindow()
cv2.imshow("Colorized", colored_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
