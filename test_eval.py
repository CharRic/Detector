# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/10
@ Institution: XiaMen University
@ Name: test_new.py
@ Version 1.1
@ information: To evaluate the outcome
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

from tools.eval import MSE_LOSS


def process0(mask):
    # 单阈值
    ret, fgMask = cv2.threshold(mask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process1(mask):
    # 阈值+3x3高斯核
    fgMask = cv2.GaussianBlur(mask, (3, 3), sigmaX=0)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process2(mask):
    # 阈值+5x5高斯核
    fgMask = cv2.GaussianBlur(mask, (5, 5), sigmaX=0)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process3(mask):
    # 阈值+7x7高斯核
    fgMask = cv2.GaussianBlur(mask, (7, 7), sigmaX=0)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process4(mask):
    # 阈值+9x9高斯核
    fgMask = cv2.GaussianBlur(mask, (9, 9), sigmaX=0)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process5(mask):
    # 阈值+9x9高斯核+3x3膨胀、腐蚀
    fgMask = cv2.GaussianBlur(mask, (9, 9), sigmaX=0)
    kernel = np.ones((3, 3), np.uint8)
    fgMask = cv2.dilate(fgMask, kernel)
    fgMask = cv2.erode(fgMask, kernel)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process6(mask):
    # 阈值+7x7高斯核+3x3膨胀、腐蚀
    fgMask = cv2.GaussianBlur(mask, (7, 7), sigmaX=0)
    kernel = np.ones((3, 3), np.uint8)
    fgMask = cv2.dilate(fgMask, kernel)
    fgMask = cv2.erode(fgMask, kernel)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process7(mask):
    # 阈值+9x9高斯核+5x5膨胀、腐蚀
    fgMask = cv2.GaussianBlur(mask, (9, 9), sigmaX=0)
    kernel = np.ones((5, 5), np.uint8)
    fgMask = cv2.dilate(fgMask, kernel)
    fgMask = cv2.erode(fgMask, kernel)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process8(mask):
    # 阈值+7x7高斯核+5x5膨胀、腐蚀
    fgMask = cv2.GaussianBlur(mask, (7, 7), sigmaX=0)
    kernel = np.ones((5, 5), np.uint8)
    fgMask = cv2.dilate(fgMask, kernel)
    fgMask = cv2.erode(fgMask, kernel)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process9(mask):
    # 阈值+7x7高斯核+7x7膨胀、腐蚀
    fgMask = cv2.GaussianBlur(mask, (7, 7), sigmaX=0)
    kernel = np.ones((7, 7), np.uint8)
    fgMask = cv2.dilate(fgMask, kernel)
    fgMask = cv2.erode(fgMask, kernel)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def process10(mask):
    # 阈值+7x7高斯核+9x9膨胀、腐蚀
    fgMask = cv2.GaussianBlur(mask, (7, 7), sigmaX=0)
    kernel = np.ones((9, 9), np.uint8)
    fgMask = cv2.dilate(fgMask, kernel)
    fgMask = cv2.erode(fgMask, kernel)
    ret, fgMask = cv2.threshold(fgMask, 178, 255, cv2.THRESH_BINARY)
    return fgMask


def visualization(vals, keys):
    # 条形图显示结果。
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams['font.size'] = 13
    plt.figure(figsize=(20, 10))  # 设置图大小

    x = keys
    y = vals

    plt.barh(x, y, height=0.5, left=0, align='center', edgecolor='r', linewidth=1)
    for index, y_value in enumerate(y):
        plt.text(y_value + 10, index - 0.2, "%s" % y_value)

    plt.title("Processing", size=26)
    plt.xlabel("MSE Loss", size=20)
    plt.ylabel("所用操作", size=20)

    plt.show()


input = "./testdata/WavingTrees.mp4"  # 视频地址
algo = 'MOG2'
ref = cv2.imread("./testdata/metric/WavingTrees/hand_segmented_00247.BMP")
index = 247
capture = cv2.VideoCapture(input)
framewidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)  # 宽度
framehight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高度
frames_num = capture.get(cv2.CAP_PROP_FRAME_COUNT)  # 帧数

if index > frames_num:  # 对比帧位置超过视频帧数
    print("wrong index")
    exit(0)

if algo == 'MOG2':  # 所用算法
    backSub = cv2.createBackgroundSubtractorMOG2(1000, 16, True)
else:
    backSub = cv2.createBackgroundSubtractorKNN()

if not capture.isOpened():  # 无法打开参考图
    print('Unable to open: ' + input)
    exit(0)
if ref is None:
    print("Could not read the reference.")
    exit(0)

count = 0
det = None
while True:  # 读取帧并检测背景前景
    ret, frame = capture.read()
    if frame is None:
        break
    m = backSub.apply(frame)

    if count == index:
        det = m.copy()

    count = count + 1
# 可视化准备
masks = []
label = ["阈值+高斯3", "阈值+高斯5", "阈值+高斯7", "阈值+高斯9", "阈值+高斯9+3腐蚀膨胀", "阈值+高斯7+3腐蚀膨胀",
         "阈值+高斯9+5腐蚀膨胀", "阈值+高斯7+5腐蚀膨胀", "阈值+高斯7+7腐蚀膨胀", "阈值+高斯7+9腐蚀膨胀"]
# masks.append(process0(det))
masks.append(process1(det))
masks.append(process2(det))
masks.append(process3(det))
masks.append(process4(det))
masks.append(process5(det))
masks.append(process6(det))
masks.append(process7(det))
masks.append(process8(det))
masks.append(process9(det))
masks.append(process10(det))

result = MSE_LOSS(masks, cv2.cvtColor(ref, cv2.COLOR_RGB2GRAY))
visualization(list(reversed(result)), list(reversed(label)))
