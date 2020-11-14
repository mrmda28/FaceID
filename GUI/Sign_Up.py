from GUI.Loading import LoadingWidget
from GUI.Main_Widget import MainWidget
from face_dataset import dataset
from db import sign_up_db, get_id_user
from GUI.Main_Window import *


class SignUpWidget(QWidget):
    def __init__(self, window):
        super(SignUpWidget, self).__init__(window)
        self.window = window

        self.layout = QHBoxLayout()
        self.layout_left = QVBoxLayout()
        self.layout_right = QVBoxLayout()

        self.input_firstname = QLineEdit()
        self.input_lastname = QLineEdit()
        self.input_email = QLineEdit()
        self.input_password = QLineEdit()

        self.message = QMessageBox()

        self.label_left = QLabel()
        self.label_right = QLabel()
        self.label_right_description = QLabel()

        self.init_ui()

    def init_ui(self):
        # -------- Left --------#
        self.layout_right.addStretch(1)

        self.label_right.setText('Введите данные,\nдалее будет FaceID')
        self.label_right.setAlignment(QtCore.Qt.AlignCenter)
        self.label_right.setStyleSheet('''
            font-size: 35px;
            background: transparent;
            color: white;
        ''')
        self.layout_right.addWidget(self.label_right)

        self.label_right_description.setText('\nУже зарегистированны?')
        self.label_right_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_right_description.setStyleSheet('''
            font-size: 16px;
            background: transparent;
            color: white;
        ''')
        self.layout_right.addWidget(self.label_right_description)

        self.button_sign_in = QPushButton('Войти')
        self.button_sign_in.setStyleSheet('''
            max-width: 100%;
            border-radius: 20px;
            border: 1px solid white;
            background: transparent;
            color: white;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 45px;
            margin-left: 100px;
            margin-right: 100px;
            margin-top: 10px;
        ''')
        self.button_sign_in.clicked.connect(self.sign_in_widget)
        self.layout_right.addWidget(self.button_sign_in)

        self.layout_right.addStretch(1)

        self.layout.addLayout(self.layout_right, stretch=1)

        # -------- Right --------#
        self.layout_left.addStretch(1)

        self.label_left.setText('Регистрация')
        self.label_left.setAlignment(QtCore.Qt.AlignCenter)
        self.label_left.setStyleSheet('''
            font-size: 35px;
            background: transparent;
        ''')
        self.layout_left.addWidget(self.label_left)

        self.input_firstname.setPlaceholderText('Имя')
        self.input_firstname.setStyleSheet('''
            background: #eee;
            border: none;
            border-radius: 10px;
            padding: 12px 15px;
            margin: 8px 50px;
        ''')
        self.layout_left.addWidget(self.input_firstname)

        self.input_lastname.setPlaceholderText('Фамилия')
        self.input_lastname.setStyleSheet('''
            background: #eee;
            border: none;
            border-radius: 10px;
            padding: 12px 15px;
            margin: 8px 50px;
        ''')
        self.layout_left.addWidget(self.input_lastname)

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

        self.button_sign_up = QPushButton('Далее')
        self.button_sign_up.setStyleSheet('''
            max-width: 100%;
            border-radius: 20px;
            border: 1px solid blue;
            background: blue;
            color: #FFFFFF;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 25px;
            margin-left: 120px;
            margin-right: 120px;
            margin-top: 10px;
        ''')
        self.button_sign_up.clicked.connect(self.sign_up_camera)
        self.layout_left.addWidget(self.button_sign_up)

        self.layout_left.addStretch(1)

        self.layout.addLayout(self.layout_left, stretch=1)
        # ------
        self.setLayout(self.layout)

    def sign_up_camera(self):
        first_name = self.input_firstname.text()
        last_name = self.input_lastname.text()
        email = self.input_email.text()
        password = self.input_password.text()

        if (first_name and last_name and email and password) == '':
            self.message.setText('Введите все данные')
            self.message.setStyleSheet('background-color: white;')
            self.message.exec_()
        else:
            try:
                sign_up_db(first_name, last_name, email, password)
                self.id = get_id_user(first_name)

                dataset(self.id)

                self.window.update_widget(LoadingWidget(self.window, self.id))
                self.window.background(0)
            except:
                error_db('Ошибка при создании датасета')

    def sign_up_widget(self):
        self.window.update_widget(SignUpWidget(self.window))
        self.window.background(2)

    def sign_in_widget(self):
        from GUI.Sign_In import SignInWidget
        self.window.update_widget(SignInWidget(self.window))
        self.window.background(1)