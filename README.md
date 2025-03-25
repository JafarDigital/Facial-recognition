# Simple Face Recognition with OpenCV and Python

A lightweight real-time face recognition system using your computer webcam and the `face_recognition` library. It detects and labels faces in live video with OpenCV.

## Features

- Real-time face detection and recognition
- Uses web-cam or IP camera (e.g., security camera or smartphone with IP Webcam app)
- Simple training using your own images

## Getting Started

### 1. Install dependencies

pip install opencv-python face_recognition

### Collect Face Data
Run the script to capture face images:

python face-data.py

Press C to capture, Q to quit.

### Train the Model

python training.py

This creates face_encodings.pkl with your face encodings.

### Run Face Recognition

python main.py

The webcam feed will open and recognized faces will be labeled.

### Optional: IP Webcam or security camera
You can change the webcam input in main.py or face-data.py:

cap = cv2.VideoCapture("http://<ip>:8080/video")
