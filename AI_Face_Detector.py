import cv2

# 1. Haar Cascade model load karna (Make sure .xml file same folder mein ho)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 2. Webcam open karna
cap =  cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # 3. Frame ko Grayscale mein convert karna
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 4. Faces detect karna 
    # (scaleFactor aur minNeighbors detection ko fine-tune karte hain)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
    
    # 5. Detect hue faces par green rectangle banana
    for (x, y, w, h) in faces:
        # frame par rectangle banao (color aur thickness ke sath)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    # 6. Total faces count ko screen par text ki tarah dikhana
    cv2.putText(frame, f"Faces: {len(faces)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # 7. Frame ko screen par show karna
    cv2.imshow('Face Detector', frame)
    
    # 8. 'q' dabane par loop break karna
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()