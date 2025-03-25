import face_recognition
import numpy as np
import pickle
import os

SAVE_DIR = "face_data"
ENCODED_FILE = "face_encodings.pkl"

encodings = []
names = []

# Load each image and encode it
for filename in os.listdir(SAVE_DIR):
    image_path = os.path.join(SAVE_DIR, filename)
    image = face_recognition.load_image_file(image_path)
    face_enc = face_recognition.face_encodings(image)

    if face_enc:
        encodings.append(face_enc[0])
        names.append("User")

# Save encodings
with open(ENCODED_FILE, "wb") as f:
    pickle.dump((encodings, names), f)

print("Face data trained and saved.")
