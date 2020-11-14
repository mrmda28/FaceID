from GUI.Main_Widget import MainWidget
from GUI.Main_Window import *
from db import sign_in_db, info_about_user
from face_recognition import recognition


class SignInWidget(QWidget):
    def __init__(self, window):
        super(SignInWidget, self).__init__(window)
        self.window = window

        self.layout = QHBoxLayout()
        self.layout_left = QVBoxLayout()
        self.layout_right = QVBoxLayout()
        self.buttons_layout = QVBoxLayout()

        self.input_email = QLineEdit()
        self.input_password = QLineEdit()

        self.button_forget = QPushButton()
        self.button_sign_in = QPushButton()
        self.button_sign_up = QPushButton()
        self.button_face_id = QPushButton()

        self.message = QMessageBox()

        self.label_left = QLabel()
        self.label_right = QLabel()
        self.label_right_description = QLabel()

        self.init_ui()

    def init_ui(self):
        # -------- Left --------#
        self.layout_left.addStretch(1)

        self.label_left.setText('Войти в запись')
        self.label_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_left.setStyleSheet('''
            font-size: 35px;
            background: transparent;
        ''')
        self.layout_left.addWidget(self.label_left)

        self.input_email.setPlaceholderText('Email')
        self.input_email.setStyleSheet('''
            background: #eee;
            border: none;
            border-radius: 10px;
            padding: 12px 15px;
            margin: 8px 50px;
        ''')
        self.layout_left.addWidget(self.input_email)

        self.input_password.setPlaceholderText('Password')
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setStyleSheet('''
            background: #eee;
            border: none;
            border-radius: 10px;
            padding: 12px 15px;
            margin: 8px 50px;
        ''')
        self.layout_left.addWidget(self.input_password)

        # self.button_forget.setText('Забыли пароль?')
        # self.button_forget.setStyleSheet('''
        #     border: none;
        #     font-size: 15px;
        #     background: transparent;
        # ''')
        # self.buttons_layout.addWidget(self.button_forget)

        self.button_sign_in.setText('Вход')
        self.button_sign_in.setStyleSheet('''
            max-width: 100%;
            border-radius: 20px;
            border: 1px solid red;
            background: red;
            color: #FFFFFF;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 45px;
            margin-left: 110px;
            margin-right: 110px;
            margin-top: 10px;
        ''')
        self.button_sign_in.clicked.connect(self.sign_in)
        self.buttons_layout.addWidget(self.button_sign_in)

        self.button_face_id.setText('Face ID')
        self.button_face_id.setStyleSheet('''
            max-width: 100%;
            border-radius: 20px;
            border: 1px solid blue;
            background: blue;
            color: #FFFFFF;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 45px;
            margin-left: 110px;
            margin-right: 110px;
            margin-top: 10px;
        ''')
        self.button_face_id.clicked.connect(self.face_id_widget)
        self.buttons_layout.addWidget(self.button_face_id)
        self.layout_left.addLayout(self.buttons_layout)

        self.layout_left.addStretch(1)

        self.layout.addLayout(self.layout_left, stretch=1)

        # -------- Right --------#
        self.layout_right.addStretch(1)

        self.label_right.setText('Введите\nemail и пароль')
        self.label_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_right.setStyleSheet('''
            font-size: 35px;
            background: transparent;
            color: white;
        ''')
        self.layout_right.addWidget(self.label_right)


        self.label_right_description.setText('\nЕще не зарегистированны?')
        self.label_right_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_right_description.setStyleSheet('''
            font-size: 16px;
            background: transparent;
            color: white;
        ''')
        self.layout_right.addWidget(self.label_right_description)

        self.button_sign_up.setText('Регистрация')
        self.button_sign_up.setStyleSheet('''
            max-width: 100%;
            border-radius: 20px;
            border: 1px solid white;
            background: transparent;
            color: white;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 35px;
            margin-left: 100px;
            margin-right: 100px;
            margin-top: 10px;
        ''')
        self.button_sign_up.clicked.connect(self.sign_up_widget)
        self.layout_right.addWidget(self.button_sign_up)

        self.layout_right.addStretch(1)

        self.layout.addLayout(self.layout_right, stretch=1)
#------
        self.setLayout(self.layout)

    def face_id_widget(self):
        id_user = recognition()
        if (id_user) is not None:
            self.window.update_widget(MainWidget(self.window, id_user))
            self.window.background(3)
        else:
            pass

    def sign_up_widget(self):
        from GUI.Sign_Up import SignUpWidget
        self.window.update_widget(SignUpWidget(self.window))
        self.window.background(2)

    def sign_in_widget(self):
        self.window.update_widget(SignInWidget(self.window))
        self.window.background(1)

    def sign_in(self):
        email = self.input_email.text()
        password = self.input_password.text()

        if (email and password) == '':
            self.message.setText('Введите все данные')
            self.message.setStyleSheet('background: white;')
            self.message.exec_()
        else:
            try:
                password_db, id_user = sign_in_db(email)

                if password == password_db:
                    self.window.update_widget(MainWidget(self.window, id_user))
                    self.window.background(3)
                else:
                    self.message.setText('Неверные данные')
                    self.message.setStyleSheet('background: white;')
                    self.message.exec_()
            except:
                from GUI.Main_Window import error_db
                error_db('Ошибка при проверке пароля')