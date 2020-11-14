import cv2


def recognition():
    global fname
    camera_capture = cv2.VideoCapture(0)
    camera_capture.set(3, 640)
    camera_capture.set(4, 480)

    minW = 0.1 * camera_capture.get(3)
    minH = 0.1 * camera_capture.get(4)

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_detector = cv2.CascadeClassifier('Data/Training/haarcascade_frontalface_default.xml')

    confirm = False
    font = cv2.FONT_HERSHEY_SIMPLEX
    id = 0

    try:
        face_recognizer.read('Data/Training/trainer.yml')
    except:
        camera_capture.release()
        cv2.destroyAllWindows()


    while True:
        ret, frame = camera_capture.read()
        frame = cv2.flip(frame, 1)
        count = 0

        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        except:
            from GUI.Main_Window import error_db
            error_db('Пользователи еще не созданы')
            camera_capture.release()
            cv2.destroyAllWindows()
            break

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            count += 1

            id, confidence = face_recognizer.predict(gray[y:y + h, x:x + w])

            if (confidence <= 40):
                from db import info_about_user
                fname, lname, email = info_about_user(id)
                confirm = True
            else:
                fname = 'unknown'

            confidence = (f'{round(100 - confidence)}%')

            cv2.putText(frame, str(fname), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(frame, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        if count <= 1:
            cv2.imshow('FaceID', frame)

            k = cv2.waitKey(10) & 0xff  # 'ESC' for exiting

            if k == 27:
                camera_capture.release()
                cv2.destroyAllWindows()
                return None

            elif confirm == True:
                camera_capture.release()
                cv2.destroyAllWindows()
                return id
        else:
            from GUI.Main_Window import error_db
            error_db('Зафиксировано больше одного лица')
            camera_capture.release()
            cv2.destroyAllWindows()
            break