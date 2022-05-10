# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 716)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(0)
        self.layout.setObjectName("layout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(52, 55, 61);\n"
"border-radius:10px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_frame = QtWidgets.QFrame(self.frame)
        self.title_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_frame.setStyleSheet("background-color:none;")
        self.title_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title_text_frame = QtWidgets.QFrame(self.title_frame)
        self.title_text_frame.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.title_text_frame.setFont(font)
        self.title_text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_text_frame.setObjectName("title_text_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.title_text_frame)
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.title_text_frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setToolTip("")
        self.label_title.setStyleSheet("color: rgb(120, 120, 175);")
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.horizontalLayout.addWidget(self.title_text_frame)
        self.buttons_frame = QtWidgets.QFrame(self.title_frame)
        self.buttons_frame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_frame.setObjectName("buttons_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.minimize_button = QtWidgets.QPushButton(self.buttons_frame)
        self.minimize_button.setMinimumSize(QtCore.QSize(16, 16))
        self.minimize_button.setMaximumSize(QtCore.QSize(17, 17))
        self.minimize_button.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:8px;\n"
"    background-color: rgb(85, 255, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(85,255,0,150);\n"
"}")
        self.minimize_button.setText("")
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_5.addWidget(self.minimize_button)
        self.maximize_button = QtWidgets.QPushButton(self.buttons_frame)
        self.maximize_button.setMinimumSize(QtCore.QSize(16, 16))
        self.maximize_button.setMaximumSize(QtCore.QSize(17, 17))
        self.maximize_button.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:8px;\n"
"    \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.maximize_button.setText("")
        self.maximize_button.setObjectName("maximize_button")
        self.horizontalLayout_5.addWidget(self.maximize_button)
        self.close_button = QtWidgets.QPushButton(self.buttons_frame)
        self.close_button.setMinimumSize(QtCore.QSize(16, 16))
        self.close_button.setMaximumSize(QtCore.QSize(17, 17))
        self.close_button.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    border-radius:8px;\n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.close_button.setText("")
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_5.addWidget(self.close_button)
        self.horizontalLayout.addWidget(self.buttons_frame)
        self.verticalLayout.addWidget(self.title_frame)
        self.main_frame = QtWidgets.QFrame(self.frame)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_top_bar = QtWidgets.QFrame(self.main_frame)
        self.frame_top_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_top_bar.setStyleSheet("background-color: rgb(43, 44, 50);")
        self.frame_top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_bar.setObjectName("frame_top_bar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_top_bar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_toggle = QtWidgets.QFrame(self.frame_top_bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(254, 121, 199);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toggle_button = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_button.sizePolicy().hasHeightForWidth())
        self.toggle_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.toggle_button.setFont(font)
        self.toggle_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggle_button.setToolTipDuration(-1)
        self.toggle_button.setStatusTip("")
        self.toggle_button.setWhatsThis("")
        self.toggle_button.setStyleSheet("border: 0px solid;")
        self.toggle_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/İndirilenler/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toggle_button.setIcon(icon)
        self.toggle_button.setIconSize(QtCore.QSize(24, 24))
        self.toggle_button.setObjectName("toggle_button")
        self.verticalLayout_5.addWidget(self.toggle_button)
        self.horizontalLayout_3.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.frame_top_bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3.addWidget(self.frame_top)
        self.verticalLayout_4.addWidget(self.frame_top_bar)
        self.frame_content = QtWidgets.QFrame(self.main_frame)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_content)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_left_menu = QtWidgets.QFrame(self.frame_content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(43, 44, 50);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.home_page = QtWidgets.QPushButton(self.frame_top_menus)
        self.home_page.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.home_page.setFont(font)
        self.home_page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_page.setToolTipDuration(-4)
        self.home_page.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.home_page.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/İndirilenler/home (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_page.setIcon(icon1)
        self.home_page.setIconSize(QtCore.QSize(28, 28))
        self.home_page.setObjectName("home_page")
        self.verticalLayout_7.addWidget(self.home_page)
        self.recognition_page = QtWidgets.QPushButton(self.frame_top_menus)
        self.recognition_page.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.recognition_page.setFont(font)
        self.recognition_page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recognition_page.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.recognition_page.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/İndirilenler/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recognition_page.setIcon(icon2)
        self.recognition_page.setIconSize(QtCore.QSize(28, 28))
        self.recognition_page.setObjectName("recognition_page")
        self.verticalLayout_7.addWidget(self.recognition_page)
        self.registration_page = QtWidgets.QPushButton(self.frame_top_menus)
        self.registration_page.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.registration_page.setFont(font)
        self.registration_page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registration_page.setMouseTracking(False)
        self.registration_page.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.registration_page.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.registration_page.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:/İndirilenler/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.registration_page.setIcon(icon3)
        self.registration_page.setIconSize(QtCore.QSize(28, 28))
        self.registration_page.setObjectName("registration_page")
        self.verticalLayout_7.addWidget(self.registration_page)
        self.attendance_page = QtWidgets.QPushButton(self.frame_top_menus)
        self.attendance_page.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.attendance_page.setFont(font)
        self.attendance_page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.attendance_page.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.attendance_page.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:/İndirilenler/list (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.attendance_page.setIcon(icon4)
        self.attendance_page.setIconSize(QtCore.QSize(28, 28))
        self.attendance_page.setObjectName("attendance_page")
        self.verticalLayout_7.addWidget(self.attendance_page)
        self.help_page = QtWidgets.QPushButton(self.frame_top_menus)
        self.help_page.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.help_page.setFont(font)
        self.help_page.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help_page.setToolTipDuration(-4)
        self.help_page.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.help_page.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("D:/İndirilenler/question-mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_page.setIcon(icon5)
        self.help_page.setIconSize(QtCore.QSize(28, 28))
        self.help_page.setObjectName("help_page")
        self.verticalLayout_7.addWidget(self.help_page)
        self.verticalLayout_6.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_4.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.frame_content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pages = QtWidgets.QStackedWidget(self.frame_pages)
        self.pages.setObjectName("pages")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_9 = QtWidgets.QFrame(self.page)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_15 = QtWidgets.QFrame(self.frame_13)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_10.addWidget(self.frame_15)
        self.pushButton = QtWidgets.QPushButton(self.frame_13)
        self.pushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("D:/İndirilenler/NOFACE _transparent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QtCore.QSize(256, 256))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_10.addWidget(self.pushButton)
        self.frame_16 = QtWidgets.QFrame(self.frame_13)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_10.addWidget(self.frame_16)
        self.verticalLayout_16.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_9)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_14)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_11.addWidget(self.textBrowser_2)
        self.verticalLayout_16.addWidget(self.frame_14)
        self.verticalLayout_9.addWidget(self.frame_9)
        self.pages.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.recognition_page_label = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.recognition_page_label.setFont(font)
        self.recognition_page_label.setText("")
        self.recognition_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.recognition_page_label.setObjectName("recognition_page_label")
        self.verticalLayout_10.addWidget(self.recognition_page_label)
        self.frame_2 = QtWidgets.QFrame(self.page_2)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.open_cam = QtWidgets.QPushButton(self.frame_3)
        self.open_cam.setMinimumSize(QtCore.QSize(0, 40))
        self.open_cam.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.open_cam.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.open_cam.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("D:/İndirilenler/photo-camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_cam.setIcon(icon7)
        self.open_cam.setIconSize(QtCore.QSize(32, 32))
        self.open_cam.setObjectName("open_cam")
        self.horizontalLayout_6.addWidget(self.open_cam)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_13.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("D:/İndirilenler/take-a-picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon8)
        self.pushButton_13.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_6.addWidget(self.pushButton_13)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_11.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("D:/İndirilenler/no-pictures.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon9)
        self.pushButton_11.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_6.addWidget(self.pushButton_11)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("D:/İndirilenler/tick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon10)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.frame_17 = QtWidgets.QFrame(self.frame_3)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox = QtWidgets.QCheckBox(self.frame_17)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setStyleSheet("color: rgb(120, 120, 175);")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_12.addWidget(self.checkBox)
        self.horizontalLayout_6.addWidget(self.frame_17)
        self.verticalLayout_11.addWidget(self.frame_3)
        self.label_person_name = QtWidgets.QLabel(self.frame_2)
        self.label_person_name.setMinimumSize(QtCore.QSize(0, 35))
        self.label_person_name.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_person_name.setFont(font)
        self.label_person_name.setStyleSheet("color: rgb(120, 120, 175);\n"
"background-color: rgb(43, 44, 50);")
        self.label_person_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_person_name.setObjectName("label_person_name")
        self.verticalLayout_11.addWidget(self.label_person_name)
        self.verticalLayout_10.addWidget(self.frame_2)
        self.pages.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_13.addWidget(self.label_2)
        self.frame_6 = QtWidgets.QFrame(self.page_3)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7.addWidget(self.frame_11)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon8)
        self.pushButton_8.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_7.addWidget(self.pushButton_8)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon8)
        self.pushButton_12.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_7.addWidget(self.pushButton_12)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon9)
        self.pushButton_9.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_7.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_10.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("D:/İndirilenler/deep-learning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon11)
        self.pushButton_10.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10)
        self.frame_12 = QtWidgets.QFrame(self.frame_10)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7.addWidget(self.frame_12)
        self.verticalLayout_14.addWidget(self.frame_10)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color: rgb(43, 44, 50);\n"
"color: rgb(120, 120, 175);\n"
"}\n"
"QLineEdit:hover{\n"
"background-color: rgb(120, 120, 175);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_14.addWidget(self.lineEdit)
        self.verticalLayout_13.addWidget(self.frame_6)
        self.pages.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_8 = QtWidgets.QFrame(self.page_4)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_8)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_9.addWidget(self.textBrowser)
        self.verticalLayout_15.addWidget(self.frame_8)
        self.pages.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_7 = QtWidgets.QFrame(self.page_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color: rgb(120, 120, 175);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(150)
        self.horizontalLayout_8.addWidget(self.tableWidget)
        self.verticalLayout_12.addWidget(self.frame_7)
        self.pages.addWidget(self.page_5)
        self.verticalLayout_8.addWidget(self.pages)
        self.horizontalLayout_4.addWidget(self.frame_pages)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.verticalLayout.addWidget(self.main_frame)
        self.credits_frame = QtWidgets.QFrame(self.frame)
        self.credits_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credits_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.credits_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credits_frame.setObjectName("credits_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.credits_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_label_credits = QtWidgets.QFrame(self.credits_frame)
        self.frame_label_credits.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_credits.setObjectName("frame_label_credits")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_credits = QtWidgets.QLabel(self.frame_label_credits)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(120, 120, 175);")
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_3.addWidget(self.label_credits)
        self.horizontalLayout_2.addWidget(self.frame_label_credits)
        self.frame_grip = QtWidgets.QFrame(self.credits_frame)
        self.frame_grip.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_grip.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_grip.setCursor(QtGui.QCursor(QtCore.Qt.SizeFDiagCursor))
        self.frame_grip.setToolTip("")
        self.frame_grip.setStyleSheet("padding:5px;\n"
"background-color: rgb(43, 44, 50);")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontalLayout_2.addWidget(self.frame_grip)
        self.verticalLayout.addWidget(self.credits_frame)
        self.layout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "<strong>NO </strong>FACE"))
        self.minimize_button.setToolTip(_translate("MainWindow", "Minimize"))
        self.maximize_button.setToolTip(_translate("MainWindow", "Maximize"))
        self.close_button.setToolTip(_translate("MainWindow", "Close"))
        self.toggle_button.setToolTip(_translate("MainWindow", "Menu"))
        self.home_page.setToolTip(_translate("MainWindow", "Home"))
        self.recognition_page.setToolTip(_translate("MainWindow", "Recognition"))
        self.registration_page.setToolTip(_translate("MainWindow", "Registration"))
        self.attendance_page.setToolTip(_translate("MainWindow", "Attendance"))
        self.help_page.setToolTip(_translate("MainWindow", "Help"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600; color:#7878af;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#7878af;\">WELCOME </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#7878af;\">TO </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#7878af;\">NOFACE</span></p></body></html>"))
        self.open_cam.setToolTip(_translate("MainWindow", "Camera On"))
        self.pushButton_13.setToolTip(_translate("MainWindow", "Take a Photo for Attendance"))
        self.pushButton_11.setToolTip(_translate("MainWindow", "Camera Off"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Confirm"))
        self.checkBox.setText(_translate("MainWindow", "   Manuel Control"))
        self.label_person_name.setText(_translate("MainWindow", "Name of the Person"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Camera On"))
        self.pushButton_8.setToolTip(_translate("MainWindow", "Take Photos for Train Set"))
        self.pushButton_12.setToolTip(_translate("MainWindow", "Take Photos for Test Set"))
        self.pushButton_9.setToolTip(_translate("MainWindow", "Camera Off"))
        self.pushButton_10.setToolTip(_translate("MainWindow", "Train The Model"))
        self.lineEdit.setText(_translate("MainWindow", "Enter A New Person Here"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#7878af;\">If you have issues or question marks in your head about how this program works, you\'re in the right place. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#7878af;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#7878af;\">Please read carefully and go step by step on the process.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#7878af;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#7878af;\">On the left, you see the menu of the application. The pink buttons take you to the page you want. When you have the cursor on these buttons, the name of the related page will occur next to the cursor. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#7878af;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#7878af;\">To start using the application, follow these steps :</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; text-decoration: underline; color:#7878af;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#7878af;\">* First, click on the </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Registration Page</span><span style=\" font-size:10pt; font-weight:600; color:#7878af;\"> </span><span style=\" font-size:10pt; color:#7878af;\">to add new people to the application whom the attendance will be taken of. On this page, click on </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Camera On</span><span style=\" font-size:10pt; color:#7878af;\"> button to turn the camera on. Then enter the name of the person below. Click on the </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Take Photos for Train Set </span><span style=\" font-size:10pt; color:#7878af;\">button and it\'ll take 20 photos of the person. The person should stay still and the face should be seen clearly. Then after the camera turns on automatically, click on the </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Take Photos for Test Set </span><span style=\" font-size:10pt; color:#7878af;\">button and let it take 4 photos of the person. Repeat this process for each person and when all people are added, just click on the </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Train The Model </span><span style=\" font-size:10pt; color:#7878af;\">button and wait for the process to be done. In this step, it\'s normal for the GUI to freeze until the model is trained, so don\'t worry, stay calm and wait. Now you\'re ready to go to the next step.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#7878af;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#7878af;\">* Click on the </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Recognition Page</span><span style=\" font-size:10pt; font-weight:600; color:#7878af;\"> </span><span style=\" font-size:10pt; color:#7878af;\">and turn the camera on. Then click on the </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Take a Photo for Attendance </span><span style=\" font-size:10pt; color:#7878af;\">button. The CNN model will predict the name of the person and it\'ll appear on the text section below. If the  </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Manuel Control</span><span style=\" font-size:10pt; font-weight:600; color:#7878af;\"> </span><span style=\" font-size:10pt; color:#7878af;\">checkbox is enabled, click on the </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Confirm </span><span style=\" font-size:10pt; color:#7878af;\">button and the name will be added into the attendance list. If the </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Confirm </span><span style=\" font-size:10pt; color:#7878af;\">button is not enabled, there\'s no need to confirm the name, thus it\'ll be automatically added to the attendance list whenever the face is recognized.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; color:#7878af;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#7878af;\">* Click on the </span><span style=\" font-size:10pt; font-weight:600; color:#fe79c7;\">Attendance Page</span><span style=\" font-size:10pt; font-weight:600; color:#7878af;\"> </span><span style=\" font-size:10pt; color:#7878af;\">and here you can see the attendance list with names, time and date details.</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Date"))
        self.label_credits.setToolTip(_translate("MainWindow", "Made By EEE Sertaç Ege Türkmen"))
        self.label_credits.setText(_translate("MainWindow", "By <strong>SEGET <strong>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

