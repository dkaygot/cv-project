import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success: break

    # Convert to RGB for Mediapipe
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        # Get landmarks for shoulders (11, 12)
        lm = results.pose_landmarks.landmark
        
        # Simple logic: If shoulder height difference is too high or y-axis is too low
        shoulder_y = (lm[11].y + lm[12].y) / 2
        
        status = "Good Posture"
        color = (0, 255, 0)
        
        if shoulder_y > 0.5: # Adjust threshold based on your seating
            status = "Slouching Detected!"
            color = (0, 0, 255)

        cv2.putText(image, status, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow('ErgoMonitor', image)
    if cv2.waitKey(5) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()