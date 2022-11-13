# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/11
@ Institution: XiaMen University
@ Name: tools.py
@ Version 1.1
@ information: 用于获取用户框的工具函数
'''
import cv2
from PyQt5 import QtWidgets


def draw_rectangle(x_start,y_start,x_end,y_end,img):
    '''
    画矩阵
    :param x_start: 左上角坐标的x
    :param y_start: 左上角坐标的y
    :param x_end: 右下角坐标的x
    :param y_end: 右下角坐标的y
    :param img: 图片
    :return: None
    '''
    cv2.rectangle(img,(x_start,y_start),(x_end,y_end),255,2)

# 鼠标响应
def mouse_callback(event, x, y, flags,data):
    global rec_frame, f0, drawing, x_start, y_start, x_end, y_end
    #左键按下
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_start, y_start = x, y
    #鼠标拖动
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing:
            rec_frame=f0.copy()# 实时显示矩形框
            draw_rectangle(x_start,y_start,x,y,rec_frame)
    # 左键松开
    elif event==cv2.EVENT_LBUTTONUP:
        x_end,y_end=x,y
        if drawing:
            rec_frame=f0.copy()
            draw_rectangle(x_start,y_start,x_end,y_end,rec_frame)

def initialize_video(video_path,parent):
    '''
    获取目标框，视频初始化
    :param video_path: 视频路径
    :param parent: 所在界面对象
    :return:  目标框，X，Y，W，H
    '''
    annot = QtWidgets.QMessageBox.information(parent, u'提示', u'请在图中框选目标区域，按回车确定。') # 提示信息
    global x_start,y_start,x_end,y_end,f0,rec_frame
    capture=cv2.VideoCapture(video_path)
    fwidth = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))  # 宽度
    fhight = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高度

    cv2.namedWindow('Annotation', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Annotation',fwidth,fhight)

    # 获取第一帧
    ret, f0 = capture.read()
    rec_frame = f0.copy()


    cv2.setMouseCallback('Annotation', mouse_callback)
    while True:
        # 用户绘图，回车结束
        cv2.imshow("Annotation", rec_frame)
        keyboard = cv2.waitKey(1) & 0xFF
        if keyboard == 13: break

    # 记录用户绘制的矩形框位置
    x_min, y_min, x_max, y_max = min(x_start,x_end), min(y_start, y_end), max(x_start, x_end), max(y_start, y_end)

    X=x_min
    Y=y_min
    w=x_max-x_min
    h=y_max-y_min
    cv2.destroyAllWindows()
    # 记录绘制结果
    cv2.imwrite('./icon/cover1.jpg',rec_frame)
    return [X,Y,w,h]




if __name__ == '__main__':
    print("this is tools.py")
