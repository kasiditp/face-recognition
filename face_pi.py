# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
# import face_recognition
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# obama_image = face_recognition.load_image_file("yamakawa.jpg")
# obama_face_encoding = face_recognition.face_encodings(obama_image, num_jitters=5)[0]

# jub_image = face_recognition.load_image_file("Kasidit2.jpg", mode='RGB')
# jub_face_encoding = face_recognition.face_encodings(jub_image, num_jitters=5)[0]

# gua_image = face_recognition.load_image_file("Pakpon2.png", mode='RGB')
# gua_face_encoding = face_recognition.face_encodings(gua_image, num_jitters=1)[0]

# allow the camera to warmup
time.sleep(0.1)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    # small_frame = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
    # if process_this_frame:
    #     # Find all the faces and face encodings in the current frame of video
    #     face_locations = face_recognition.face_locations(small_frame)
    #     face_encodings = face_recognition.face_encodings(
    #         small_frame, face_locations, num_jitters=1)

    #     face_names = []
    #     for face_encoding in face_encodings:
    #         # See if the face is a match for the known face(s)
    #         match = face_recognition.compare_faces([obama_face_encoding, gua_face_encoding, jub_face_encoding ],
    #                                                face_encoding,tolerance=0.6)
    #         name = "Unknown"
    #         print match
    #         if match[0] == True:
    #             name = "Yamakawa"
    #         elif match[1]:
    #             name = "Gua"
    #         elif match[2]:
    #             name = "Kasidit"

    #         face_names.append(name)

    # process_this_frame = not process_this_frame

    # # Display the results
    # for (top, right, bottom, left), name in zip(face_locations, face_names):
    #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    #     top *= 4
    #     right *= 4
    #     bottom *= 4
    #     left *= 4

    #     # Draw a box around the face
    #     cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

    #     # Draw a label with a name below the face
    #     cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255),
    #                   1)
    #     font = cv2.FONT_HERSHEY_DUPLEX
    #     cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    # cv2.imshow('Video', frame)
	
 
	# show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
		break
