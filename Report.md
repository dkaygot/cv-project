Problem Statement: Remote work/study has increased sedentary behavior. Poor posture is a common "silent" health issue.

Why it Matters: Early intervention via visual cues can prevent long-term musculoskeletal issues.

Approach: * Tech Stack: Python, OpenCV (Video I/O), Mediapipe (Pose Estimation).

Methodology: Used a pre-trained CNN-based pose estimator to extract 3D landmarks. Focused on the Y-coordinates of landmarks 11 and 12 (shoulders) to determine torso collapse.

Key Decisions: Chose Mediapipe over OpenPose for its low CPU latency, allowing it to run alongside other applications without slowing down the PC.

Challenges: Lighting variations affecting landmark confidence. I mitigated this by using normalized coordinates provided by the model.

Learning: I learned how to map abstract coordinate data to human-readable "states" (Good vs. Bad posture).