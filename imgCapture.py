import cv2 as cv
import sys

def main():
    # Open video file or capture device
    cap=cv.VideoCapture(0)
    
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
            cv.imshow('Camera', frame)
            # Access pixel at (100, 100)
            # pixel_bgr = frame[100, 100]
            # print(f"Pixel BGR: {pixel_bgr}")    
            if cv.waitKey(1) & 0xFF == ord('s'):  # Save on 's' press
              cv.imwrite('captured_image.bmp', frame)
              print("Image saved as 'captured_image.jpg'")
              break   
            
            elif cv.waitKey(1) & 0xFF == ord('q'):  # Quit on 'q'
              break 
      cap.release()
      cv.destroyAllWindows()  
    
if __name__ == "__main__":
    main()  