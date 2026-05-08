import cv2
import mediapipe as mp

# MediaPipe Pose setup
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    # BGR to RGB conversion
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    # Pose landmarks draw karna
    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                               mp_draw.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                               mp_draw.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))

    cv2.imshow('Pose Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()