# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(833, 731)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menuFrame = QtWidgets.QFrame(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuFrame.sizePolicy().hasHeightForWidth())
        self.menuFrame.setSizePolicy(sizePolicy)
        self.menuFrame.setMaximumSize(QtCore.QSize(338, 514))
        self.menuFrame.setStyleSheet("width:20%;\n"
"height:100%;\n"
"background-color: rgb(250, 247, 240);")
        self.menuFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.menuFrame.setObjectName("menuFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuFrame)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonHome = QtWidgets.QPushButton(self.menuFrame)
        self.pushButtonHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonHome.setStyleSheet("height:80%;\n"
"width:100%;\n"
"margin-top:30%;\n"
"background-color:rgb(221,184,146);\n"
"font-size:16pt;\n"
"font: \"黑体\";\n"
"font-weight:900;\n"
"color:rgb(51, 57, 85);")
        self.pushButtonHome.setObjectName("pushButtonHome")
        self.verticalLayout.addWidget(self.pushButtonHome)
        self.pushButtonBackground = QtWidgets.QPushButton(self.menuFrame)
        self.pushButtonBackground.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonBackground.setStyleSheet("height:80%;\n"
"width:90%;\n"
"margin-top:10%;\n"
"\n"
"background-color:rgb(221,184,146);\n"
"font-size:15pt;\n"
"font: \"黑体\";\n"
"font-weight:900;\n"
"color:rgb(51, 57, 85);")
        self.pushButtonBackground.setObjectName("pushButtonBackground")
        self.verticalLayout.addWidget(self.pushButtonBackground)
        self.pushButtonObject = QtWidgets.QPushButton(self.menuFrame)
        self.pushButtonObject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonObject.setStyleSheet("height:80%;\n"
"width:100%;\n"
"margin-top:10%;\n"
"\n"
"background-color:rgb(221,184,146);\n"
"font-size:15pt;\n"
"font: \"黑体\";\n"
"font-weight:900;\n"
"color:rgb(51, 57, 85);")
        self.pushButtonObject.setObjectName("pushButtonObject")
        self.verticalLayout.addWidget(self.pushButtonObject)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButtonExit = QtWidgets.QPushButton(self.menuFrame)
        self.pushButtonExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonExit.setStyleSheet("width:100%;\n"
"height:20%;\n"
"color: rgb(255, 142, 62);\n"
"background-color:rgb(221,184,146);\n"
"font-size:10pt;\n"
"font: \"黑体\";\n"
"font-weight:900;")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.verticalLayout.addWidget(self.pushButtonExit)
        self.horizontalLayout.addWidget(self.menuFrame)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("background-color:rgb(250, 247, 240);")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageHome = QtWidgets.QWidget()
        self.pageHome.setObjectName("pageHome")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pageHome)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelHome = QtWidgets.QLabel(self.pageHome)
        self.labelHome.setStyleSheet("font: 20pt \"黑体\";\n"
"color: rgb(89, 69, 69);\n"
"margin-top:10%")
        self.labelHome.setObjectName("labelHome")
        self.verticalLayout_7.addWidget(self.labelHome)
        self.textBrowserIntroduction = QtWidgets.QTextBrowser(self.pageHome)
        self.textBrowserIntroduction.setStyleSheet("background-color: rgb(215, 191, 157);\n"
"color:black;\n"
"margin-top:20%;\n"
"border-radius:15;")
        self.textBrowserIntroduction.setObjectName("textBrowserIntroduction")
        self.verticalLayout_7.addWidget(self.textBrowserIntroduction)
        self.widget_3 = QtWidgets.QWidget(self.pageHome)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_7.addWidget(self.widget_3)
        self.labelTail = QtWidgets.QLabel(self.pageHome)
        self.labelTail.setStyleSheet("font: 10pt \"黑体\";\n"
"color: rgb(89, 69, 69);\n"
"margin-top:10%;\n"
"text-align:right;")
        self.labelTail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTail.setOpenExternalLinks(True)
        self.labelTail.setObjectName("labelTail")
        self.verticalLayout_7.addWidget(self.labelTail)
        self.stackedWidget.addWidget(self.pageHome)
        self.pageBackground = QtWidgets.QWidget()
        self.pageBackground.setObjectName("pageBackground")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pageBackground)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelBackground = QtWidgets.QLabel(self.pageBackground)
        self.labelBackground.setStyleSheet("font-size:20pt;\n"
"margin-left:20%;\n"
"margin-top:10%;\n"
"margin-bottom:10%;\n"
"font-weight:bold;")
        self.labelBackground.setObjectName("labelBackground")
        self.verticalLayout_5.addWidget(self.labelBackground)
        self.widgetBackground = QtWidgets.QWidget(self.pageBackground)
        self.widgetBackground.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widgetBackground.setObjectName("widgetBackground")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widgetBackground)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widgetSelection = QtWidgets.QWidget(self.widgetBackground)
        self.widgetSelection.setObjectName("widgetSelection")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widgetSelection)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelBackgroundSelection = QtWidgets.QLabel(self.widgetSelection)
        self.labelBackgroundSelection.setStyleSheet("font-size:14pt;")
        self.labelBackgroundSelection.setObjectName("labelBackgroundSelection")
        self.horizontalLayout_5.addWidget(self.labelBackgroundSelection)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.pushButtonBackgroundSelection = QtWidgets.QPushButton(self.widgetSelection)
        self.pushButtonBackgroundSelection.setStyleSheet("font: 11pt \"黑体\";\n"
"background-color:rgb(221,184,146);")
        self.pushButtonBackgroundSelection.setObjectName("pushButtonBackgroundSelection")
        self.horizontalLayout_5.addWidget(self.pushButtonBackgroundSelection)
        self.verticalLayout_4.addWidget(self.widgetSelection)
        self.widget = QtWidgets.QWidget(self.widgetBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("background-color: rgb(215, 192, 174);\n"
"border:2px solid black;\n"
"margin-right:100%;\n"
"\n"
"margin-left:100%;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelBackgroundImg = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBackgroundImg.sizePolicy().hasHeightForWidth())
        self.labelBackgroundImg.setSizePolicy(sizePolicy)
        self.labelBackgroundImg.setStyleSheet("heiht:100%;\n"
"border:0;")
        self.labelBackgroundImg.setText("")
        self.labelBackgroundImg.setObjectName("labelBackgroundImg")
        self.horizontalLayout_2.addWidget(self.labelBackgroundImg)
        self.verticalLayout_4.addWidget(self.widget)
        self.verticalLayout_5.addWidget(self.widgetBackground)
        self.widgetBackgroundTail = QtWidgets.QWidget(self.pageBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetBackgroundTail.sizePolicy().hasHeightForWidth())
        self.widgetBackgroundTail.setSizePolicy(sizePolicy)
        self.widgetBackgroundTail.setObjectName("widgetBackgroundTail")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widgetBackgroundTail)
        self.horizontalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidgetBackground = QtWidgets.QTabWidget(self.widgetBackgroundTail)
        self.tabWidgetBackground.setToolTipDuration(-1)
        self.tabWidgetBackground.setStyleSheet("background-color: white;\n"
"font: 13pt \"楷体\";")
        self.tabWidgetBackground.setObjectName("tabWidgetBackground")
        self.tabBackgroundInstruction = QtWidgets.QWidget()
        self.tabBackgroundInstruction.setObjectName("tabBackgroundInstruction")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tabBackgroundInstruction)
        self.verticalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textBrowserBackgroundInstruction = QtWidgets.QTextBrowser(self.tabBackgroundInstruction)
        self.textBrowserBackgroundInstruction.setObjectName("textBrowserBackgroundInstruction")
        self.verticalLayout_11.addWidget(self.textBrowserBackgroundInstruction)
        self.tabWidgetBackground.addTab(self.tabBackgroundInstruction, "")
        self.tabBackgroundInformation = QtWidgets.QWidget()
        self.tabBackgroundInformation.setObjectName("tabBackgroundInformation")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tabBackgroundInformation)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.textBrowserBackgroundInformation = QtWidgets.QTextBrowser(self.tabBackgroundInformation)
        self.textBrowserBackgroundInformation.setObjectName("textBrowserBackgroundInformation")
        self.verticalLayout_10.addWidget(self.textBrowserBackgroundInformation)
        self.tabWidgetBackground.addTab(self.tabBackgroundInformation, "")
        self.horizontalLayout_6.addWidget(self.tabWidgetBackground)
        self.pushButtonBackgroundDetection = QtWidgets.QPushButton(self.widgetBackgroundTail)
        self.pushButtonBackgroundDetection.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonBackgroundDetection.setStyleSheet("height:100%;\n"
"width:100%;\n"
"margin-left:20%;\n"
"margin-right:20%;\n"
"border-image:url(\"./icon/right-circle.png\");\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border-radius:50%;\n"
"margin-top:20%;")
        self.pushButtonBackgroundDetection.setText("")
        self.pushButtonBackgroundDetection.setObjectName("pushButtonBackgroundDetection")
        self.horizontalLayout_6.addWidget(self.pushButtonBackgroundDetection)
        self.verticalLayout_5.addWidget(self.widgetBackgroundTail)
        self.stackedWidget.addWidget(self.pageBackground)
        self.pageObject = QtWidgets.QWidget()
        self.pageObject.setObjectName("pageObject")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageObject)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelObject = QtWidgets.QLabel(self.pageObject)
        self.labelObject.setStyleSheet("font-size:20pt;\n"
"margin-left:20%;\n"
"margin-top:10%;\n"
"margin-bottom:10%;\n"
"font-weight:bold;")
        self.labelObject.setObjectName("labelObject")
        self.verticalLayout_2.addWidget(self.labelObject)
        self.widgetObject = QtWidgets.QWidget(self.pageObject)
        self.widgetObject.setObjectName("widgetObject")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widgetObject)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgetObjectSelection = QtWidgets.QWidget(self.widgetObject)
        self.widgetObjectSelection.setObjectName("widgetObjectSelection")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widgetObjectSelection)
        self.horizontalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelObjectSelection = QtWidgets.QLabel(self.widgetObjectSelection)
        self.labelObjectSelection.setStyleSheet("font-size:14pt;")
        self.labelObjectSelection.setObjectName("labelObjectSelection")
        self.horizontalLayout_4.addWidget(self.labelObjectSelection)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButtonObjectSelection = QtWidgets.QPushButton(self.widgetObjectSelection)
        self.pushButtonObjectSelection.setStyleSheet("font: 11pt \"黑体\";\n"
"background-color:rgb(221,184,146);")
        self.pushButtonObjectSelection.setObjectName("pushButtonObjectSelection")
        self.horizontalLayout_4.addWidget(self.pushButtonObjectSelection)
        self.labelObjectSelection.raise_()
        self.pushButtonObjectSelection.raise_()
        self.verticalLayout_3.addWidget(self.widgetObjectSelection)
        self.widgetObjectVideo = QtWidgets.QWidget(self.widgetObject)
        self.widgetObjectVideo.setStyleSheet("")
        self.widgetObjectVideo.setObjectName("widgetObjectVideo")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widgetObjectVideo)
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_2 = QtWidgets.QWidget(self.widgetObjectVideo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("background-color: rgb(215, 192, 174);\n"
"border:2px solid black;\n"
"margin-right:50%;\n"
"margin-left:50%;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.labelObjectImg = QtWidgets.QLabel(self.widget_2)
        self.labelObjectImg.setStyleSheet("border:0;")
        self.labelObjectImg.setText("")
        self.labelObjectImg.setObjectName("labelObjectImg")
        self.horizontalLayout_8.addWidget(self.labelObjectImg)
        self.horizontalLayout_7.addWidget(self.widget_2)
        self.widgetObjectChoice = QtWidgets.QWidget(self.widgetObjectVideo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetObjectChoice.sizePolicy().hasHeightForWidth())
        self.widgetObjectChoice.setSizePolicy(sizePolicy)
        self.widgetObjectChoice.setStyleSheet("border:1px solid black;\n"
"font: 9pt \"新宋体\";")
        self.widgetObjectChoice.setObjectName("widgetObjectChoice")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widgetObjectChoice)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButtonObjectStatic = QtWidgets.QRadioButton(self.widgetObjectChoice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonObjectStatic.sizePolicy().hasHeightForWidth())
        self.radioButtonObjectStatic.setSizePolicy(sizePolicy)
        self.radioButtonObjectStatic.setStyleSheet("border:none;")
        self.radioButtonObjectStatic.setChecked(True)
        self.radioButtonObjectStatic.setObjectName("radioButtonObjectStatic")
        self.verticalLayout_6.addWidget(self.radioButtonObjectStatic)
        self.radioButtonObjectMove = QtWidgets.QRadioButton(self.widgetObjectChoice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonObjectMove.sizePolicy().hasHeightForWidth())
        self.radioButtonObjectMove.setSizePolicy(sizePolicy)
        self.radioButtonObjectMove.setStyleSheet("border:none;")
        self.radioButtonObjectMove.setObjectName("radioButtonObjectMove")
        self.verticalLayout_6.addWidget(self.radioButtonObjectMove)
        self.horizontalLayout_7.addWidget(self.widgetObjectChoice)
        self.verticalLayout_3.addWidget(self.widgetObjectVideo)
        self.verticalLayout_2.addWidget(self.widgetObject)
        self.widgetObjectTail = QtWidgets.QWidget(self.pageObject)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetObjectTail.sizePolicy().hasHeightForWidth())
        self.widgetObjectTail.setSizePolicy(sizePolicy)
        self.widgetObjectTail.setObjectName("widgetObjectTail")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetObjectTail)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidgetObject = QtWidgets.QTabWidget(self.widgetObjectTail)
        self.tabWidgetObject.setToolTipDuration(-1)
        self.tabWidgetObject.setStyleSheet("background-color: white;\n"
"font: 13pt \"楷体\";")
        self.tabWidgetObject.setObjectName("tabWidgetObject")
        self.tabObjectInstruction = QtWidgets.QWidget()
        self.tabObjectInstruction.setObjectName("tabObjectInstruction")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tabObjectInstruction)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textBrowserObjectInstruction = QtWidgets.QTextBrowser(self.tabObjectInstruction)
        self.textBrowserObjectInstruction.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.textBrowserObjectInstruction.setObjectName("textBrowserObjectInstruction")
        self.verticalLayout_9.addWidget(self.textBrowserObjectInstruction)
        self.tabWidgetObject.addTab(self.tabObjectInstruction, "")
        self.tabObjectInformation = QtWidgets.QWidget()
        self.tabObjectInformation.setObjectName("tabObjectInformation")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabObjectInformation)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.textBrowserObjectInformation = QtWidgets.QTextBrowser(self.tabObjectInformation)
        self.textBrowserObjectInformation.setObjectName("textBrowserObjectInformation")
        self.verticalLayout_8.addWidget(self.textBrowserObjectInformation)
        self.tabWidgetObject.addTab(self.tabObjectInformation, "")
        self.horizontalLayout_3.addWidget(self.tabWidgetObject)
        self.pushButtonObjectDetection = QtWidgets.QPushButton(self.widgetObjectTail)
        self.pushButtonObjectDetection.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonObjectDetection.setStyleSheet("height:100%;\n"
"width:100%;\n"
"margin-left:20%;\n"
"margin-right:20%;\n"
"border-image:url(\"./icon/right-circle.png\");\n"
"background-color:rgba(255, 255, 255, 0);\n"
"border-radius:50%;\n"
"margin-top:20%;")
        self.pushButtonObjectDetection.setText("")
        self.pushButtonObjectDetection.setIconSize(QtCore.QSize(10, 10))
        self.pushButtonObjectDetection.setObjectName("pushButtonObjectDetection")
        self.horizontalLayout_3.addWidget(self.pushButtonObjectDetection)
        self.verticalLayout_2.addWidget(self.widgetObjectTail)
        self.stackedWidget.addWidget(self.pageObject)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 833, 23))
        self.menuBar.setStyleSheet("")
        self.menuBar.setObjectName("menuBar")
        self.menuList = QtWidgets.QMenu(self.menuBar)
        self.menuList.setStyleSheet("")
        self.menuList.setObjectName("menuList")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAlgorithm = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/wendang.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlgorithm.setIcon(icon)
        self.actionAlgorithm.setObjectName("actionAlgorithm")
        self.actionInformation = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icon/banquan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInformation.setIcon(icon1)
        self.actionInformation.setObjectName("actionInformation")
        self.menuList.addAction(self.actionAlgorithm)
        self.menuList.addSeparator()
        self.menuList.addAction(self.actionInformation)
        self.menuBar.addAction(self.menuList.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.tabWidgetBackground.setCurrentIndex(1)
        self.tabWidgetObject.setCurrentIndex(0)
        self.pushButtonExit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detector"))
        self.pushButtonHome.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:17pt; font-weight:792; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButtonHome.setText(_translate("MainWindow", "首页"))
        self.pushButtonBackground.setText(_translate("MainWindow", "背景检测"))
        self.pushButtonObject.setText(_translate("MainWindow", "目标跟踪"))
        self.pushButtonExit.setText(_translate("MainWindow", "⚪ 退出"))
        self.labelHome.setText(_translate("MainWindow", "首页"))
        self.textBrowserIntroduction.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.textBrowserIntroduction.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.textBrowserIntroduction.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#010000;\">本系统集成了一个背景检测系统以及目标跟踪系统。</span></p></body></html>"))
        self.labelTail.setText(_translate("MainWindow", "<html><head/><body><p>本程序xxx请见<a href=\"https://github.com/CharRic/Detector/tree/main\"><span style=\" text-decoration: underline; color:#0000ff;\">网页</span></a></p></body></html>"))
        self.labelBackground.setText(_translate("MainWindow", "背景检测"))
        self.labelBackgroundSelection.setText(_translate("MainWindow", "请选择视频文件:"))
        self.pushButtonBackgroundSelection.setText(_translate("MainWindow", " 选择文件 "))
        self.tabWidgetBackground.setTabText(self.tabWidgetBackground.indexOf(self.tabBackgroundInstruction), _translate("MainWindow", "教程"))
        self.tabWidgetBackground.setTabText(self.tabWidgetBackground.indexOf(self.tabBackgroundInformation), _translate("MainWindow", "信息台"))
        self.labelObject.setText(_translate("MainWindow", "目标跟踪"))
        self.labelObjectSelection.setText(_translate("MainWindow", "请选择视频文件:"))
        self.pushButtonObjectSelection.setText(_translate("MainWindow", " 选择文件 "))
        self.radioButtonObjectStatic.setText(_translate("MainWindow", "静止摄像机"))
        self.radioButtonObjectMove.setText(_translate("MainWindow", "运动摄像机"))
        self.tabWidgetObject.setTabText(self.tabWidgetObject.indexOf(self.tabObjectInstruction), _translate("MainWindow", "教程"))
        self.tabWidgetObject.setTabText(self.tabWidgetObject.indexOf(self.tabObjectInformation), _translate("MainWindow", "信息台"))
        self.menuList.setTitle(_translate("MainWindow", "  帮助  "))
        self.actionAlgorithm.setText(_translate("MainWindow", "算法原理"))
        self.actionInformation.setText(_translate("MainWindow", "关于Detector"))

