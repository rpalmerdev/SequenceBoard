# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowlYFmYR.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.play_audio_button = QPushButton(self.centralwidget)
        self.play_audio_button.setObjectName(u"play_audio_button")
        self.play_audio_button.setGeometry(QRect(50, 60, 75, 24))
        self.stop_audio_button = QPushButton(self.centralwidget)
        self.stop_audio_button.setObjectName(u"stop_audio_button")
        self.stop_audio_button.setGeometry(QRect(50, 110, 75, 24))
        self.record_audio_button = QPushButton(self.centralwidget)
        self.record_audio_button.setObjectName(u"record_audio_button")
        self.record_audio_button.setGeometry(QRect(50, 160, 75, 24))
        self.volume_slider_1 = QSlider(self.centralwidget)
        self.volume_slider_1.setObjectName(u"volume_slider_1")
        self.volume_slider_1.setGeometry(QRect(730, 40, 18, 160))
        self.volume_slider_1.setSliderPosition(75)
        self.volume_slider_1.setOrientation(Qt.Vertical)
        self.volume_label_1 = QLabel(self.centralwidget)
        self.volume_label_1.setObjectName(u"volume_label_1")
        self.volume_label_1.setGeometry(QRect(680, 180, 49, 16))
        self.volume_label_1.setAlignment(Qt.AlignCenter)
        self.volume_line_L = QFrame(self.centralwidget)
        self.volume_line_L.setObjectName(u"volume_line_L")
        self.volume_line_L.setGeometry(QRect(690, 70, 31, 20))
        self.volume_line_L.setFrameShape(QFrame.HLine)
        self.volume_line_L.setFrameShadow(QFrame.Sunken)
        self.volume_line_R = QFrame(self.centralwidget)
        self.volume_line_R.setObjectName(u"volume_line_R")
        self.volume_line_R.setGeometry(QRect(750, 70, 31, 20))
        self.volume_line_R.setFrameShape(QFrame.HLine)
        self.volume_line_R.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sequence Board", None))
        self.play_audio_button.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.stop_audio_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.record_audio_button.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.volume_label_1.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
    # retranslateUi

