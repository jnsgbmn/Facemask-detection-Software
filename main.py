from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QPropertyAnimation, QThread, pyqtSignal, pyqtSlot)

from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QImage)


from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType




import sys
import cv2
import numpy as np
import os
import pandas as pd
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import pickle
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dense
import time
from datetime import datetime
from PIL.ImageQt import ImageQt
from PIL import Image

counter = 0
GLOBAL_STATE = 0


class ThreadProgress(QThread):
    mysignal = pyqtSignal(int)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
    def run(self):
        i = 0
        while i<101:
            time.sleep(0.1)
            self.mysignal.emit(i)
            i += 1

FROM_SPLASH,_ = loadUiType(os.path.join(os.path.dirname(__file__),"Mainwin.ui"))
FROM_Main,_ = loadUiType(os.path.join(os.path.dirname(__file__),"Fcamera.ui"))







class MainWindow(QMainWindow, FROM_Main):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  
        self.setupUi(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.ui = FROM_Main()
        self.ui.setupUi(self)
        self.ui.btnhome.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        self.ui.btnuser.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.user))
        self.ui.btnrecog.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.recog))
        self.ui.btndatabes.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Database))


        self.logic = 0
        self.value = 1
        self.ui.btncam.clicked.connect(self.onClicked)

        self.logic2 = 0
        self.value2 = 1
        self.ui.btncam1.clicked.connect(self.onClicked2)

    @pyqtSlot()
    def onClicked(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret,frame = cap.read()
            frame = cv2.flip(frame,1)
            if ret == True:
                self.displayImage(frame,1)
                cv2.waitKey()
                if self.logic == 2 :
                    self.value = self.value +1
                    cv2.imwrite()
                    self.logic = 1

    def displayImage(self,img,window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat =QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1],img.shape[0],qformat)
        img = img.rgbSwapped()
        self.ui.videoFrame.setPixmap(QPixmap.fromImage(img))
        self.ui.videoFrame.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    @pyqtSlot()
    def onClicked2(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret,frame = cap.read()
            frame = cv2.flip(frame,1)
            if ret == True:
                self.displayImage2(frame,1)
                cv2.waitKey()
                if self.logic2 == 2 :
                    self.value2 = self.value2 +1
                    cv2.imwrite()
                    self.logic2 = 1
            else:
                print("not found")

    def displayImage2(self,img,window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat =QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1],img.shape[0],qformat)
        img = img.rgbSwapped()
        self.ui.recognition_page_label.setPixmap(QPixmap.fromImage(img))
        self.ui.recognition_page_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    


class SplashScreen(QMainWindow, FROM_SPLASH):
    def __init__(self, parent = None):
        super(SplashScreen, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  
        self.setupUi(self)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft()) 
        self.show()
        progress = ThreadProgress(self)
        progress.mysignal.connect(self.progress)
        progress.start()

    @pyqtSlot(int)
    def progress(self, i):
        self.progressBar.setValue(i)
        if i == 100:
            self.hide()
            main = MainWindow(self)
            main.show()


        
    
app = QtWidgets.QApplication(sys.argv)
window = SplashScreen()
app.exec_()