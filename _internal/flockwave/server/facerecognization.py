import cv2
import face_recognition

# Load your face image
known_image = face_recognition.load_image_file("me.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Start the webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

    # Detect faces and get encodings
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        match = face_recognition.compare_faces([known_encoding], face_encoding)
        name = "Unknown"

        if match[0]:
            name = "Mahek"
            import csv
from datetime import datetime

with open("attendance.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])


        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Show the result
    cv2.imshow('Face Recognition', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
video_capture.release()
cv2.destroyAllWindows()
