import cv2
import sys
import os

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
img = cv2.imread(img_path_in, 0)

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Failed to load image from '{img_path_in}'. Check file permissions or integrity.")
    sys.exit(1)

# Get the filename from the input path using os.path.basename
filename = os.path.basename(img_path_in)

# Define the output directory
dir_path_out = "A:\\GRAY\\"
# Create the output directory if it does not exist (exist_ok=True prevents errors)
os.makedirs(dir_path_out, exist_ok=True)

# Construct the full output file path using os.path.join
filepath_out = os.path.join(dir_path_out, filename)

# Save the grayscale image
if cv2.imwrite(filepath_out, img):
    print(f'Image saved successfully: {filepath_out}')
    
    # Display the grayscale image (we are using the already loaded `img` object)
    img=cv2.imread(filepath_out,1)
    cv2.imshow("Grayscale Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Error: Failed to save the image.')
