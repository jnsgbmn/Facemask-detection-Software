from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
import sys
import time


from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from os.path import dirname, join
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import os


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





class detect_mask():
    def videosurvillance (self):
        def detect_and_predict_mask(frame, faceNet, maskNet):
            (h, w) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
                                    (104.0, 177.0, 123.0))
            faceNet.setInput(blob)
            detections = faceNet.forward()
            print(detections.shape)
            faces = []
            locs = []
            preds = []

            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.5:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    (startX, startY) = (max(0, startX), max(0, startY))
                    (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

                    face = frame[startY:endY, startX:endX]
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                    face = cv2.resize(face, (224, 224))
                    face = img_to_array(face)
                    face = preprocess_input(face)

                    faces.append(face)
                    locs.append((startX, startY, endX, endY))
            if len(faces) > 0:
                faces = np.array(faces, dtype="float32")
                preds = maskNet.predict(faces, batch_size=32)
                return (locs, preds)
        prototxtPath = r"deploy.protext"
        weightsPath = r"res10_300x300_ssd_iter_140000.caffemodel"
        faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

        maskNet = load_model("mask_detector.model")
        print("Starting the CAMERA...")
        vs = VideoStream(src=1)
        

        while True:
            frame = vs.read()
            frame = imutils.resize(frame)
            (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)
            for (box, pred) in zip(locs, preds):

                (startX, startY, endX, endY) = box
                (mask, withoutMask) = pred

                label = "With Mask" if mask > withoutMask else "No Mask"
                color = (0, 255, 0) if label == "With Mask" else (0, 0, 255)
                label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
                cv2.putText(frame, label, (startX, startY - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                cv2.rectangle(frame, (startX, startY), (endX, endY), color, 5)

    def convertFrame(self):
        try:
            height,width = self.frame.shape[:2]
            img=QtGui.QImage(self.currentFrame,
                             width,
                              height,
                             QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None



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
        self.video = VideoStream(src=0).start()





        


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


        
    
def main():
    app=QApplication(sys.argv)
    window = SplashScreen()
    window.show()
    app.exec_()

if __name__ == '__main__':
    try:
        main()
    except Exception as why:
        print(why)