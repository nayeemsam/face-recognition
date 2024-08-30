Face Recognition with OpenCV and face_recognition
This is a simple face recognition project using Python, OpenCV, and the face_recognition library.

Features
Detects and recognizes faces from a webcam feed in real-time.
Matches detected faces with known faces from images.
Requirements
Python 3.x
OpenCV
face_recognition
Install the required libraries using pip:

bash
Copy code
pip install opencv-python face_recognition
Usage
Add Known Faces:

Place images of known individuals in the project directory.
Update the image paths in the script.
Run the Script:

bash
Copy code
python face_recognition.py
The script will start the webcam and display a video feed with recognized faces labeled.
Stop the Script:

Press q to stop the video feed and exit the script.
How It Works
The script loads images of known faces and encodes them.
It captures video from the webcam, detects faces in each frame, and tries to recognize them based on the known faces.
License
This project is licensed under the MIT License.
