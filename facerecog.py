import cv2
import face_recognition

#load known face encoding and unknown face encodingff

known_face_encodings=[]
known_face_names=[]

#load known face and thier names

known_person1_image=face_recognition.load_image_file('C:\\Users\\nayee\\OneDrive\\Desktop\\python\\face recognition\\images.jpeg')
known_person2_image=face_recognition.load_image_file('C:\\Users\\nayee\\OneDrive\\Desktop\\python\\face recognition\\WhatsApp Image 2024-06-07 at 23.08.25_8de38025.jpg')
known_person3_image=face_recognition.load_image_file('C:\\Users\\nayee\\OneDrive\\Desktop\\python\\face recognition\\WhatsApp Image 2024-06-07 at 23.20.54_52ff6d45.jpg')
    
known_person1_encoding=face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding=face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding=face_recognition.face_encodings(known_person3_image)[0]
known_face_names.append("messi")
known_face_names.append("naim")
known_face_names.append("nayeem")

#video capture
video_capture=cv2.VideoCapture(0)

while True:
    #cpature frame
    ret,frame=video_capture.read()
    #find face location in current frame
    face_location=face_recognition.face_locations(frame)
    face_encoding=face_recognition.face_encodings(frame,face_location)
    #loop through each face find in a frame
    for (top,right,bottom,left), face_encoding in zip(face_location,face_encoding):
    #check if the current face matches any known face
        matches=face_recognition.compare_faces(known_face_encodings,face_encoding)  
        name="messi"
        if True in matches:
            first_match_index=matches.index(True)
            name=known_face_names[first_match_index]
        #draw a box around the face and label with name
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    cv2.imshow("video",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()