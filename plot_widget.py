import numpy as np
from pyqtgraph import PlotWidget, mkPen

class PGWidget(PlotWidget):
    def __init__(self, parent=None):
        super(PGWidget, self).__init__(parent)
        self.setBackground('#141414')
        self.getPlotItem().hideAxis('left')
        self.getPlotItem().hideAxis('bottom')

    def plot_audio_data(self, t, data):
        self.clear()
        if data.ndim == 2:
            data = data.mean(axis=1)  # Average the two channels
        self.plot(t, data, pen=mkPen('#b055c8', width=1))