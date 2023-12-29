from PySide6 import QtCore, QtWidgets, QtGui 
from PySide6.QtUiTools import QUiLoader
from recorder import Recorder
from player import AudioPlayer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import logging

class MPLWidget(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        # Set the face color of the figure to match the Fusion theme
        self.fig.patch.set_facecolor('#2d2d2d')

        # Set the face color of the plot to black
        self.axes.set_facecolor('#141414')

        # Remove the title and labels
        self.axes.set_title('')
        self.axes.set_xlabel('')
        self.axes.set_ylabel('')

        # Remove the ticks and tick labels
        self.axes.set_xticks([])
        self.axes.set_yticks([])
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])

        # Remove the box around the plot
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)

        # Adjust subplot spacing
        self.fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0, hspace=0)

        super(MPLWidget, self).__init__(self.fig)
        self.setParent(parent)

        # Set the figure size to match the size of the FigureCanvas
        self.fig.set_size_inches(width, height)

        # Set the size policy of the FigureCanvas
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot_audio_data(self, data):
        self.axes.clear()
        # Plot the waveform in purple
        self.axes.plot(data, color='#b055c8')

        # Remove the ticks and tick labels
        self.axes.set_xticks([])
        self.axes.set_yticks([])
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])

        self.draw()


loader = QUiLoader()
loader.registerCustomWidget(MPLWidget)

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
        self.mpl_widgets = [getattr(self.ui, f'mplwidget_{i}') for i in range(1, 7)]
       
        # Create a new Recorder and Player
        self.recorder = Recorder()
        self.player = AudioPlayer('output')


        # Connect the record buttons 
        self.ui.record_button_1.pressed.connect(lambda: self.start_recording_channel(1))
        self.ui.record_button_1.released.connect(lambda: self.stop_recording_and_plot(1))
        
        self.ui.record_button_2.pressed.connect(lambda: self.start_recording_channel(2))
        self.ui.record_button_2.released.connect(lambda: self.stop_recording_and_plot(2))
        
        self.ui.record_button_3.pressed.connect(lambda: self.start_recording_channel(3))
        self.ui.record_button_3.released.connect(lambda: self.stop_recording_and_plot(3))
        
        self.ui.record_button_4.pressed.connect(lambda: self.start_recording_channel(4))
        self.ui.record_button_4.released.connect(lambda: self.stop_recording_and_plot(4))
        
        self.ui.record_button_5.pressed.connect(lambda: self.start_recording_channel(5))
        self.ui.record_button_5.released.connect(lambda: self.stop_recording_and_plot(5))
        
        self.ui.record_button_6.pressed.connect(lambda: self.start_recording_channel(6))
        self.ui.record_button_6.released.connect(lambda: self.stop_recording_and_plot(6))
        
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
    
    def stop_recording_and_plot(self, channel):
        self.recorder.stop_recording()
        waveform_data = self.recorder.get_audio_data(channel)
        self.plot_audio_data(channel, waveform_data)

    def plot_audio_data(self, channel, data):
        if 1 <= channel <= 6:
            logging.info(f"Audio data for channel {channel}: {data}")
            if data is not None:
                self.mpl_widgets[channel - 1].plot_audio_data(data)
        
    def show(self):
        self.ui.show()
        