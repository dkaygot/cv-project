AI-Powered Ergonomics & Posture Monitor
🚀 Overview
This project is a real-time computer vision application designed to combat "Tech Neck" and poor seating habits. Using pose estimation, the application monitors the user's posture through a webcam and provides instant visual feedback when slouching or poor alignment is detected.

💡 The Problem
In an era of remote work and digital learning, many people spend hours in front of screens, leading to chronic back and neck pain. This project serves as a lightweight, accessible tool to help users maintain a healthy posture without requiring expensive hardware.

🛠️ Tech Stack
Language: Python 3.x

Libraries: * OpenCV: For real-time video processing and UI overlay.

Mediapipe: High-fidelity body landmark tracking (Pose estimation).

⚙️ Installation & Setup
To run this project locally, follow these steps:

Clone the repository:

Install Dependencies:

Run the Application:

🖥️ How it Works
Frame Capture: The system accesses the webcam using OpenCV.

Pose Estimation: Mediapipe’s Pose model identifies 33 3D landmarks on the body.

Ergonomic Logic: The script specifically monitors the Y-coordinates of the Shoulders (Landmarks 11 and 12).

Alert System: If the average shoulder height drops below a calibrated threshold (indicating a slouch), the screen text switches from a green "Good Posture" to a red "Slouching Detected!".

📊 Features
Real-time Analysis: High FPS processing with minimal latency.

Non-Invasive: Works with standard webcams—no extra sensors needed.

Visual Feedback: Dynamic on-screen HUD (Heads-Up Display) for immediate correction.

📝 Course Information
Course: Computer Vision

Assignment: Bring Your Own Project (BYOP) Capstone

Institution: VITyarthi Platform
