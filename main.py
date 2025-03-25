import cv2
import face_recognition
import pickle

# Load known face encodings from the saved file
with open("face_encodings.pkl", "rb") as f:
    known_encodings, known_names = pickle.load(f)

# Change to use the default webcam (0 is default camera)
cap = cv2.VideoCapture(0)  

# Set resolution for the video capture (can be adjusted as needed)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame from BGR to RGB for face recognition
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the detected face encoding to known encodings
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"  # Default name is 'Unknown'

        # If a match is found, assign the known name, ex. "User"
        if True in matches:
            name = "User"

        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        # Display the name above the rectangle
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Display the frame with face recognition
    cv2.imshow("Face Recognition", frame)

    # Exit the loop if 'Q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
