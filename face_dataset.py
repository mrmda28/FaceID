from db import photo_to_db
import os
import cv2


face_detector = cv2.CascadeClassifier('Data/Training/haarcascade_frontalface_default.xml')

img_path = 'Data/Images/user.jpg'


def img_save_img():
    with open(rf'{img_path}', 'rb') as file:
        return file.read()

def dataset(id_user):
    camera_capture = cv2.VideoCapture(0)
    camera_capture.set(3, 640)
    camera_capture.set(4, 480)

    img_count = 0

    while (True):
        ret, frame = camera_capture.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            img_count += 1

            cv2.imwrite(img_path, gray[y:y + h, x:x + w])

            img_save_img()

            photo_to_db(id_user, img_save_img())

            path_img = os.path.join(os.path.abspath(os.path.dirname(__file__)), img_path)
            os.remove(path_img)

            cv2.imshow('Save your face', frame)

        k = cv2.waitKey(100) & 0xff

        if k == 27 or img_count >= 40:
            camera_capture.release()
            cv2.destroyAllWindows()
            break