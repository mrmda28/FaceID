import os
import numpy as np
from PIL import Image
import cv2

camera_capture = cv2.VideoCapture(0)
camera_capture.set(3, 640)
camera_capture.set(4, 480)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_detector = cv2.CascadeClassifier('Data/Training/haarcascade_frontalface_default.xml')

path = 'Data/Images/Users'

def training():
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        faceSamples=[]
        ids = []

        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img,'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[0])

            faces = face_detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples, ids

    # print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces,ids = getImagesAndLabels(path)
    face_recognizer.train(faces, np.array(ids))

    # Save the model into trainer/trainer.yml
    face_recognizer.save('Data/Training/trainer.yml')

    # Print the numer of faces trained and end program
    # print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    return True