import sys
from PyQt5.QtWidgets import QApplication
from GUI.Main_Window import MainWindow


if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyle("Fusion")
	main_window = MainWindow()
	sys.exit(app.exec_())