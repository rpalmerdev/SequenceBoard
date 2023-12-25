from PySide6 import QtCore, QtWidgets, QtGui 
from PySide6.QtUiTools import QUiLoader
from recorder import Recorder
from player import AudioPlayer



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

        # Create a new Recorder and Player
        self.recorder = Recorder()
        self.player = AudioPlayer('output')

        # Connect the record buttons to the start_recording and stop_recording methods
       
        # channel 1
        self.ui.record_button_1.pressed.connect(lambda: self.start_recording_channel(1))
        self.ui.record_button_1.released.connect(self.recorder.stop_recording)
        # channel 2
        self.ui.record_button_2.pressed.connect(lambda: self.start_recording_channel(2))
        self.ui.record_button_2.released.connect(self.recorder.stop_recording)
        # channel 3
        self.ui.record_button_3.pressed.connect(lambda: self.start_recording_channel(3))
        self.ui.record_button_3.released.connect(self.recorder.stop_recording)
        # channel 4
        self.ui.record_button_4.pressed.connect(lambda: self.start_recording_channel(4))
        self.ui.record_button_4.released.connect(self.recorder.stop_recording)
        # channel 5
        self.ui.record_button_5.pressed.connect(lambda: self.start_recording_channel(5))
        self.ui.record_button_5.released.connect(self.recorder.stop_recording)
        # channel 6
        self.ui.record_button_6.pressed.connect(lambda: self.start_recording_channel(6))
        self.ui.record_button_6.released.connect(self.recorder.stop_recording)
        
        #Connect the play buttons to the play_channel and stop_channel methods
        
        # channel 1
        self.ui.play_button_1.pressed.connect(lambda: self.player.play_channel(1))
        self.ui.play_button_1.released.connect(lambda: self.player.stop_channel(1))
        # channel 2
        self.ui.play_button_2.pressed.connect(lambda: self.player.play_channel(2))
        self.ui.play_button_2.released.connect(lambda: self.player.stop_channel(2))
        # channel 3
        self.ui.play_button_3.pressed.connect(lambda: self.player.play_channel(3))
        self.ui.play_button_3.released.connect(lambda: self.player.stop_channel(3))
        # channel 4
        self.ui.play_button_4.pressed.connect(lambda: self.player.play_channel(4))
        self.ui.play_button_4.released.connect(lambda: self.player.stop_channel(4))
        # channel 5
        self.ui.play_button_5.pressed.connect(lambda: self.player.play_channel(5))
        self.ui.play_button_5.released.connect(lambda: self.player.stop_channel(5))
        # channel 6
        self.ui.play_button_6.pressed.connect(lambda: self.player.play_channel(6))
        self.ui.play_button_6.released.connect(lambda: self.player.stop_channel(6))

    def start_recording_channel(self, channel):
        # Start recording on the specified channel
        self.recorder.set_output_channel(channel) 
        self.recorder.start_recording()

    def show(self):
        self.ui.show()