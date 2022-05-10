# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QPropertyAnimation, QThread, pyqtSignal, pyqtSlot)

from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QImage)

from PyQt5.QtWidgets import *
# Splash Screen
from ui_splash_screen import Ui_SplashScreen
# Main Window
from ui_main import Ui_MainWindow

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

# Globals
counter = 0
GLOBAL_STATE = 0

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Toggle menu
        self.ui.toggle_button.clicked.connect(self.ToggleMenu)
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # Maximize Window
        self.ui.maximize_button.clicked.connect(self.maximize_restore)
        # Minimize Window
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        # Close Window
        self.ui.close_button.clicked.connect(lambda: self.close())
        # Set dropshadow window
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 200))
        # Apply dropshadow to the frame
        self.ui.frame.setGraphicsEffect(self.shadow)
        # Create size grip to resize the window
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(30, 30, 30) }")
        # Page 1
        self.ui.home_page.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page))
        # Page 2
        self.ui.recognition_page.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page_2))
        # Page 3
        self.ui.registration_page.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page_3))
        # Page 4
        self.ui.attendance_page.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page_5))
        # Page 5
        self.ui.help_page.clicked.connect(lambda: self.ui.pages.setCurrentWidget(self.ui.page_4))
        # Take photos for the dataset
        self.ui.pushButton_8.clicked.connect(self.generate_train_dataset)
        self.ui.pushButton_12.clicked.connect(self.generate_test_dataset)
        # Load csv file
        self.ui.attendance_page.clicked.connect(self.openFile)
        # Take a photo for attendance
        self.ui.pushButton_13.clicked.connect(self.take_attendance_image)
        # Train the model
        self.ui.pushButton_10.clicked.connect(self.train_model)
        # Set default of checkbox to enabled
        self.ui.checkBox.setChecked(True)
        # Set the logo to labels
        image = Image.open("NOFACE.png")
        qimage = ImageQt(image)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.ui.recognition_page_label.setPixmap(pixmap)
        self.ui.label_2.setPixmap(pixmap)

        # Move Window
        def moveWindow(event):
            # Move window if left mouse button is clicked
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
                
        self.ui.label_title.mouseMoveEvent = moveWindow
        
        # ################################## Camera on label for REGISTRATION PAGE ##################################
        # For registration page
        self.logic = 0
        self.value = 1
        self.ui.pushButton_3.clicked.connect(self.onClicked)
        
        # For recognition page
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
            else:
                print("not found")
        cap.release()
        cv2.destroyAllWindows()
    def displayImage(self,img,window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat =QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1],img.shape[0],qformat)
        img = img.rgbSwapped()
        self.ui.label_2.setPixmap(QPixmap.fromImage(img))
        self.ui.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        # ###########################################################################################################
        
        
        # ################################## Camera on label for RECOGNITION PAGE ##################################

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
        cap.release()
        cv2.destroyAllWindows()
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
        # ###########################################################################################################
        
    def generate_train_dataset(self):
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        def face_crop(img):
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            faces = face_classifier.detectMultiScale(gray,1.3,5)
            
            if faces is ():
                return None
            for (x,y,w,h) in faces:
                cropped_face = img[y:y+h, x:x+w]
            return cropped_face
        host = self.ui.lineEdit.text()
        path1 = "./dataset/Final Training Images"
        path2 = os.path.join(path1, host)
        if not os.path.exists(path2):
            os.mkdir(path2)
        else: pass
        video_capture = cv2.VideoCapture(0)
        img_id = 0
        while True:
            # Capture frame-by-frame
            ret,frame = video_capture.read()
            frame = cv2.flip(frame,1)
            if face_crop(frame) is not None:
                img_id+=1
                face = cv2.resize(face_crop(frame),(200,200))
                file_name_path = path2+"/"+host+"."+str(img_id)+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.putText(face, str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX, 2,(0,255,0),2)
    
                qformat = QImage.Format_Indexed8
                if len(face.shape) == 3:
                    if face.shape[2] == 4:
                        qformat =QImage.Format_RGBA888
                    else:
                        qformat = QImage.Format_RGB888
                face = QImage(face, face.shape[1],face.shape[0],qformat)
                face = face.rgbSwapped()
                self.ui.label_2.setPixmap(QPixmap.fromImage(face))
                self.ui.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    
            if cv2.waitKey(1)==27 or img_id == 20:
                self.onClicked()
                break
                
        cv2.destroyAllWindows()
        video_capture.release()
        
    def generate_test_dataset(self):
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        def face_crop(img):
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            faces = face_classifier.detectMultiScale(gray,1.3,5)
            
            if faces is ():
                return None
            for (x,y,w,h) in faces:
                cropped_face = img[y:y+h, x:x+w]
            return cropped_face
        host = self.ui.lineEdit.text()
        path1 = "./dataset/Final Testing Images"
        path2 = os.path.join(path1, host)
        if not os.path.exists(path2):
            os.mkdir(path2)
        else: pass
        video_capture = cv2.VideoCapture(0)
        img_id = 0
        while True:
            # Capture frame-by-frame
            ret,frame = video_capture.read()
            frame = cv2.flip(frame,1)
            if face_crop(frame) is not None:
                img_id+=1
                face = cv2.resize(face_crop(frame),(200,200))
                file_name_path = path2+"/"+host+"."+str(img_id)+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.putText(face, str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX, 2,(0,255,0),2)
    
                qformat = QImage.Format_Indexed8
                if len(face.shape) == 3:
                    if face.shape[2] == 4:
                        qformat =QImage.Format_RGBA888
                    else:
                        qformat = QImage.Format_RGB888
                face = QImage(face, face.shape[1],face.shape[0],qformat)
                face = face.rgbSwapped()
                self.ui.label_2.setPixmap(QPixmap.fromImage(face))
                self.ui.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    
            if cv2.waitKey(1)==27 or img_id == 4:
                self.onClicked()
                break
                
        cv2.destroyAllWindows()
        video_capture.release()
        
    def train_model(self):
        # Specifying the folder where images are present
        TrainingImagePath='./dataset/Final Training Images'
        
        # Defining pre-processing transformations on raw images of training data
        # These hyper parameters helps to generate slightly twisted versions
        # of the original image, which leads to a better model, since it learns
        # on the good and bad mix of images
        
        train_datagen = ImageDataGenerator(rescale=1./255,
                shear_range=0.1,
                zoom_range=0.1,
                horizontal_flip=True)
        
        # Defining pre-processing transformations on raw images of testing data
        # No transformations are done on the testing images
        test_datagen = ImageDataGenerator(rescale=1./255)
        
        # Generating the Training Data
        training_set = train_datagen.flow_from_directory(
                TrainingImagePath,
                target_size=(64, 64),
                batch_size=32,
                class_mode='categorical')
        
        # Generating the Testing Data
        test_set = test_datagen.flow_from_directory(
                TrainingImagePath,
                target_size=(64, 64),
                batch_size=32,
                class_mode='categorical')
        
        # Printing class labels for each face
        test_set.class_indices
        
        # class_indices have the numeric tag for each face
        TrainClasses=training_set.class_indices
        
        # Storing the face and the numeric tag for future reference
        ResultMap={}
        for faceValue,faceName in zip(TrainClasses.values(),TrainClasses.keys()):
            ResultMap[faceValue]= faceName
        
        # Saving the face map for future reference
        with open("ResultsMap.pkl", 'wb') as fileWriteStream:
            pickle.dump(ResultMap, fileWriteStream)
        
        # The model will give answer as a numeric tag
        # This mapping will help to get the corresponding face name for it
        print("Mapping of Face and its ID",ResultMap)
        
        # The number of neurons for the output layer is equal to the number of faces
        OutputNeurons=len(ResultMap)
        print('\n The Number of output neurons: ', OutputNeurons)
        
        '''######################## Create CNN deep learning model ########################'''
        '''Initializing the Convolutional Neural Network'''
        classifier= Sequential()
        
        ''' STEP--1 Convolution
        # Adding the first layer of CNN
        # we are using the format (64,64,3) because we are using TensorFlow backend
        # It means 3 matrix of size (64X64) pixels representing Red, Green and Blue components of pixels
        '''
        classifier.add(Convolution2D(32, kernel_size=(5, 5), strides=(1, 1), input_shape=(64,64,3), activation='relu'))
        
        '''# STEP--2 MAX Pooling'''
        classifier.add(MaxPool2D(pool_size=(2,2)))
        
        '''############## ADDITIONAL LAYER of CONVOLUTION for better accuracy #################'''
        classifier.add(Convolution2D(64, kernel_size=(5, 5), strides=(1, 1), activation='relu'))
        
        classifier.add(MaxPool2D(pool_size=(2,2)))
        
        '''# STEP--3 FLattening'''
        classifier.add(Flatten())
        
        '''# STEP--4 Fully Connected Neural Network'''
        classifier.add(Dense(64, activation='relu'))
        
        classifier.add(Dense(OutputNeurons, activation='softmax'))
        
        '''# Compiling the CNN'''
        #classifier.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        classifier.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics=["accuracy"])
        
        classifier.summary()
        
        # Measuring the time taken by the model to train
        StartTime=time.time()
        
        # Starting the model training
        classifier.fit_generator(
                            training_set,
                            steps_per_epoch=len(training_set),
                            epochs=30,
                            validation_data=test_set,
                            validation_steps=len(test_set))
        
        EndTime=time.time()
        print("###### Total Time Taken: ", round((EndTime-StartTime)/60), 'Minutes ######')
        
        # Save the model
        classifier.save('model_new')
        
    def take_attendance_image(self):
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
        def face_crop(img):
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            faces = face_classifier.detectMultiScale(gray,1.3,5)
            
            if faces is ():
                return None
            for (x,y,w,h) in faces:
                cropped_face = img[y:y+h, x:x+w]
            return cropped_face
        
        def mark_attendance(name):
            with open('Attendance.csv','r+') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])   
                if name not in nameList:
                    now = datetime.now()
                    today = datetime.today()  
                    date_today = today.strftime("%d/%m/%Y")
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'\n{name},{dtString},{date_today}')
        
        path = "Images for Attendance"
        video_capture = cv2.VideoCapture(0)
        
        images = []
        image_numbers = []
        myList = os.listdir(path)
        for img in myList:
            curImg = cv2.imread(f'{path}/{img}')
            images.append(curImg)
            image_numbers.append(os.path.splitext(img)[0])
        img_id = int(image_numbers[-1])
        
        while True:
            # Capture frame-by-frame
            ret,frame = video_capture.read()
            frame = cv2.flip(frame,1)
            if face_crop(frame) is not None:
                img_id+=1
                face = cv2.resize(face_crop(frame),(200,200))
                file_name_path = path+"/"+str(img_id)+".jpg"
                cv2.imwrite(file_name_path,face)
    
                qformat = QImage.Format_Indexed8
                if len(face.shape) == 3:
                    if face.shape[2] == 4:
                        qformat =QImage.Format_RGBA888
                    else:
                        qformat = QImage.Format_RGB888
                face = QImage(face, face.shape[1],face.shape[0],qformat)
                face = face.rgbSwapped()
                self.ui.recognition_page_label.setPixmap(QPixmap.fromImage(face))
                self.ui.recognition_page_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                
                model = keras.models.load_model('model_new')
        
                # Specifying the folder where images are present
                TrainingImagePath='./dataset/Final Training Images'
                # Defining pre-processing transformations on raw images of training data
                # These hyper parameters helps to generate slightly twisted versions
                # of the original image, which leads to a better model, since it learns
                # on the good and bad mix of images
                train_datagen = ImageDataGenerator(rescale=1./255,
                        shear_range=0.1,
                        zoom_range=0.1,
                        horizontal_flip=True)
                # Defining pre-processing transformations on raw images of testing data
                # No transformations are done on the testing images
                test_datagen = ImageDataGenerator(rescale=1./255,)
                # Generating the Training Data
                training_set = train_datagen.flow_from_directory(
                        TrainingImagePath,
                        target_size=(64, 64),
                        batch_size=32,
                        class_mode='categorical')
                # Generating the Testing Data
                test_set = test_datagen.flow_from_directory(
                        TrainingImagePath,
                        target_size=(64, 64),
                        batch_size=32,
                        class_mode='categorical')
                # Printing class labels for each face
                test_set.class_indices
                # class_indices have the numeric tag for each face
                TrainClasses=training_set.class_indices
                # Storing the face and the numeric tag for future reference
                ResultMap={}
                for faceValue,faceName in zip(TrainClasses.values(),TrainClasses.keys()):
                    ResultMap[faceValue]= faceName  
                # Prediction
                my_img_path = "Images for Attendance"
                myList2 = os.listdir(my_img_path)
                for i in myList2:
                    if img_id == int(os.path.splitext(i)[0]):
                        image_path = my_img_path+"/"+str(img_id)+".jpg"
                        break
                test_image=image.load_img(image_path,target_size=(64, 64))
                test_image=image.img_to_array(test_image)
                 
                test_image=np.expand_dims(test_image,axis=0)
                 
                result=model.predict_proba(test_image,verbose=0)
                self.ui.label_person_name.setText(ResultMap[np.argmax(result)])
                
                # time.sleep(0.1)
                if self.ui.checkBox.isChecked():
                    name = self.ui.label_person_name.text()
                    self.ui.pushButton_2.clicked.connect(lambda state, name=name: mark_attendance(name))
                else:
                    mark_attendance(self.ui.label_person_name.text())
            
            if cv2.waitKey(1)==27 or img_id > int(image_numbers[-1]):
                self.onClicked2()
                break
        
        cv2.destroyAllWindows()
        video_capture.release()
        return 
        
                             
    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()
        
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # If not max
        if status == 0:
            self.showMaximized()

            # Set global variable to 1
            GLOBAL_STATE = 1

            # If max, remove margins and border radius
            self.ui.layout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame.setStyleSheet("background-color: rgb(52, 55, 61);border-radius:0px;")
            self.ui.maximize_button.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.layout.setContentsMargins(10, 10, 10, 10)
            self.ui.frame.setStyleSheet("background-color: rgb(52, 55, 61);border-radius:10px;")
            self.ui.maximize_button.setToolTip("Maximize")

    def ToggleMenu(self):
        if True:

            # Get width
            width = self.ui.frame_left_menu.width()
            maxExtend = 200
            standard = 70

            # Set max width
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # Animation
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            
    def openFile(self):
        path = "Attendance.csv"
        self.all_data = pd.read_csv(path)
        self.ui.tableWidget.setColumnCount(len(self.all_data.columns))
        self.ui.tableWidget.setRowCount(len(self.all_data.index))
        # self.ui.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)
        for i in range(len(self.all_data.index)):
            for j in range(len(self.all_data.columns)):
                self.ui.tableWidget.setItem(i,j,QTableWidgetItem(str(self.all_data.iat[i,j])))
        
class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(SplashScreen, self).__init__()
        uic.loadUi('splash_screen.ui', self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,200))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        
        # Timer 
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(20)
        
        # Change loading text
        QtCore.QTimer.singleShot(1000, lambda: self.ui.label_loading.setText("LOADING DATABASE"))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.label_loading.setText("LOADING USER INTERFACE"))
        
        self.show()
        
    def progress(self):
        global counter
        # Set value to progress bar
        self.ui.progressBar.setValue(counter)
        
        # Close splash screen & open app
        if counter > 100:
            # Stop timer
            self.timer.stop()
            # Show main window
            self.main = MainWindow()
            self.main.show()
            # Close splash screen
            self.close()
        # Increase counter
        counter += 1

        
app = QtWidgets.QApplication(sys.argv)
window = SplashScreen()
app.exec_()