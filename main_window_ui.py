# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

from user_interface.py import MPLWidget
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 586)
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.main_window_label = QLabel(self.centralwidget)
        self.main_window_label.setObjectName(u"main_window_label")
        self.main_window_label.setGeometry(QRect(11, 11, 234, 43))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.main_window_label.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 70, 921, 431))
        self.stripLayout = QVBoxLayout(self.layoutWidget)
        self.stripLayout.setObjectName(u"stripLayout")
        self.stripLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(3, 1, 5, 9)
        self.play_button_6 = QPushButton(self.layoutWidget)
        self.play_button_6.setObjectName(u"play_button_6")

        self.gridLayout.addWidget(self.play_button_6, 3, 10, 1, 1)

        self.mplwidget_1 = MPLWidget(self.layoutWidget)
        self.mplwidget_1.setObjectName(u"mplwidget_1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplwidget_1.sizePolicy().hasHeightForWidth())
        self.mplwidget_1.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setBold(False)
        font2.setKerning(False)
        self.mplwidget_1.setFont(font2)
        self.mplwidget_1.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.mplwidget_1, 2, 0, 1, 1)

        self.play_button_4 = QPushButton(self.layoutWidget)
        self.play_button_4.setObjectName(u"play_button_4")

        self.gridLayout.addWidget(self.play_button_4, 3, 6, 1, 1)

        self.mplwidget_6 = MPLWidget(self.layoutWidget)
        self.mplwidget_6.setObjectName(u"mplwidget_6")
        sizePolicy.setHeightForWidth(self.mplwidget_6.sizePolicy().hasHeightForWidth())
        self.mplwidget_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.mplwidget_6, 2, 10, 1, 1)

        self.gain_splitter_3 = QHBoxLayout()
        self.gain_splitter_3.setObjectName(u"gain_splitter_3")
        self.gain_slider_3 = QSlider(self.layoutWidget)
        self.gain_slider_3.setObjectName(u"gain_slider_3")
        self.gain_slider_3.setMinimumSize(QSize(0, 200))
        self.gain_slider_3.setValue(75)
        self.gain_slider_3.setOrientation(Qt.Vertical)

        self.gain_splitter_3.addWidget(self.gain_slider_3)

        self.gain_meter_3 = QProgressBar(self.layoutWidget)
        self.gain_meter_3.setObjectName(u"gain_meter_3")
        self.gain_meter_3.setValue(75)
        self.gain_meter_3.setTextVisible(False)
        self.gain_meter_3.setOrientation(Qt.Vertical)

        self.gain_splitter_3.addWidget(self.gain_meter_3)


        self.gridLayout.addLayout(self.gain_splitter_3, 1, 4, 1, 1)

        self.record_button_1 = QPushButton(self.layoutWidget)
        self.record_button_1.setObjectName(u"record_button_1")

        self.gridLayout.addWidget(self.record_button_1, 4, 0, 1, 1)

        self.mplwidget_5 = MPLWidget(self.layoutWidget)
        self.mplwidget_5.setObjectName(u"mplwidget_5")
        sizePolicy.setHeightForWidth(self.mplwidget_5.sizePolicy().hasHeightForWidth())
        self.mplwidget_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.mplwidget_5, 2, 8, 1, 1)

        self.play_button_2 = QPushButton(self.layoutWidget)
        self.play_button_2.setObjectName(u"play_button_2")

        self.gridLayout.addWidget(self.play_button_2, 3, 2, 1, 1)

        self.channel_spacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_1, 1, 1, 1, 1)

        self.strip_4 = QLabel(self.layoutWidget)
        self.strip_4.setObjectName(u"strip_4")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.strip_4.setFont(font3)
        self.strip_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_4, 0, 6, 1, 1)

        self.gain_splitter_1 = QHBoxLayout()
        self.gain_splitter_1.setObjectName(u"gain_splitter_1")
        self.gain_slider_1 = QSlider(self.layoutWidget)
        self.gain_slider_1.setObjectName(u"gain_slider_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gain_slider_1.sizePolicy().hasHeightForWidth())
        self.gain_slider_1.setSizePolicy(sizePolicy1)
        self.gain_slider_1.setMinimumSize(QSize(0, 200))
        self.gain_slider_1.setValue(75)
        self.gain_slider_1.setSliderPosition(75)
        self.gain_slider_1.setOrientation(Qt.Vertical)

        self.gain_splitter_1.addWidget(self.gain_slider_1)

        self.gain_meter_1 = QProgressBar(self.layoutWidget)
        self.gain_meter_1.setObjectName(u"gain_meter_1")
        self.gain_meter_1.setValue(75)
        self.gain_meter_1.setTextVisible(False)
        self.gain_meter_1.setOrientation(Qt.Vertical)

        self.gain_splitter_1.addWidget(self.gain_meter_1)


        self.gridLayout.addLayout(self.gain_splitter_1, 1, 0, 1, 1)

        self.gain_splitter_4 = QHBoxLayout()
        self.gain_splitter_4.setObjectName(u"gain_splitter_4")
        self.gain_slider_4 = QSlider(self.layoutWidget)
        self.gain_slider_4.setObjectName(u"gain_slider_4")
        self.gain_slider_4.setMinimumSize(QSize(0, 200))
        self.gain_slider_4.setValue(75)
        self.gain_slider_4.setOrientation(Qt.Vertical)

        self.gain_splitter_4.addWidget(self.gain_slider_4)

        self.gain_meter_4 = QProgressBar(self.layoutWidget)
        self.gain_meter_4.setObjectName(u"gain_meter_4")
        self.gain_meter_4.setMinimumSize(QSize(0, 200))
        self.gain_meter_4.setValue(75)
        self.gain_meter_4.setTextVisible(False)
        self.gain_meter_4.setOrientation(Qt.Vertical)

        self.gain_splitter_4.addWidget(self.gain_meter_4)


        self.gridLayout.addLayout(self.gain_splitter_4, 1, 6, 1, 1)

        self.record_button_4 = QPushButton(self.layoutWidget)
        self.record_button_4.setObjectName(u"record_button_4")

        self.gridLayout.addWidget(self.record_button_4, 4, 6, 1, 1)

        self.play_button_1 = QPushButton(self.layoutWidget)
        self.play_button_1.setObjectName(u"play_button_1")

        self.gridLayout.addWidget(self.play_button_1, 3, 0, 1, 1)

        self.strip_5 = QLabel(self.layoutWidget)
        self.strip_5.setObjectName(u"strip_5")
        self.strip_5.setFont(font3)
        self.strip_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_5, 0, 8, 1, 1)

        self.play_button_5 = QPushButton(self.layoutWidget)
        self.play_button_5.setObjectName(u"play_button_5")

        self.gridLayout.addWidget(self.play_button_5, 3, 8, 1, 1)

        self.channel_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_2, 1, 3, 1, 1)

        self.gain_splitter_2 = QHBoxLayout()
        self.gain_splitter_2.setObjectName(u"gain_splitter_2")
        self.gain_slider_2 = QSlider(self.layoutWidget)
        self.gain_slider_2.setObjectName(u"gain_slider_2")
        self.gain_slider_2.setMinimumSize(QSize(0, 200))
        self.gain_slider_2.setValue(75)
        self.gain_slider_2.setOrientation(Qt.Vertical)

        self.gain_splitter_2.addWidget(self.gain_slider_2)

        self.gain_meter_2 = QProgressBar(self.layoutWidget)
        self.gain_meter_2.setObjectName(u"gain_meter_2")
        self.gain_meter_2.setValue(75)
        self.gain_meter_2.setTextVisible(False)
        self.gain_meter_2.setOrientation(Qt.Vertical)

        self.gain_splitter_2.addWidget(self.gain_meter_2)


        self.gridLayout.addLayout(self.gain_splitter_2, 1, 2, 1, 1)

        self.strip_2 = QLabel(self.layoutWidget)
        self.strip_2.setObjectName(u"strip_2")
        self.strip_2.setFont(font3)
        self.strip_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_2, 0, 2, 1, 1)

        self.gain_splitter_5 = QHBoxLayout()
        self.gain_splitter_5.setObjectName(u"gain_splitter_5")
        self.gain_slider_5 = QSlider(self.layoutWidget)
        self.gain_slider_5.setObjectName(u"gain_slider_5")
        self.gain_slider_5.setMinimumSize(QSize(0, 200))
        self.gain_slider_5.setValue(75)
        self.gain_slider_5.setOrientation(Qt.Vertical)

        self.gain_splitter_5.addWidget(self.gain_slider_5)

        self.gain_meter_5 = QProgressBar(self.layoutWidget)
        self.gain_meter_5.setObjectName(u"gain_meter_5")
        self.gain_meter_5.setValue(75)
        self.gain_meter_5.setTextVisible(False)
        self.gain_meter_5.setOrientation(Qt.Vertical)

        self.gain_splitter_5.addWidget(self.gain_meter_5)


        self.gridLayout.addLayout(self.gain_splitter_5, 1, 8, 1, 1)

        self.gain_splitter_6 = QHBoxLayout()
        self.gain_splitter_6.setObjectName(u"gain_splitter_6")
        self.gain_slider_6 = QSlider(self.layoutWidget)
        self.gain_slider_6.setObjectName(u"gain_slider_6")
        self.gain_slider_6.setMinimumSize(QSize(0, 200))
        self.gain_slider_6.setValue(75)
        self.gain_slider_6.setOrientation(Qt.Vertical)

        self.gain_splitter_6.addWidget(self.gain_slider_6)

        self.gain_meter_6 = QProgressBar(self.layoutWidget)
        self.gain_meter_6.setObjectName(u"gain_meter_6")
        self.gain_meter_6.setValue(75)
        self.gain_meter_6.setTextVisible(False)
        self.gain_meter_6.setOrientation(Qt.Vertical)

        self.gain_splitter_6.addWidget(self.gain_meter_6)


        self.gridLayout.addLayout(self.gain_splitter_6, 1, 10, 1, 1)

        self.channel_spacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_3, 1, 5, 1, 1)

        self.channel_spacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_4, 1, 7, 1, 1)

        self.strip_1 = QLabel(self.layoutWidget)
        self.strip_1.setObjectName(u"strip_1")
        self.strip_1.setFont(font3)
        self.strip_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_1, 0, 0, 1, 1)

        self.strip_3 = QLabel(self.layoutWidget)
        self.strip_3.setObjectName(u"strip_3")
        self.strip_3.setFont(font3)
        self.strip_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_3, 0, 4, 1, 1)

        self.mplwidget_2 = MPLWidget(self.layoutWidget)
        self.mplwidget_2.setObjectName(u"mplwidget_2")
        sizePolicy.setHeightForWidth(self.mplwidget_2.sizePolicy().hasHeightForWidth())
        self.mplwidget_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.mplwidget_2, 2, 2, 1, 1)

        self.mplwidget_3 = MPLWidget(self.layoutWidget)
        self.mplwidget_3.setObjectName(u"mplwidget_3")
        sizePolicy.setHeightForWidth(self.mplwidget_3.sizePolicy().hasHeightForWidth())
        self.mplwidget_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.mplwidget_3, 2, 4, 1, 1)

        self.record_button_6 = QPushButton(self.layoutWidget)
        self.record_button_6.setObjectName(u"record_button_6")

        self.gridLayout.addWidget(self.record_button_6, 4, 10, 1, 1)

        self.mplwidget_4 = MPLWidget(self.layoutWidget)
        self.mplwidget_4.setObjectName(u"mplwidget_4")
        sizePolicy.setHeightForWidth(self.mplwidget_4.sizePolicy().hasHeightForWidth())
        self.mplwidget_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.mplwidget_4, 2, 6, 1, 1)

        self.record_button_3 = QPushButton(self.layoutWidget)
        self.record_button_3.setObjectName(u"record_button_3")

        self.gridLayout.addWidget(self.record_button_3, 4, 4, 1, 1)

        self.record_button_5 = QPushButton(self.layoutWidget)
        self.record_button_5.setObjectName(u"record_button_5")

        self.gridLayout.addWidget(self.record_button_5, 4, 8, 1, 1)

        self.play_button_3 = QPushButton(self.layoutWidget)
        self.play_button_3.setObjectName(u"play_button_3")

        self.gridLayout.addWidget(self.play_button_3, 3, 4, 1, 1)

        self.record_button_2 = QPushButton(self.layoutWidget)
        self.record_button_2.setObjectName(u"record_button_2")

        self.gridLayout.addWidget(self.record_button_2, 4, 2, 1, 1)

        self.strip_6 = QLabel(self.layoutWidget)
        self.strip_6.setObjectName(u"strip_6")
        self.strip_6.setFont(font3)
        self.strip_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_6, 0, 10, 1, 1)

        self.channel_spacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_5, 1, 9, 1, 1)


        self.stripLayout.addLayout(self.gridLayout)

        self.recordingLayout = QHBoxLayout()
        self.recordingLayout.setSpacing(65)
        self.recordingLayout.setObjectName(u"recordingLayout")
        self.recording_1 = QLabel(self.layoutWidget)
        self.recording_1.setObjectName(u"recording_1")
        self.recording_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.recordingLayout.addWidget(self.recording_1)

        self.recording_2 = QLabel(self.layoutWidget)
        self.recording_2.setObjectName(u"recording_2")
        self.recording_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.recordingLayout.addWidget(self.recording_2)

        self.recording_3 = QLabel(self.layoutWidget)
        self.recording_3.setObjectName(u"recording_3")
        self.recording_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.recordingLayout.addWidget(self.recording_3)

        self.recording_4 = QLabel(self.layoutWidget)
        self.recording_4.setObjectName(u"recording_4")
        self.recording_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.recordingLayout.addWidget(self.recording_4)

        self.recording_5 = QLabel(self.layoutWidget)
        self.recording_5.setObjectName(u"recording_5")
        self.recording_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.recordingLayout.addWidget(self.recording_5)

        self.recording_6 = QLabel(self.layoutWidget)
        self.recording_6.setObjectName(u"recording_6")
        self.recording_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.recordingLayout.addWidget(self.recording_6)


        self.stripLayout.addLayout(self.recordingLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sequence Board", None))
        self.main_window_label.setText(QCoreApplication.translate("MainWindow", u"SequenceBoard", None))
        self.play_button_6.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.play_button_4.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.record_button_1.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.play_button_2.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.strip_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.record_button_4.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.play_button_1.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.strip_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.play_button_5.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.strip_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.strip_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.strip_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.record_button_6.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.record_button_3.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.record_button_5.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.play_button_3.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.record_button_2.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.strip_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.recording_1.setText("")
        self.recording_2.setText("")
        self.recording_3.setText("")
        self.recording_4.setText("")
        self.recording_5.setText("")
        self.recording_6.setText("")
    # retranslateUi

