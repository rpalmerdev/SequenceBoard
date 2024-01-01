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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

from double_range_slider.py import DoubleRangeSlider
from plot_widget.py import PGWidget
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(688, 445)
        font = QFont()
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout_15 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.main_window_label = QLabel(self.frame)
        self.main_window_label.setObjectName(u"main_window_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_window_label.sizePolicy().hasHeightForWidth())
        self.main_window_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.main_window_label.setFont(font1)

        self.verticalLayout_13.addWidget(self.main_window_label)


        self.verticalLayout_14.addWidget(self.frame)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.labelFrame_1 = QFrame(self.centralwidget)
        self.labelFrame_1.setObjectName(u"labelFrame_1")
        self.labelFrame_1.setFrameShape(QFrame.StyledPanel)
        self.labelFrame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.labelFrame_1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.strip_label_1 = QLabel(self.labelFrame_1)
        self.strip_label_1.setObjectName(u"strip_label_1")
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.strip_label_1.setFont(font2)
        self.strip_label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.strip_label_1)


        self.verticalLayout_7.addWidget(self.labelFrame_1)

        self.volume_frame_1 = QFrame(self.centralwidget)
        self.volume_frame_1.setObjectName(u"volume_frame_1")
        self.volume_frame_1.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.volume_frame_1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.gain_slider_1 = QSlider(self.volume_frame_1)
        self.gain_slider_1.setObjectName(u"gain_slider_1")
        sizePolicy.setHeightForWidth(self.gain_slider_1.sizePolicy().hasHeightForWidth())
        self.gain_slider_1.setSizePolicy(sizePolicy)
        self.gain_slider_1.setMinimumSize(QSize(0, 100))
        self.gain_slider_1.setValue(75)
        self.gain_slider_1.setSliderPosition(75)
        self.gain_slider_1.setOrientation(Qt.Vertical)

        self.horizontalLayout_7.addWidget(self.gain_slider_1)

        self.gain_meter_1 = QProgressBar(self.volume_frame_1)
        self.gain_meter_1.setObjectName(u"gain_meter_1")
        sizePolicy.setHeightForWidth(self.gain_meter_1.sizePolicy().hasHeightForWidth())
        self.gain_meter_1.setSizePolicy(sizePolicy)
        self.gain_meter_1.setMinimumSize(QSize(0, 100))
        self.gain_meter_1.setValue(75)
        self.gain_meter_1.setTextVisible(False)
        self.gain_meter_1.setOrientation(Qt.Vertical)

        self.horizontalLayout_7.addWidget(self.gain_meter_1)


        self.verticalLayout_7.addWidget(self.volume_frame_1)

        self.mplFrame_1 = QFrame(self.centralwidget)
        self.mplFrame_1.setObjectName(u"mplFrame_1")
        self.mplFrame_1.setFrameShape(QFrame.StyledPanel)
        self.mplFrame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mplFrame_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pgwidget_1 = PGWidget(self.mplFrame_1)
        self.pgwidget_1.setObjectName(u"pgwidget_1")

        self.verticalLayout.addWidget(self.pgwidget_1)

        self.doubleslider_1 = DoubleRangeSlider(self.mplFrame_1)
        self.doubleslider_1.setObjectName(u"doubleslider_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.doubleslider_1.sizePolicy().hasHeightForWidth())
        self.doubleslider_1.setSizePolicy(sizePolicy1)
        self.doubleslider_1.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.doubleslider_1)


        self.verticalLayout_7.addWidget(self.mplFrame_1)

        self.button_frame_1 = QFrame(self.centralwidget)
        self.button_frame_1.setObjectName(u"button_frame_1")
        self.button_frame_1.setFrameShape(QFrame.StyledPanel)
        self.button_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.button_frame_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.play_button_1 = QPushButton(self.button_frame_1)
        self.play_button_1.setObjectName(u"play_button_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.play_button_1.sizePolicy().hasHeightForWidth())
        self.play_button_1.setSizePolicy(sizePolicy2)
        self.play_button_1.setMinimumSize(QSize(0, 0))
        self.play_button_1.setMaximumSize(QSize(60, 40))
        self.play_button_1.setStyleSheet(u"image: url(:/play_icon.png);")

        self.horizontalLayout.addWidget(self.play_button_1)

        self.record_button_1 = QPushButton(self.button_frame_1)
        self.record_button_1.setObjectName(u"record_button_1")
        sizePolicy2.setHeightForWidth(self.record_button_1.sizePolicy().hasHeightForWidth())
        self.record_button_1.setSizePolicy(sizePolicy2)
        self.record_button_1.setMaximumSize(QSize(60, 40))
        self.record_button_1.setStyleSheet(u"image: url(:/record_icon.png);")

        self.horizontalLayout.addWidget(self.record_button_1)


        self.verticalLayout_7.addWidget(self.button_frame_1)


        self.horizontalLayout_19.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelFrame_2 = QFrame(self.centralwidget)
        self.labelFrame_2.setObjectName(u"labelFrame_2")
        self.labelFrame_2.setFrameShape(QFrame.StyledPanel)
        self.labelFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.labelFrame_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.strip_label_2 = QLabel(self.labelFrame_2)
        self.strip_label_2.setObjectName(u"strip_label_2")
        self.strip_label_2.setFont(font2)
        self.strip_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.strip_label_2)


        self.verticalLayout_8.addWidget(self.labelFrame_2)

        self.volume_frame_2 = QFrame(self.centralwidget)
        self.volume_frame_2.setObjectName(u"volume_frame_2")
        self.volume_frame_2.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.volume_frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gain_slider_2 = QSlider(self.volume_frame_2)
        self.gain_slider_2.setObjectName(u"gain_slider_2")
        sizePolicy.setHeightForWidth(self.gain_slider_2.sizePolicy().hasHeightForWidth())
        self.gain_slider_2.setSizePolicy(sizePolicy)
        self.gain_slider_2.setMinimumSize(QSize(0, 100))
        self.gain_slider_2.setValue(75)
        self.gain_slider_2.setOrientation(Qt.Vertical)

        self.horizontalLayout_8.addWidget(self.gain_slider_2)

        self.gain_meter_2 = QProgressBar(self.volume_frame_2)
        self.gain_meter_2.setObjectName(u"gain_meter_2")
        sizePolicy.setHeightForWidth(self.gain_meter_2.sizePolicy().hasHeightForWidth())
        self.gain_meter_2.setSizePolicy(sizePolicy)
        self.gain_meter_2.setMinimumSize(QSize(0, 100))
        self.gain_meter_2.setValue(75)
        self.gain_meter_2.setTextVisible(False)
        self.gain_meter_2.setOrientation(Qt.Vertical)

        self.horizontalLayout_8.addWidget(self.gain_meter_2)


        self.verticalLayout_8.addWidget(self.volume_frame_2)

        self.mplFrame_2 = QFrame(self.centralwidget)
        self.mplFrame_2.setObjectName(u"mplFrame_2")
        self.mplFrame_2.setFrameShape(QFrame.StyledPanel)
        self.mplFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mplFrame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pgwidget_2 = PGWidget(self.mplFrame_2)
        self.pgwidget_2.setObjectName(u"pgwidget_2")

        self.verticalLayout_2.addWidget(self.pgwidget_2)

        self.doubleslider_2 = DoubleRangeSlider(self.mplFrame_2)
        self.doubleslider_2.setObjectName(u"doubleslider_2")
        sizePolicy1.setHeightForWidth(self.doubleslider_2.sizePolicy().hasHeightForWidth())
        self.doubleslider_2.setSizePolicy(sizePolicy1)
        self.doubleslider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.doubleslider_2)


        self.verticalLayout_8.addWidget(self.mplFrame_2)

        self.button_frame_2 = QFrame(self.centralwidget)
        self.button_frame_2.setObjectName(u"button_frame_2")
        self.button_frame_2.setFrameShape(QFrame.StyledPanel)
        self.button_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.button_frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.play_button_2 = QPushButton(self.button_frame_2)
        self.play_button_2.setObjectName(u"play_button_2")
        sizePolicy2.setHeightForWidth(self.play_button_2.sizePolicy().hasHeightForWidth())
        self.play_button_2.setSizePolicy(sizePolicy2)
        self.play_button_2.setMaximumSize(QSize(60, 40))
        self.play_button_2.setStyleSheet(u"image: url(:/play_icon.png);")

        self.horizontalLayout_2.addWidget(self.play_button_2)

        self.record_button_2 = QPushButton(self.button_frame_2)
        self.record_button_2.setObjectName(u"record_button_2")
        sizePolicy2.setHeightForWidth(self.record_button_2.sizePolicy().hasHeightForWidth())
        self.record_button_2.setSizePolicy(sizePolicy2)
        self.record_button_2.setMaximumSize(QSize(60, 40))
        self.record_button_2.setStyleSheet(u"image: url(:/record_icon.png);")

        self.horizontalLayout_2.addWidget(self.record_button_2)


        self.verticalLayout_8.addWidget(self.button_frame_2)


        self.horizontalLayout_19.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.labelFrame_3 = QFrame(self.centralwidget)
        self.labelFrame_3.setObjectName(u"labelFrame_3")
        self.labelFrame_3.setFrameShape(QFrame.StyledPanel)
        self.labelFrame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.labelFrame_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.strip_label_3 = QLabel(self.labelFrame_3)
        self.strip_label_3.setObjectName(u"strip_label_3")
        self.strip_label_3.setFont(font2)
        self.strip_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.strip_label_3)


        self.verticalLayout_9.addWidget(self.labelFrame_3)

        self.volume_frame_3 = QFrame(self.centralwidget)
        self.volume_frame_3.setObjectName(u"volume_frame_3")
        self.volume_frame_3.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.volume_frame_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gain_slider_3 = QSlider(self.volume_frame_3)
        self.gain_slider_3.setObjectName(u"gain_slider_3")
        sizePolicy.setHeightForWidth(self.gain_slider_3.sizePolicy().hasHeightForWidth())
        self.gain_slider_3.setSizePolicy(sizePolicy)
        self.gain_slider_3.setMinimumSize(QSize(0, 100))
        self.gain_slider_3.setValue(75)
        self.gain_slider_3.setOrientation(Qt.Vertical)

        self.horizontalLayout_9.addWidget(self.gain_slider_3)

        self.gain_meter_3 = QProgressBar(self.volume_frame_3)
        self.gain_meter_3.setObjectName(u"gain_meter_3")
        sizePolicy.setHeightForWidth(self.gain_meter_3.sizePolicy().hasHeightForWidth())
        self.gain_meter_3.setSizePolicy(sizePolicy)
        self.gain_meter_3.setMinimumSize(QSize(0, 100))
        self.gain_meter_3.setValue(75)
        self.gain_meter_3.setTextVisible(False)
        self.gain_meter_3.setOrientation(Qt.Vertical)

        self.horizontalLayout_9.addWidget(self.gain_meter_3)


        self.verticalLayout_9.addWidget(self.volume_frame_3)

        self.mplFrame_3 = QFrame(self.centralwidget)
        self.mplFrame_3.setObjectName(u"mplFrame_3")
        self.mplFrame_3.setFrameShape(QFrame.StyledPanel)
        self.mplFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.mplFrame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pgwidget_3 = PGWidget(self.mplFrame_3)
        self.pgwidget_3.setObjectName(u"pgwidget_3")

        self.verticalLayout_3.addWidget(self.pgwidget_3)

        self.doubleslider_3 = DoubleRangeSlider(self.mplFrame_3)
        self.doubleslider_3.setObjectName(u"doubleslider_3")
        sizePolicy1.setHeightForWidth(self.doubleslider_3.sizePolicy().hasHeightForWidth())
        self.doubleslider_3.setSizePolicy(sizePolicy1)
        self.doubleslider_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.doubleslider_3)


        self.verticalLayout_9.addWidget(self.mplFrame_3)

        self.button_frame_3 = QFrame(self.centralwidget)
        self.button_frame_3.setObjectName(u"button_frame_3")
        self.button_frame_3.setFrameShape(QFrame.StyledPanel)
        self.button_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.button_frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.play_button_3 = QPushButton(self.button_frame_3)
        self.play_button_3.setObjectName(u"play_button_3")
        sizePolicy2.setHeightForWidth(self.play_button_3.sizePolicy().hasHeightForWidth())
        self.play_button_3.setSizePolicy(sizePolicy2)
        self.play_button_3.setMaximumSize(QSize(60, 40))
        self.play_button_3.setStyleSheet(u"image: url(:/play_icon.png);")

        self.horizontalLayout_3.addWidget(self.play_button_3)

        self.record_button_3 = QPushButton(self.button_frame_3)
        self.record_button_3.setObjectName(u"record_button_3")
        sizePolicy2.setHeightForWidth(self.record_button_3.sizePolicy().hasHeightForWidth())
        self.record_button_3.setSizePolicy(sizePolicy2)
        self.record_button_3.setMaximumSize(QSize(60, 40))
        self.record_button_3.setStyleSheet(u"image: url(:/record_icon.png);")

        self.horizontalLayout_3.addWidget(self.record_button_3)


        self.verticalLayout_9.addWidget(self.button_frame_3)


        self.horizontalLayout_19.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.labelFrame_4 = QFrame(self.centralwidget)
        self.labelFrame_4.setObjectName(u"labelFrame_4")
        self.labelFrame_4.setFrameShape(QFrame.StyledPanel)
        self.labelFrame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.labelFrame_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.strip_label_4 = QLabel(self.labelFrame_4)
        self.strip_label_4.setObjectName(u"strip_label_4")
        self.strip_label_4.setFont(font2)
        self.strip_label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.strip_label_4)


        self.verticalLayout_10.addWidget(self.labelFrame_4)

        self.volume_frame_4 = QFrame(self.centralwidget)
        self.volume_frame_4.setObjectName(u"volume_frame_4")
        self.volume_frame_4.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.volume_frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.gain_slider_4 = QSlider(self.volume_frame_4)
        self.gain_slider_4.setObjectName(u"gain_slider_4")
        sizePolicy.setHeightForWidth(self.gain_slider_4.sizePolicy().hasHeightForWidth())
        self.gain_slider_4.setSizePolicy(sizePolicy)
        self.gain_slider_4.setMinimumSize(QSize(0, 100))
        self.gain_slider_4.setValue(75)
        self.gain_slider_4.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.gain_slider_4)

        self.gain_meter_4 = QProgressBar(self.volume_frame_4)
        self.gain_meter_4.setObjectName(u"gain_meter_4")
        sizePolicy.setHeightForWidth(self.gain_meter_4.sizePolicy().hasHeightForWidth())
        self.gain_meter_4.setSizePolicy(sizePolicy)
        self.gain_meter_4.setMinimumSize(QSize(0, 100))
        self.gain_meter_4.setValue(75)
        self.gain_meter_4.setTextVisible(False)
        self.gain_meter_4.setOrientation(Qt.Vertical)

        self.horizontalLayout_10.addWidget(self.gain_meter_4)


        self.verticalLayout_10.addWidget(self.volume_frame_4)

        self.mplFrame_4 = QFrame(self.centralwidget)
        self.mplFrame_4.setObjectName(u"mplFrame_4")
        self.mplFrame_4.setFrameShape(QFrame.StyledPanel)
        self.mplFrame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mplFrame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pgwidget_4 = PGWidget(self.mplFrame_4)
        self.pgwidget_4.setObjectName(u"pgwidget_4")

        self.verticalLayout_4.addWidget(self.pgwidget_4)

        self.doubleslider_4 = DoubleRangeSlider(self.mplFrame_4)
        self.doubleslider_4.setObjectName(u"doubleslider_4")
        sizePolicy1.setHeightForWidth(self.doubleslider_4.sizePolicy().hasHeightForWidth())
        self.doubleslider_4.setSizePolicy(sizePolicy1)
        self.doubleslider_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.doubleslider_4)


        self.verticalLayout_10.addWidget(self.mplFrame_4)

        self.button_frame_4 = QFrame(self.centralwidget)
        self.button_frame_4.setObjectName(u"button_frame_4")
        self.button_frame_4.setFrameShape(QFrame.StyledPanel)
        self.button_frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.button_frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.play_button_4 = QPushButton(self.button_frame_4)
        self.play_button_4.setObjectName(u"play_button_4")
        sizePolicy2.setHeightForWidth(self.play_button_4.sizePolicy().hasHeightForWidth())
        self.play_button_4.setSizePolicy(sizePolicy2)
        self.play_button_4.setMaximumSize(QSize(60, 40))
        self.play_button_4.setStyleSheet(u"image: url(:/play_icon.png);")

        self.horizontalLayout_4.addWidget(self.play_button_4)

        self.record_button_4 = QPushButton(self.button_frame_4)
        self.record_button_4.setObjectName(u"record_button_4")
        sizePolicy2.setHeightForWidth(self.record_button_4.sizePolicy().hasHeightForWidth())
        self.record_button_4.setSizePolicy(sizePolicy2)
        self.record_button_4.setMaximumSize(QSize(60, 40))
        self.record_button_4.setStyleSheet(u"image: url(:/record_icon.png);")

        self.horizontalLayout_4.addWidget(self.record_button_4)


        self.verticalLayout_10.addWidget(self.button_frame_4)


        self.horizontalLayout_19.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.labelFrame_5 = QFrame(self.centralwidget)
        self.labelFrame_5.setObjectName(u"labelFrame_5")
        self.labelFrame_5.setFrameShape(QFrame.StyledPanel)
        self.labelFrame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.labelFrame_5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.strip_label_5 = QLabel(self.labelFrame_5)
        self.strip_label_5.setObjectName(u"strip_label_5")
        self.strip_label_5.setFont(font2)
        self.strip_label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.strip_label_5)


        self.verticalLayout_11.addWidget(self.labelFrame_5)

        self.volume_frame_5 = QFrame(self.centralwidget)
        self.volume_frame_5.setObjectName(u"volume_frame_5")
        self.volume_frame_5.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.volume_frame_5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.gain_slider_5 = QSlider(self.volume_frame_5)
        self.gain_slider_5.setObjectName(u"gain_slider_5")
        sizePolicy.setHeightForWidth(self.gain_slider_5.sizePolicy().hasHeightForWidth())
        self.gain_slider_5.setSizePolicy(sizePolicy)
        self.gain_slider_5.setMinimumSize(QSize(0, 100))
        self.gain_slider_5.setValue(75)
        self.gain_slider_5.setOrientation(Qt.Vertical)

        self.horizontalLayout_11.addWidget(self.gain_slider_5)

        self.gain_meter_5 = QProgressBar(self.volume_frame_5)
        self.gain_meter_5.setObjectName(u"gain_meter_5")
        sizePolicy.setHeightForWidth(self.gain_meter_5.sizePolicy().hasHeightForWidth())
        self.gain_meter_5.setSizePolicy(sizePolicy)
        self.gain_meter_5.setMinimumSize(QSize(0, 100))
        self.gain_meter_5.setValue(75)
        self.gain_meter_5.setTextVisible(False)
        self.gain_meter_5.setOrientation(Qt.Vertical)

        self.horizontalLayout_11.addWidget(self.gain_meter_5)


        self.verticalLayout_11.addWidget(self.volume_frame_5)

        self.mplFrame_5 = QFrame(self.centralwidget)
        self.mplFrame_5.setObjectName(u"mplFrame_5")
        self.mplFrame_5.setFrameShape(QFrame.StyledPanel)
        self.mplFrame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mplFrame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pgwidget_5 = PGWidget(self.mplFrame_5)
        self.pgwidget_5.setObjectName(u"pgwidget_5")

        self.verticalLayout_5.addWidget(self.pgwidget_5)

        self.doubleslider_5 = DoubleRangeSlider(self.mplFrame_5)
        self.doubleslider_5.setObjectName(u"doubleslider_5")
        sizePolicy1.setHeightForWidth(self.doubleslider_5.sizePolicy().hasHeightForWidth())
        self.doubleslider_5.setSizePolicy(sizePolicy1)
        self.doubleslider_5.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.doubleslider_5)


        self.verticalLayout_11.addWidget(self.mplFrame_5)

        self.button_frame_5 = QFrame(self.centralwidget)
        self.button_frame_5.setObjectName(u"button_frame_5")
        self.button_frame_5.setFrameShape(QFrame.StyledPanel)
        self.button_frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.button_frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.play_button_5 = QPushButton(self.button_frame_5)
        self.play_button_5.setObjectName(u"play_button_5")
        sizePolicy2.setHeightForWidth(self.play_button_5.sizePolicy().hasHeightForWidth())
        self.play_button_5.setSizePolicy(sizePolicy2)
        self.play_button_5.setMaximumSize(QSize(60, 40))
        self.play_button_5.setStyleSheet(u"image: url(:/play_icon.png);")

        self.horizontalLayout_5.addWidget(self.play_button_5)

        self.record_button_5 = QPushButton(self.button_frame_5)
        self.record_button_5.setObjectName(u"record_button_5")
        sizePolicy2.setHeightForWidth(self.record_button_5.sizePolicy().hasHeightForWidth())
        self.record_button_5.setSizePolicy(sizePolicy2)
        self.record_button_5.setMaximumSize(QSize(60, 40))
        self.record_button_5.setStyleSheet(u"image: url(:/record_icon.png);")

        self.horizontalLayout_5.addWidget(self.record_button_5)


        self.verticalLayout_11.addWidget(self.button_frame_5)


        self.horizontalLayout_19.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelFrame_6 = QFrame(self.centralwidget)
        self.labelFrame_6.setObjectName(u"labelFrame_6")
        self.labelFrame_6.setFrameShape(QFrame.StyledPanel)
        self.labelFrame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.labelFrame_6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.strip_label_6 = QLabel(self.labelFrame_6)
        self.strip_label_6.setObjectName(u"strip_label_6")
        self.strip_label_6.setFont(font2)
        self.strip_label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.strip_label_6)


        self.verticalLayout_12.addWidget(self.labelFrame_6)

        self.volume_frame_6 = QFrame(self.centralwidget)
        self.volume_frame_6.setObjectName(u"volume_frame_6")
        self.volume_frame_6.setFrameShape(QFrame.StyledPanel)
        self.volume_frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.volume_frame_6)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.gain_slider_6 = QSlider(self.volume_frame_6)
        self.gain_slider_6.setObjectName(u"gain_slider_6")
        sizePolicy.setHeightForWidth(self.gain_slider_6.sizePolicy().hasHeightForWidth())
        self.gain_slider_6.setSizePolicy(sizePolicy)
        self.gain_slider_6.setMinimumSize(QSize(0, 100))
        self.gain_slider_6.setValue(75)
        self.gain_slider_6.setOrientation(Qt.Vertical)

        self.horizontalLayout_12.addWidget(self.gain_slider_6)

        self.gain_meter_6 = QProgressBar(self.volume_frame_6)
        self.gain_meter_6.setObjectName(u"gain_meter_6")
        sizePolicy.setHeightForWidth(self.gain_meter_6.sizePolicy().hasHeightForWidth())
        self.gain_meter_6.setSizePolicy(sizePolicy)
        self.gain_meter_6.setMinimumSize(QSize(0, 100))
        self.gain_meter_6.setValue(75)
        self.gain_meter_6.setTextVisible(False)
        self.gain_meter_6.setOrientation(Qt.Vertical)

        self.horizontalLayout_12.addWidget(self.gain_meter_6)


        self.verticalLayout_12.addWidget(self.volume_frame_6)

        self.mplFrame_6 = QFrame(self.centralwidget)
        self.mplFrame_6.setObjectName(u"mplFrame_6")
        self.mplFrame_6.setFrameShape(QFrame.StyledPanel)
        self.mplFrame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.mplFrame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pgwidget_6 = PGWidget(self.mplFrame_6)
        self.pgwidget_6.setObjectName(u"pgwidget_6")

        self.verticalLayout_6.addWidget(self.pgwidget_6)

        self.doubleslider_6 = DoubleRangeSlider(self.mplFrame_6)
        self.doubleslider_6.setObjectName(u"doubleslider_6")
        sizePolicy1.setHeightForWidth(self.doubleslider_6.sizePolicy().hasHeightForWidth())
        self.doubleslider_6.setSizePolicy(sizePolicy1)
        self.doubleslider_6.setOrientation(Qt.Horizontal)

        self.verticalLayout_6.addWidget(self.doubleslider_6)


        self.verticalLayout_12.addWidget(self.mplFrame_6)

        self.button_frame_6 = QFrame(self.centralwidget)
        self.button_frame_6.setObjectName(u"button_frame_6")
        self.button_frame_6.setFrameShape(QFrame.StyledPanel)
        self.button_frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.button_frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.play_button_6 = QPushButton(self.button_frame_6)
        self.play_button_6.setObjectName(u"play_button_6")
        sizePolicy2.setHeightForWidth(self.play_button_6.sizePolicy().hasHeightForWidth())
        self.play_button_6.setSizePolicy(sizePolicy2)
        self.play_button_6.setMaximumSize(QSize(60, 40))
        self.play_button_6.setStyleSheet(u"image: url(:/play_icon.png);")

        self.horizontalLayout_6.addWidget(self.play_button_6)

        self.record_button_6 = QPushButton(self.button_frame_6)
        self.record_button_6.setObjectName(u"record_button_6")
        sizePolicy2.setHeightForWidth(self.record_button_6.sizePolicy().hasHeightForWidth())
        self.record_button_6.setSizePolicy(sizePolicy2)
        self.record_button_6.setMaximumSize(QSize(60, 40))
        self.record_button_6.setStyleSheet(u"image: url(:/record_icon.png);")

        self.horizontalLayout_6.addWidget(self.record_button_6)


        self.verticalLayout_12.addWidget(self.button_frame_6)


        self.horizontalLayout_19.addLayout(self.verticalLayout_12)


        self.verticalLayout_14.addLayout(self.horizontalLayout_19)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sequence Board", None))
        self.main_window_label.setText(QCoreApplication.translate("MainWindow", u"SequenceBoard", None))
        self.strip_label_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.play_button_1.setText("")
        self.record_button_1.setText("")
        self.strip_label_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.play_button_2.setText("")
        self.record_button_2.setText("")
        self.strip_label_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.play_button_3.setText("")
        self.record_button_3.setText("")
        self.strip_label_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.play_button_4.setText("")
        self.record_button_4.setText("")
        self.strip_label_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.play_button_5.setText("")
        self.record_button_5.setText("")
        self.strip_label_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.play_button_6.setText("")
        self.record_button_6.setText("")
    # retranslateUi

