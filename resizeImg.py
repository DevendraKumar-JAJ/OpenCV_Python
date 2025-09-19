import sys
import os
import cv2 


# Check that a command-line argument was provided
if len(sys.argv) < 2:
    print("Error: Please provide an image file path as a command-line argument.")
    sys.exit(1)

# The first command-line argument is the path to the image
img_path_in = sys.argv[1]

# Check if the input file actually exists
if not os.path.exists(img_path_in):
    print(f"Error: The file '{img_path_in}' does not exist.")
    sys.exit(1)

# Read the image in grayscale (0 flag)
img = cv2.imread(img_path_in, 1)

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Failed to load image from '{img_path_in}'. Check file permissions or integrity.")
    sys.exit(1)

# img=cv2.resize(img,(200,600))
# cv2.imshow("Hello Dear",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# with mantaing aspect 
# while True:
#   try:
#     newW = int(input("New Img Width [100px-500px]: ").strip())
#     if newW < 100 and newW > 500:
#         raise ValueError("Width out of allowed range.")
#     break
#   except ValueError as e:
#     print(f"Invalid input: {e}")
#     sys.exit(1)
    
# imgh,imgw=img.shape[:2]
# # newW=40
# img_aspect=imgh/imgw

# newH=int(newW*img_aspect)
# img=cv2.resize(img,(newW,newH))
# cv2.imwrite("resized.jpg",img)
# cv2.imshow("Resized Img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# with users width and height size 
# while True:
#   try:
#     newW = int(input("New Img Width [100px-500px]: ").strip())
#     newH=int(input("New Img height [100px-500px]: ").strip())
#     if  newW >= 100 and newW <= 500:
#       break
#   except ValueError as e:
#     print(f"Invalid input: {e}")
#     sys.exit(1)
    
# img=cv2.resize(img,(newW,newH))
# cv2.imwrite("resized.jpg",img)
# cv2.imshow("Resized Img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

original_size_kb = os.path.getsize(img_path_in) // 1024
min_size = max(1, int(original_size_kb * 0.01))  # 1% of original

print(f"Compression possible: {min_size}KB - {original_size_kb}KB")

while True:
    try:
        target_size_kb = int(input("Target image size (KB): ").strip())
        if target_size_kb < min_size or target_size_kb > original_size_kb:
            raise ValueError(f"Size out of range ({min_size}KB - {original_size_kb}KB).")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

# Estimate JPEG quality
quality = int((target_size_kb / original_size_kb) * 100)
quality = max(1, min(quality, 100))

# Save compressed image
filename = f"compressed_q{quality}.jpg"
cv2.imwrite(filename, img, [cv2.IMWRITE_JPEG_QUALITY, quality])
file_size_kb = os.path.getsize(filename) // 1024

print(f"✅ Compressed to {file_size_kb}KB at quality {quality} → saved as '{filename}'")