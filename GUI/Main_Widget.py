from GUI.Main_Window import *
from db import info_about_user


class MainWidget(QWidget):
    def __init__(self, window, id_user):
        super(MainWidget, self).__init__(window)
        self.window = window
        self.window.background(3)

        self.id_user = id_user
        self.fname, self.lname, self.email = info_about_user(self.id_user)

        self.top_layout = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.top_label = QLabel()
        self.id_label = QLabel()
        self.email_label = QLabel()

        self.init_ui()

    def init_ui(self):
        # -------- Top --------#
        self.top_label.setText(f'Приветствую, {str(self.fname)} {str(self.lname)}!')
        self.top_label.setStyleSheet('font-size: 28px; color: white; margin-top: 70px')
        self.top_label.setAlignment(QtCore.Qt.AlignCenter)

        self.top_layout.addWidget(self.top_label)
        self.layout.addLayout(self.top_layout)

        # -------- Main --------#
        self.layout.addStretch(2)

        self.email_label.setText(f'id: {str(self.id_user)}')
        self.email_label.setStyleSheet('font-size: 22px; color: gray; background: white;')
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.email_label)

        self.id_label.setText(f'email: {str(self.email)}')
        self.id_label.setStyleSheet('font-size: 22px; color: gray; background: white;')
        self.id_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.id_label)

        self.layout.addStretch(1)

        self.button_exit = QPushButton('Выйти')
        self.button_exit.setStyleSheet('''
            max-width: 100%;
            border-radius: 20px;
            border: 1px solid blue;
            background: blue;
            color: #FFFFFF;
            font-size: 15px;
            font-weight: bold;
            padding: 12px 45px;
            margin-left: 280px;
        ''')
        self.button_exit.clicked.connect(self.exit)
        self.layout.addWidget(self.button_exit)

        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def exit(self):
        from GUI.Sign_In import SignInWidget
        self.window.update_widget(SignInWidget(self.window))
        self.window.background(1)