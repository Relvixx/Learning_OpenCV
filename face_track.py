import cv2
import mediapipe as mp

# MediaPipe Face Mesh setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils
# Mesh ki lines draw karne ke liye style
draw_spec = mp_draw.DrawingSpec(thickness=1, circle_radius=1)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    # Face Mesh draw karna
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_draw.draw_landmarks(image=frame, 
                                   landmark_list=face_landmarks,
                                   connections=mp_face_mesh.FACEMESH_TESSELATION,
                                   landmark_drawing_spec=draw_spec,
                                   connection_drawing_spec=draw_spec)

    cv2.imshow('Face Mesh', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()