# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/10
@ Institution: XiaMen University
@ Name: Utils.py
@ Version 1.0
@ information: Useful functions for detector.
'''
import os
import time

import cv2
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


def get_cover(path):
    '''
    get a cover from the video
    :param path: path of the video
    :return: None
    '''
    video = cv2.VideoCapture(path)  # 读取视频文件
    success, image = video.read()  # 选取第30帧图或最后一帧作为视频封面保存。
    n = 1
    im = image
    while n < 30 and success:
        im = image
        success, image = video.read()
        n += 1
    cv2.imwrite('./icon/cover.jpg', im)


class myvideo(QVideoWidget):  # 集成重写了一个新的用于播放视频的类，供显示所选视频预览
    def __init__(self):
        super(myvideo, self).__init__()
        self.player = QMediaPlayer()

    def closeEvent(self, event):
        # 窗口退出事件响应
        reply = QtWidgets.QMessageBox.question(self, u'结束预览', u'结束视频预览?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.player.stop()  # 停止视频媒体的播放
            event.accept()  # 关闭窗口
        else:
            event.ignore()  # 忽视点击X事件

    def combine_player(self, player):
        # 与主界面的player绑定
        self.player = player


def background_detection(path, textBrower, algo="MOG2"):
    '''
    key function for detecting the background
    :param path: path of the video
    :param textBrower: information console
    :param algo: name of the algorithm
    :return: None
    '''
    root_path = os.path.split(path)[0]
    video_path = path
    # 结果视频
    video_result_path = os.path.join(root_path, "result/result.mp4")
    # 背景图
    background_path = os.path.join(root_path, "result/background.bmp")
    # 对比视频
    video_result_agg_path = os.path.join(root_path, "result/result_agg.mp4")

    # 选择算法
    if algo == "MOG2":  # 混合高斯模型
        model = cv2.createBackgroundSubtractorMOG2(1000, 16, True)
    else:
        model = cv2.createBackgroundSubtractorKNN()

    capture = cv2.VideoCapture(video_path)  # 读取视频
    frame_num = capture.get(cv2.CAP_PROP_FRAME_COUNT)  # 帧数
    fwidth = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))  # 宽度
    fhight = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高度
    videoWriter = cv2.VideoWriter(video_result_path, cv2.VideoWriter_fourcc(*'mp4v'), 15, (fwidth, fhight))  # 视频存储
    videoWriterAgg = cv2.VideoWriter(video_result_agg_path, cv2.VideoWriter_fourcc(*'mp4v'), 15,
                                     (fwidth * 3, fhight))  # 对比视频存储

    # 判断结果文件夹是否存在
    if not os.path.exists(os.path.join(root_path, "result")):
        os.mkdir(os.path.join(root_path, "result"))
    if not capture.isOpened():
        textBrower.append(time.strftime('%H:%M:%S', time.localtime(time.time())) + "\tUnable to open: " + path)
        return
    # 开始逐帧处理
    count = 0
    while True:
        ret, frame = capture.read()  # 读取帧
        if frame is None:
            break

        mask = model.apply(frame)  # 使用模型处理帧
        mask_processed = img_process(mask)  # 对得到的mask进行预处理

        mask_3D = cv2.cvtColor(mask_processed, cv2.COLOR_GRAY2RGB)  # mask转化为RGB以保存
        videoWriter.write(mask_3D)

        ret, mask_all = cv2.threshold(mask_processed, 180, 1, cv2.THRESH_BINARY)  # mask图像二值化，供后续截取目标

        frame1 = frame.copy()
        cv2.putText(frame1, str(capture.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))  # 标记帧号
        mask_ = np.reshape(mask_all, (fhight, fwidth, 1))
        videoWriterAgg.write(np.hstack((frame1, np.multiply(mask_, frame), mask_3D)))  # 获取对比图
        # testret,testmask=cv2.threshold(mask_processed,180,255,cv2.THRESH_BINARY)
        # testmask = np.reshape(testmask, (fhight, fwidth, 1))
        # cv2.imshow("test",testmask)
        # keyboard = cv2.waitKey(0)
        # if keyboard == 'q' or keyboard == 27:
        #     break
        if count % 50 == 0:  # 每隔50帧输出提示信息
            textBrower.append(
                time.strftime('%H:%M:%S', time.localtime(time.time())) + "\tprocessing:{}//{} ;".format(count,
                                                                                                        int(frame_num)))
        count = count + 1
    cv2.imencode(".bmp", model.getBackgroundImage())[1].tofile(background_path)  # 编码存储背景图
    videoWriter.release()
    videoWriterAgg.release()
    textBrower.append(time.strftime('%H:%M:%S', time.localtime(time.time())) + "\t背景图像已保存至" + background_path)


def img_process(img):
    '''
    process the mask to get a better result
    :param img:  mask
    :return: processed mask
    '''
    kernel = np.ones((7, 7), np.uint8)  # 核
    tmp = cv2.GaussianBlur(img, (7, 7), sigmaX=0)  # 高斯模糊
    tmp = cv2.dilate(tmp, kernel)  # 膨胀
    tmp = cv2.erode(tmp, kernel)  # 腐蚀

    return tmp


if __name__ == '__main__':
    print("this is Utils.py")
