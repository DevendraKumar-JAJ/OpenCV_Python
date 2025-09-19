import cv2

# Initialize camera (0 for default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open camera.")
else:
    print("Press 's' to save a photo, 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame.")
            break
          
        if ret:
          print(f"Frame shape: {frame.shape}")  # e.g., (480, 640, 3)
    # Access pixel at (100, 100)
          pixel_bgr = frame[100, 100]
          print(f"Pixel BGR: {pixel_bgr}")
        
        cv2.imshow('Camera', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Save on 's' press
            cv2.imwrite('captured_image.bmp', frame)
            print("Image saved as 'captured_image.jpg'")
            break
        elif key == ord('q'):  # Quit on 'q'
            break
    
    cap.release()
    cv2.destroyAllWindows()