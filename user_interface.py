from PySide6 import QtCore, QtWidgets, QtGui 
from PySide6.QtUiTools import QUiLoader



#set up a loader object
loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        # get the current QApplication instance
        app = QtWidgets.QApplication.instance()
        # set the style 
        app.setStyle('Fusion') 
        self.ui = loader.load("main_window.ui", None)
        # Set the window icon
        self.ui.setWindowIcon(QtGui.QIcon('assets/icon.png'))
        


    def show(self):
        self.ui.show()