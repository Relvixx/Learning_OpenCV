"""import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Path to the model
model_path = 'hand_landmarker.task'

# Create options
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=2)

# Create landmarker
with vision.HandLandmarker.create_from_options(options) as landmarker:
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create MediaPipe image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # Detect hands
        result = landmarker.detect(mp_image)

        # Draw landmarks
        if result.hand_landmarks:
            for hand_landmarks in result.hand_landmarks:
                for landmark in hand_landmarks:
                    x = int(landmark.x * frame.shape[1])
                    y = int(landmark.y * frame.shape[0])
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        cv2.imshow("MediaPipe Hand Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
"""

import cv2
import mediapipe as mp

# 1. MediaPipe Hands ka setup
mp_hands = mp.solutions.hands
# Confidence 0.5 matlab agar AI 50% sure hai ki yeh haath hai, tabhi draw karega
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) 
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 2. BGR frame ko RGB mein convert karna
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 3. Frame ko MediaPipe se process karwana
    results = hands.process(rgb_frame)

    # 4. Agar frame mein koi haath detect hota hai
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 1. Landmarks draw karna
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 2. Points ko ek list mein nikalna (pixel coordinates ke bajaye normalized use karenge)
            # MediaPipe points 0 se 1 ke beech hote hain (x, y)
            lm = hand_landmarks.landmark 
            
            fingers = []

            # --- FINGER LOGIC ---

            # A. Thumb (Angutha)
            # Right hand ke liye: Agar tip (4) knuckle (2) ke left mein hai toh 'Open'
            if lm[4].x < lm[2].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # B. Baaki 4 Ungliyan
            tip_ids = [8, 12, 16, 20]
            knuckle_ids = [6, 10, 14, 18]

            for i in range(4):
                # Agar tip (8,12,16,20) ki Y-value knuckle (6,10,14,18) se kam hai
                # (Y kam matlab screen par upar)
                if lm[tip_ids[i]].y < lm[knuckle_ids[i]].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # --- DISPLAY ---
            total_fingers = fingers.count(1)
            
            # Ek bada box aur number display karna
            cv2.rectangle(frame, (20, 20), (150, 120), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, str(total_fingers), (45, 100), 
                        cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)

    cv2.imshow("Finger Counter", frame)
    cv2.imshow("MediaPipe Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows