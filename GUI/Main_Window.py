from PyQt5 import QtCore
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QMainWindow, QWidget, \
    QDesktopWidget, QMessageBox, QPushButton, QLineEdit
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from GUI.Sign_In import SignInWidget


class MainWindow(QMainWindow):
    WINDOW_W = 768
    WINDOW_H = 480

    WINDOW_TITLE = 'FaceID'

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(self.WINDOW_TITLE)
        self.setStyleSheet('background: url(Data/Images/bg_sign_in.png);')
        self.center_on_screen()
        self.update_widget(SignInWidget(self))
        self.show()

    def background(self, n):
        if n == 0:
            self.setStyleSheet('background: white;')
        elif n == 1:
            self.setStyleSheet('background: url(Data/Images/bg_sign_in.png);')
        elif n == 2:
            self.setStyleSheet('background: url(Data/Images/bg_sign_up.png);')
        elif n == 3:
            self.setStyleSheet('background: url(Data/Images/bg_main.png);')


    def update_widget(self, widget: QWidget, size_w: int = WINDOW_W, size_h: int = WINDOW_H):
        self.setFixedSize(size_w, size_h)
        self.setCentralWidget(widget)

    def center_on_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def error_db(text):
    msg = QMessageBox()
    msg.setText(str(text))
    msg.setStyleSheet('background: white;')
    msg.exec_()