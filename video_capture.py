import cv2
import time

# Webcam open karna
cap = cv2.VideoCapture(0)
prev_time = time.time()  # 0 ki jagah current time se initialize karo

while True:
    # 1. Frame read karna
    ret, frame = cap.read()
    
    if not ret:
        print("Frame receive nahi hua. Exiting...")
        break

    # 4. FPS calculation
    current_time = time.time()
    time_def = current_time - prev_time
    prev_time = current_time
    
    # divide-by-zero avoid karne ke liye check
    if time_def > 0:
        fps = 1 / time_def
    else:
        fps = 0

    # 5. Rendering on camera feed
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
    # 2. Frame ko 'video capture' window mein display karna
    cv2.imshow('video capture', frame)
    
    # 3. Agar 'q' press ho toh loop tod dena
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()