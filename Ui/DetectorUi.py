# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/10
@ Institution: XiaMen University
@ Name: DetectorUi.py
@ Version 1.0
@ information: The detector UI. Containing the eventFunction from Ui by users.
'''

import webbrowser

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtWidgets import QMainWindow, QFileDialog

from Ui.mainwindow import Ui_MainWindow
from Utils.Utils import *


class DetectorUi(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(DetectorUi, self).__init__()
        self.setupUi(self)
        self.init()
        self.connecter()
        self.show()

    def init(self):
        # 初始化
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidgetBackground.setCurrentIndex(0)
        self.tabWidgetObject.setCurrentIndex(0)
        self.background_filename = ""
        self.object_filename = ""
        self.background_carema_mode = 0

        self.video = myvideo()
        self.player = QMediaPlayer()
        self.video.resize(540, 460)
        self.player.setVideoOutput(self.video)

    def connecter(self):
        # 前端事件触发绑定
        self.actionInformation.triggered.connect(self.information_page)
        self.actionAlgorithm.triggered.connect(self.algorithm_page)

        self.pushButtonHome.clicked.connect(self.home_Index)
        self.pushButtonBackground.clicked.connect(self.background_Index)
        self.pushButtonObject.clicked.connect(self.object_Index)

        self.radioButtonObjectMove.toggled.connect(self.caremaModeChange)

        self.pushButtonBackgroundSelection.clicked.connect(self.background_video_upload)
        self.pushButtonObjectSelection.clicked.connect(self.object_video_upload)

        self.pushButtonBackgroundDetection.clicked.connect(self.backgroundDetection)
        self.pushButtonObjectDetection.clicked.connect(self.objectDetection)

    def information_page(self):
        # 程序信息网页
        webbrowser.open("https://github.com/CharRic/Detector/blob/main/Information.txt", 1)

    def algorithm_page(self):
        # 算法原理网页
        webbrowser.open("https://github.com/CharRic/Detector/tree/main", 1)

    def home_Index(self):
        # 切换至主页
        self.stackedWidget.setCurrentIndex(0)

    def background_Index(self):
        # 切换至背景检测页面
        self.stackedWidget.setCurrentIndex(1)

    def object_Index(self):  # TODO
        # 切换物体检测页面
        self.stackedWidget.setCurrentIndex(2)

    def caremaModeChange(self):  # TODO
        # 摄像机模式切换
        self.tabWidgetObject.setCurrentIndex(1)
        if self.radioButtonObjectMove.isChecked():
            self.textBrowserObjectInformation.append(
                time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t已切换至运动摄像机")
            self.background_carema_mode = 1
        else:
            self.textBrowserObjectInformation.append(
                time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t已切换至静止摄像机")
            self.background_carema_mode = 0

    def background_video_upload(self):
        # 背景检测视频上传
        file_name = QFileDialog.getOpenFileName(self, caption="请选择文件", filter="视频文件(*MP4);")  # 弹窗显示文件
        self.tabWidgetBackground.setCurrentIndex(1)
        if file_name[1] == file_name[0] and file_name[0] == "":  # 提示未选择文件
            self.textBrowserBackgroundInformation.append(
                time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t未选择文件")
        else:  # 读取视频文件，并给出视频预览
            self.textBrowserBackgroundInformation.append(
                time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t文件" + str(
                    file_name[0].split('/')[-1]) + "已打开")
            self.display_video(file_name[0])
            get_cover(file_name[0])
            self.show_img(0)
        self.background_filename = file_name[0]

    def object_video_upload(self):  # TODO
        # 目标检测视频上传
        file_name = QFileDialog.getOpenFileName(self, caption="请选择文件", filter="视频文件(*MP4);")
        self.tabWidgetObject.setCurrentIndex(1)
        if file_name[1] == file_name[0] and file_name[0] == "":
            self.textBrowserObjectInformation.append(
                time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t未选择文件")
        else:
            self.textBrowserObjectInformation.append(
                time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t文件" + str(
                    file_name[0].split('/')[-1]) + "已打开")
            self.display_video(file_name[0])
            get_cover(file_name[0])
            self.show_img(1)
        self.object_filename = file_name[0]

    def objectDetection(self):  # TODO
        # 目标检测
        self.tabWidgetObject.setCurrentIndex(1)
        self.textBrowserObjectInformation.setText(time.strftime('%H:%M:%S', time.localtime(time.time())) + "\tstart")
        self.textBrowserObjectInformation.append(
            time.strftime('%H:%M:%S', time.localtime(time.time())) + "\tProcess finished")

    def backgroundDetection(self):
        # 背景检测
        self.tabWidgetBackground.setCurrentIndex(1)
        if self.background_filename == "":  # 未选择视频
            self.textBrowserBackgroundInformation.append(
                time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t无可检测视频.")
            return
            # 开始检测
        self.textBrowserBackgroundInformation.setText(
            time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t开始运行...")
        background_detection(self.background_filename, self.textBrowserBackgroundInformation)
        # 检测完成
        self.textBrowserBackgroundInformation.append(
            time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t处理完成！")

    def display_video(self, path):
        # 读入视频预览
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.video.combine_player(self.player)
        self.video.show()
        self.player.play()

    def show_img(self, index):
        # 视频缩略图显示
        pixmap = QPixmap("./icon/cover.jpg")
        pixmap = pixmap.scaled(368, 207)
        if index == 0:
            self.labelBackgroundImg.setPixmap(pixmap)
        else:
            self.labelObjectImg.setPixmap(pixmap)
