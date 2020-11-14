from db import get_id_from_img, Images
import os
import numpy as np
from PIL import Image
import cv2


face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_detector = cv2.CascadeClassifier('Data/Training/haarcascade_frontalface_default.xml')

img_path = 'Data/Images/user.jpg'

def path_save_img(bimg):
    with open(rf'{img_path}', 'wb') as file:
        file.write(bimg)
    return img_path

def del_img():
    path_img = os.path.join(os.path.abspath(os.path.dirname(__file__)), img_path)
    os.remove(path_img)

def training():
    def images_ids():
        face_samples = []
        ids = []

        for b_image in Images.select(Images.image):
            img = b_image.image
            PIL_img = Image.open(path_save_img(img)).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')

            id = get_id_from_img(img)

            faces = face_detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y + h, x:x + w])
                ids.append(int(str(id)))
        del_img()
        return face_samples, ids

    faces, ids = images_ids()
    face_recognizer.train(faces, np.array(ids)) # training

    face_recognizer.save('Data/Training/trainer.yml') # save the model

    # Print the number of faces trained and end program
    # print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    return True

































