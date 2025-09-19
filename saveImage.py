import  cv2 as cv2
# img = cv2.imread('./img.png')
# if img is None:
#     print("Error: Image not loaded.")
# else:
#     cv2.imwrite('savedImage.jpg', img)


image_path = './img.jpg'
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Unable to load image at {image_path}")
else:
    filename = 'savedImage.jpg'
    cv2.imwrite(filename, img)
    img_saved = cv2.imread(filename)
    # cv2.imshow("Saved Image", img_saved)
    # Resize image to fit certain dimensions
    resized_img = cv2.resize(img_saved, (400, 600))
    cv2.imshow("Saved Image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()