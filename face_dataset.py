import os
import cv2

camera_capture = cv2.VideoCapture(0)
camera_capture.set(3, 640)
camera_capture.set(4, 480)

face_detector = cv2.CascadeClassifier('Data/Training/haarcascade_frontalface_default.xml')

def dataset(id_user):
    count = 0

    while (True):
        ret, frame = camera_capture.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            cv2.imwrite(f'Data/Images/Users/{str(id_user)}.{str(count)}.jpg', gray[y:y + h, x:x + w])

            cv2.imshow('Save your face', frame)

        k = cv2.waitKey(100) & 0xff
        if k == 27 or count >= 40:
            break

    camera_capture.release()
    cv2.destroyAllWindows()