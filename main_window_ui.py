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
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 575)
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
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 80, 821, 300))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.play_button_c2 = QPushButton(self.gridLayoutWidget)
        self.play_button_c2.setObjectName(u"play_button_c2")

        self.gridLayout.addWidget(self.play_button_c2, 2, 2, 1, 1)

        self.record_button_c1 = QPushButton(self.gridLayoutWidget)
        self.record_button_c1.setObjectName(u"record_button_c1")

        self.gridLayout.addWidget(self.record_button_c1, 3, 0, 1, 1)

        self.recording_5 = QLabel(self.gridLayoutWidget)
        self.recording_5.setObjectName(u"recording_5")
        self.recording_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recording_5, 4, 8, 1, 1)

        self.channel_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_2, 1, 3, 1, 1)

        self.record_button_c5 = QPushButton(self.gridLayoutWidget)
        self.record_button_c5.setObjectName(u"record_button_c5")

        self.gridLayout.addWidget(self.record_button_c5, 3, 8, 1, 1)

        self.play_button_c4 = QPushButton(self.gridLayoutWidget)
        self.play_button_c4.setObjectName(u"play_button_c4")

        self.gridLayout.addWidget(self.play_button_c4, 2, 6, 1, 1)

        self.gain_splitter_5 = QHBoxLayout()
        self.gain_splitter_5.setObjectName(u"gain_splitter_5")
        self.gain_slider_5 = QSlider(self.gridLayoutWidget)
        self.gain_slider_5.setObjectName(u"gain_slider_5")
        self.gain_slider_5.setValue(75)
        self.gain_slider_5.setOrientation(Qt.Vertical)

        self.gain_splitter_5.addWidget(self.gain_slider_5)

        self.gain_meter_5 = QProgressBar(self.gridLayoutWidget)
        self.gain_meter_5.setObjectName(u"gain_meter_5")
        self.gain_meter_5.setValue(0)
        self.gain_meter_5.setTextVisible(False)
        self.gain_meter_5.setOrientation(Qt.Vertical)

        self.gain_splitter_5.addWidget(self.gain_meter_5)


        self.gridLayout.addLayout(self.gain_splitter_5, 1, 8, 1, 1)

        self.play_button_c5 = QPushButton(self.gridLayoutWidget)
        self.play_button_c5.setObjectName(u"play_button_c5")

        self.gridLayout.addWidget(self.play_button_c5, 2, 8, 1, 1)

        self.play_button_c3 = QPushButton(self.gridLayoutWidget)
        self.play_button_c3.setObjectName(u"play_button_c3")

        self.gridLayout.addWidget(self.play_button_c3, 2, 4, 1, 1)

        self.strip_4 = QLabel(self.gridLayoutWidget)
        self.strip_4.setObjectName(u"strip_4")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.strip_4.setFont(font2)
        self.strip_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_4, 0, 6, 1, 1)

        self.recording_4 = QLabel(self.gridLayoutWidget)
        self.recording_4.setObjectName(u"recording_4")
        self.recording_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recording_4, 4, 6, 1, 1)

        self.gain_splitter_2 = QHBoxLayout()
        self.gain_splitter_2.setObjectName(u"gain_splitter_2")
        self.gain_slider_2 = QSlider(self.gridLayoutWidget)
        self.gain_slider_2.setObjectName(u"gain_slider_2")
        self.gain_slider_2.setValue(75)
        self.gain_slider_2.setOrientation(Qt.Vertical)

        self.gain_splitter_2.addWidget(self.gain_slider_2)

        self.gain_meter_2 = QProgressBar(self.gridLayoutWidget)
        self.gain_meter_2.setObjectName(u"gain_meter_2")
        self.gain_meter_2.setValue(0)
        self.gain_meter_2.setTextVisible(False)
        self.gain_meter_2.setOrientation(Qt.Vertical)

        self.gain_splitter_2.addWidget(self.gain_meter_2)


        self.gridLayout.addLayout(self.gain_splitter_2, 1, 2, 1, 1)

        self.gain_splitter_4 = QHBoxLayout()
        self.gain_splitter_4.setObjectName(u"gain_splitter_4")
        self.gain_slider_4 = QSlider(self.gridLayoutWidget)
        self.gain_slider_4.setObjectName(u"gain_slider_4")
        self.gain_slider_4.setValue(75)
        self.gain_slider_4.setOrientation(Qt.Vertical)

        self.gain_splitter_4.addWidget(self.gain_slider_4)

        self.gain_meter_4 = QProgressBar(self.gridLayoutWidget)
        self.gain_meter_4.setObjectName(u"gain_meter_4")
        self.gain_meter_4.setValue(0)
        self.gain_meter_4.setTextVisible(False)
        self.gain_meter_4.setOrientation(Qt.Vertical)

        self.gain_splitter_4.addWidget(self.gain_meter_4)


        self.gridLayout.addLayout(self.gain_splitter_4, 1, 6, 1, 1)

        self.channel_spacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_3, 1, 5, 1, 1)

        self.recording_3 = QLabel(self.gridLayoutWidget)
        self.recording_3.setObjectName(u"recording_3")
        self.recording_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recording_3, 4, 4, 1, 1)

        self.record_button_c4 = QPushButton(self.gridLayoutWidget)
        self.record_button_c4.setObjectName(u"record_button_c4")

        self.gridLayout.addWidget(self.record_button_c4, 3, 6, 1, 1)

        self.gain_splitter_1 = QHBoxLayout()
        self.gain_splitter_1.setObjectName(u"gain_splitter_1")
        self.gain_slider_1 = QSlider(self.gridLayoutWidget)
        self.gain_slider_1.setObjectName(u"gain_slider_1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gain_slider_1.sizePolicy().hasHeightForWidth())
        self.gain_slider_1.setSizePolicy(sizePolicy)
        self.gain_slider_1.setValue(75)
        self.gain_slider_1.setSliderPosition(75)
        self.gain_slider_1.setOrientation(Qt.Vertical)

        self.gain_splitter_1.addWidget(self.gain_slider_1)

        self.gain_meter_1 = QProgressBar(self.gridLayoutWidget)
        self.gain_meter_1.setObjectName(u"gain_meter_1")
        self.gain_meter_1.setValue(0)
        self.gain_meter_1.setTextVisible(False)
        self.gain_meter_1.setOrientation(Qt.Vertical)

        self.gain_splitter_1.addWidget(self.gain_meter_1)


        self.gridLayout.addLayout(self.gain_splitter_1, 1, 0, 1, 1)

        self.record_button_c3 = QPushButton(self.gridLayoutWidget)
        self.record_button_c3.setObjectName(u"record_button_c3")

        self.gridLayout.addWidget(self.record_button_c3, 3, 4, 1, 1)

        self.gain_splitter_3 = QHBoxLayout()
        self.gain_splitter_3.setObjectName(u"gain_splitter_3")
        self.gain_slider_3 = QSlider(self.gridLayoutWidget)
        self.gain_slider_3.setObjectName(u"gain_slider_3")
        self.gain_slider_3.setValue(75)
        self.gain_slider_3.setOrientation(Qt.Vertical)

        self.gain_splitter_3.addWidget(self.gain_slider_3)

        self.gain_meter_3 = QProgressBar(self.gridLayoutWidget)
        self.gain_meter_3.setObjectName(u"gain_meter_3")
        self.gain_meter_3.setValue(0)
        self.gain_meter_3.setTextVisible(False)
        self.gain_meter_3.setOrientation(Qt.Vertical)

        self.gain_splitter_3.addWidget(self.gain_meter_3)


        self.gridLayout.addLayout(self.gain_splitter_3, 1, 4, 1, 1)

        self.strip_2 = QLabel(self.gridLayoutWidget)
        self.strip_2.setObjectName(u"strip_2")
        self.strip_2.setFont(font2)
        self.strip_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_2, 0, 2, 1, 1)

        self.strip_6 = QLabel(self.gridLayoutWidget)
        self.strip_6.setObjectName(u"strip_6")
        self.strip_6.setFont(font2)
        self.strip_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_6, 0, 10, 1, 1)

        self.record_button_c2 = QPushButton(self.gridLayoutWidget)
        self.record_button_c2.setObjectName(u"record_button_c2")

        self.gridLayout.addWidget(self.record_button_c2, 3, 2, 1, 1)

        self.recording_1 = QLabel(self.gridLayoutWidget)
        self.recording_1.setObjectName(u"recording_1")
        self.recording_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recording_1, 4, 0, 1, 1)

        self.play_button_c1 = QPushButton(self.gridLayoutWidget)
        self.play_button_c1.setObjectName(u"play_button_c1")

        self.gridLayout.addWidget(self.play_button_c1, 2, 0, 1, 1)

        self.channel_spacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_1, 1, 1, 1, 1)

        self.strip_5 = QLabel(self.gridLayoutWidget)
        self.strip_5.setObjectName(u"strip_5")
        self.strip_5.setFont(font2)
        self.strip_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_5, 0, 8, 1, 1)

        self.recording_6 = QLabel(self.gridLayoutWidget)
        self.recording_6.setObjectName(u"recording_6")
        self.recording_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recording_6, 4, 10, 1, 1)

        self.strip_1 = QLabel(self.gridLayoutWidget)
        self.strip_1.setObjectName(u"strip_1")
        self.strip_1.setFont(font2)
        self.strip_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_1, 0, 0, 1, 1)

        self.channel_spacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_4, 1, 7, 1, 1)

        self.recording_2 = QLabel(self.gridLayoutWidget)
        self.recording_2.setObjectName(u"recording_2")
        self.recording_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.recording_2, 4, 2, 1, 1)

        self.play_button_c6 = QPushButton(self.gridLayoutWidget)
        self.play_button_c6.setObjectName(u"play_button_c6")

        self.gridLayout.addWidget(self.play_button_c6, 2, 10, 1, 1)

        self.record_button_c6 = QPushButton(self.gridLayoutWidget)
        self.record_button_c6.setObjectName(u"record_button_c6")

        self.gridLayout.addWidget(self.record_button_c6, 3, 10, 1, 1)

        self.gain_splitter_6 = QHBoxLayout()
        self.gain_splitter_6.setObjectName(u"gain_splitter_6")
        self.gain_slider_6 = QSlider(self.gridLayoutWidget)
        self.gain_slider_6.setObjectName(u"gain_slider_6")
        self.gain_slider_6.setValue(75)
        self.gain_slider_6.setOrientation(Qt.Vertical)

        self.gain_splitter_6.addWidget(self.gain_slider_6)

        self.gain_meter_6 = QProgressBar(self.gridLayoutWidget)
        self.gain_meter_6.setObjectName(u"gain_meter_6")
        self.gain_meter_6.setValue(0)
        self.gain_meter_6.setTextVisible(False)
        self.gain_meter_6.setOrientation(Qt.Vertical)

        self.gain_splitter_6.addWidget(self.gain_meter_6)


        self.gridLayout.addLayout(self.gain_splitter_6, 1, 10, 1, 1)

        self.strip_3 = QLabel(self.gridLayoutWidget)
        self.strip_3.setObjectName(u"strip_3")
        self.strip_3.setFont(font2)
        self.strip_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.strip_3, 0, 4, 1, 1)

        self.channel_spacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.channel_spacer_5, 1, 9, 1, 1)

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
        self.play_button_c2.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.record_button_c1.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.recording_5.setText(QCoreApplication.translate("MainWindow", u"Recording!", None))
        self.record_button_c5.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.play_button_c4.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.play_button_c5.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.play_button_c3.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.strip_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.recording_4.setText(QCoreApplication.translate("MainWindow", u"Recording!", None))
        self.recording_3.setText(QCoreApplication.translate("MainWindow", u"Recording!", None))
        self.record_button_c4.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.record_button_c3.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.strip_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.strip_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.record_button_c2.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.recording_1.setText(QCoreApplication.translate("MainWindow", u"Recording!", None))
        self.play_button_c1.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.strip_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.recording_6.setText(QCoreApplication.translate("MainWindow", u"Recording!", None))
        self.strip_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.recording_2.setText(QCoreApplication.translate("MainWindow", u"Recording!", None))
        self.play_button_c6.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.record_button_c6.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.strip_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
    # retranslateUi

