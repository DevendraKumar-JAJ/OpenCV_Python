import cv2 as cv
import sys

def main():
    # Open video file or capture device
    cap=cv.VideoCapture(0)
    
    fwidth=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    fheight=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    print(f"Frame width: {fwidth}, Frame height: {fheight}")
    fps=cap.get(cv.CAP_PROP_FPS)  
    # 
    codec=cv.VideoWriter_fourcc(*'mp4v')
    rec=cv.VideoWriter('output.mp4',codec,fps,(fwidth,fheight))
    while True:
      suc,img=cap.read()
      
      if not suc:
        print("Error: Can't receive frame.")
        break 
      
      cv.putText(img, "Hello Video", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv.LINE_AA)
      rec.write(img)
      cv.imshow('Video',img)
      if cv.waitKey(1) & 0xFF==ord('q'):
        break

    cap.release()
    rec.release()
    cv.destroyAllWindows()
if __name__ == "__main__":
    main()  