import sys
from PySide6 import QtCore, QtWidgets, QtGui 
from PySide6.QtUiTools import QUiLoader



#testing buttons
def play_clicked():
        print("Play button clicked!")
def stop_clicked():
        print("Stop button clicked!")
def record_clicked():
        print("Record button clicked!")


#set up a loader object
loader = QUiLoader()


#object to wrap UI
class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        app = QtWidgets.QApplication.instance()  # get the current QApplication instance
        app.setStyle('Fusion')  # set the style to Fusion
        self.ui = loader.load("main_window.ui", None)
        self.ui.play_audio_button.clicked.connect(play_clicked)
        self.ui.stop_audio_button.clicked.connect(stop_clicked)
        self.ui.record_audio_button.clicked.connect(record_clicked)
         # Set the window icon
        self.ui.setWindowIcon(QtGui.QIcon('icon.png'))
    def show(self):
        self.ui.show()
 