import cv2
import os

# Create a directory to store images
SAVE_DIR = "face_data"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

cap = cv2.VideoCapture(0)

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture Your Face - Press 'C' to Save", frame)
    
    # Press 'C' to capture images
    if cv2.waitKey(1) & 0xFF == ord('c'):
        filename = f"{SAVE_DIR}/face_{count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        count += 1

    # Press 'Q' to quit
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
