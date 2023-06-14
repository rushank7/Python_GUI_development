# import sys
# from PySide6.QtWidgets import QApplication, QWidget,QPushButton , QMainWindow

# ## Subclass qmainwindow to customize your applications main window

# class ButtonHolder(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle(" button holder app")
#         button = QPushButton("Press me")
#         # set our button as central widget
#         self.setCentralWidget(button)

# app = QApplication(sys.argv)
# window = ButtonHolder()
# window.show()
# app.exec()

import sys
from PySide6.QtWidgets import QApplication, QWidget,QPushButton , QMainWindow
from button_holder import ButtonHolder

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()