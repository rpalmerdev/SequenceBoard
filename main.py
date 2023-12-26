import sys
import logging
from PySide6 import QtWidgets
from user_interface import UserInterface

logging.basicConfig(level=logging.INFO)

app = QtWidgets.QApplication(sys.argv)
window = UserInterface()
window.show()

app.exec()