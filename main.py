from PySide6.QtWidgets import QApplication, QWidget,QPushButton , QMainWindow

import sys

app = QApplication(sys.argv)

window = QWidget()

window = QMainWindow()
window.setWindowTitle("my First Mainwindow app")

button = QPushButton()
button.setText("Press me")

window.setCentralWidget(button)
window.show()

app.exec()