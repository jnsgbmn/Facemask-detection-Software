import sys
import cv2
import numpy as np
from PyQt5 import QtGui, QtCore, Qt, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel
from PyQt5.QtWidgets import QWidget

import dlib
import face_recognition
import os
import time

faces = []
encode = []
known_faces = []
names = []
y = 0
class Video():
    def __init__(self,capture):
        global y
        self.capture = capture
        self.currentFrame=np.array([])
        for filename in os.listdir('faces/'):
            if filename.endswith('.jpg'):
                faces.append(face_recognition.load_image_file(os.path.join('faces/', filename)))
                encode.append(face_recognition.face_encodings(faces[y])[0])
                known_faces.append(encode[y])
                names.append(filename.replace('.jpg', ''))
                y += 1
                
    def captureNextFrame(self):
        """                           
        capture frame and conver it from BGR to RBG return opencv image                                      
        """ 
        ret, frame = self.capture.read()
        if(ret==True):
            self.currentFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            location = face_recognition.face_locations(self.currentFrame, number_of_times_to_upsample=1, model=0)
            encodings = face_recognition.face_encodings(self.currentFrame, location)
            name = 'Unkown'
            for encoding in encodings:
                match = face_recognition.compare_faces(known_faces, encoding, tolerance=0.9)
                distance = face_recognition.face_distance(known_faces, encoding)
                bestMatch = np.argmin(distance)
                if match[bestMatch]:
                    name = names[bestMatch]
                    print('This is '+str(name))
                    for (x, y, w, h) in (location):
                        cv2.rectangle(self.currentFrame, (h, x), (y, w), (0, 255, 0), 3)
                        cv2.rectangle(self.currentFrame, (h, w + 30), (y, w), (0, 255, 0), -1)
                        cv2.putText(self.currentFrame, name, (h, w + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
 
    def convertFrame(self):
        """     converts frame to format suitable for QtGui            """
        try:
            height,width = self.currentFrame.shape[:2]
            img=QtGui.QImage(self.currentFrame,
                              width,
                              height,
                              QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None
            
 
class MyGui(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        uic.loadUi('Window.ui', self)
        self.show()
        self.video = Video(cv2.VideoCapture(0))
        
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self.update()
 
    def play(self):
        try:
            self.video.captureNextFrame()
            self.videoFrame.setPixmap(self.video.convertFrame())
            self.videoFrame.setScaledContents(True)
        except TypeError:
            print ("No frame")

    @pyqtSlot()
    def on_ButtonBegin_clicked(self):
        self._timer.start(27)
        
    @pyqtSlot()        
    def on_ButtonStop_clicked(self):
        self._timer.stop()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyGui()
    ex.show()
    
    
