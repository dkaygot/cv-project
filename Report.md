Project Report: AI-Powered Ergonomics Monitor
1. Problem Identification
The modern digital lifestyle has led to an increase in postural issues such as "Tech Neck" and rounded shoulders. This project aims to use Computer Vision to provide a real-time monitoring solution that alerts users when their posture deviates from a healthy baseline.

2. Approach & Technical Implementation
I utilized Mediapipe's Pose Estimation model to track 33 body landmarks. The core logic focuses on the Y-coordinates of the shoulder landmarks (11 and 12).

Algorithm: The system calculates the average vertical position of the shoulders. If the coordinates exceed a specific threshold (indicating the shoulders have dropped/slouched), a trigger is sent to the UI.

Tools: Python for logic, OpenCV for video stream manipulation, and Mediapipe for the CNN-based landmark detection.

3. Key Decisions
Pre-trained vs. Custom: I chose a pre-trained Mediapipe model over training a custom YOLO model to ensure real-time performance on standard CPU hardware without needing a dedicated GPU.

Visual Feedback: I decided on a simple color-coded text overlay (Green/Red) to provide non-intrusive feedback to the user.

4. Challenges Faced
Environment Setup: Initially encountered a ModuleNotFoundError for cv2. This was resolved by reconfiguring the Python interpreter and manually installing dependencies via pip.

Threshold Calibration: Setting a universal "slouch" threshold is difficult due to varying camera angles. A future improvement would be a "Calibrate" button to set a personalized baseline.

5. Learning & Reflection
This project deepened my understanding of how coordinate geometry from pose estimation can be translated into actionable real-world insights. I learned the importance of choosing the right tool (Mediapipe) for the specific hardware constraints of the end-user.
