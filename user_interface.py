from PySide6 import QtCore, QtWidgets, QtGui 
from PySide6.QtUiTools import QUiLoader
from recorder import Recorder
from player import AudioPlayer


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

        # Connect the record buttons 
        self.ui.record_button_1.pressed.connect(lambda: self.start_recording_channel(1))
        self.ui.record_button_1.released.connect(self.recorder.stop_recording)
        
        self.ui.record_button_2.pressed.connect(lambda: self.start_recording_channel(2))
        self.ui.record_button_2.released.connect(self.recorder.stop_recording)
        
        self.ui.record_button_3.pressed.connect(lambda: self.start_recording_channel(3))
        self.ui.record_button_3.released.connect(self.recorder.stop_recording)
        
        self.ui.record_button_4.pressed.connect(lambda: self.start_recording_channel(4))
        self.ui.record_button_4.released.connect(self.recorder.stop_recording)
        
        self.ui.record_button_5.pressed.connect(lambda: self.start_recording_channel(5))
        self.ui.record_button_5.released.connect(self.recorder.stop_recording)
        
        self.ui.record_button_6.pressed.connect(lambda: self.start_recording_channel(6))
        self.ui.record_button_6.released.connect(self.recorder.stop_recording)
        
        #Connect the play buttons 
        self.ui.play_button_1.pressed.connect(lambda: self.player.play_channel(1))
        self.ui.play_button_1.released.connect(lambda: self.player.stop_channel(1))
        
        self.ui.play_button_2.pressed.connect(lambda: self.player.play_channel(2))
        self.ui.play_button_2.released.connect(lambda: self.player.stop_channel(2))
        
        self.ui.play_button_3.pressed.connect(lambda: self.player.play_channel(3))
        self.ui.play_button_3.released.connect(lambda: self.player.stop_channel(3))
        
        self.ui.play_button_4.pressed.connect(lambda: self.player.play_channel(4))
        self.ui.play_button_4.released.connect(lambda: self.player.stop_channel(4))
        
        self.ui.play_button_5.pressed.connect(lambda: self.player.play_channel(5))
        self.ui.play_button_5.released.connect(lambda: self.player.stop_channel(5))
        
        self.ui.play_button_6.pressed.connect(lambda: self.player.play_channel(6))
        self.ui.play_button_6.released.connect(lambda: self.player.stop_channel(6))
        
        # Connect the gain sliders
        self.ui.gain_slider_1.valueChanged.connect(lambda value: self.set_volume(1, value))
        self.ui.gain_slider_2.valueChanged.connect(lambda value: self.set_volume(2, value))
        self.ui.gain_slider_3.valueChanged.connect(lambda value: self.set_volume(3, value))
        self.ui.gain_slider_4.valueChanged.connect(lambda value: self.set_volume(4, value))
        self.ui.gain_slider_5.valueChanged.connect(lambda value: self.set_volume(5, value))
        self.ui.gain_slider_6.valueChanged.connect(lambda value: self.set_volume(6, value))

    def start_recording_channel(self, channel):
        self.recorder.set_output_channel(channel) 
        self.recorder.start_recording()
    
    def set_volume(self, channel, value):
        # Convert the slider value to a volume level between 0.0 and 1.0
        volume = value / 100.0
        self.player.set_volume(channel, volume)
        # Update the corresponding progress bar
        getattr(self.ui, f'gain_meter_{channel}').setValue(value) 
        
    def show(self):
        self.ui.show()
        