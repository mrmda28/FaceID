from GUI.Main_Window import *
from face_training import training


class LoadingWidget(QWidget):
    def __init__(self, window, id_user):
        super(LoadingWidget, self).__init__(window)
        self.window = window
        self.window.background(0)

        self.id_user = id_user

        self.timer = QTimer()
        self.label_animation = QLabel()
        self.movie = QMovie('Data/Images/loading_icon.gif')

        self.layout = QVBoxLayout()
        self.label = QLabel()

        self.init_ui()

    def init_ui(self):
        # -------- Left --------#
        self.layout.addStretch(1)

        self.label.setText('Подождите, идет обработка данных')
        self.label.setStyleSheet('font-size: 18px;')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.layout.addStretch(1)

        # loading gif
        self.label_animation.setMovie(self.movie)
        self.label_animation.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label_animation)

        self.start_animation()
        self.timer.singleShot(4000, self.stop_animation)

        self.layout.addStretch(1)
        self.setLayout(self.layout)

    def finish(self):
        self.label.setText('Успешно!')
        self.label.setStyleSheet('font-size: 22px; font-weight: bold; color: green;')
        self.timer.singleShot(1500, self.exit)

    def exit(self):
        from GUI.Main_Widget import MainWidget
        self.movie.start()
        self.window.update_widget(MainWidget(self.window, self.id_user))
        self.window.background(3)

    def training(self):
        training()
        self.finish()

    def start_animation(self):
        self.movie.start()

    def stop_animation(self):
        self.movie.stop()
        self.training()