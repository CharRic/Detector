# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/10
@ Institution: XiaMen University
@ Name: video2frame.py
@ Version 1.1
@ information: Contain a function for generating the frames from a video.
'''
import cv2
from tqdm import tqdm


def video2frame(videos_path, frames_path, gap=1, type='.bmp', start_time=0, end_time=-1):
    '''
    generating the frames from a video.
    :param videos_path: the root of the video
    :param frames_path: the root of directory for saving the frames
    :param gap: gap between saving two frames
    :param type: type of saved frame
    :param start_time: the index of the starting frame
    :param end_time: the index of the ending frame
    :return: None
    '''
    vidcap = cv2.VideoCapture(videos_path)  # 使用VideoCapture读取视频
    frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)  # 获取总帧数
    rate = vidcap.get(cv2.CAP_PROP_FPS)  # 获取帧率
    if end_time == -1:  # 结尾帧无特别要求，则全部遍历
        print('该视频每秒' + str(int(rate)) + '帧', '一共' + str(int(frames)) + '帧')
        print('本次输出' + str(int(frames) // gap) + '帧')

        for i in tqdm(range(int(frames))):
            ret, image = vidcap.read()
            if ret is False:
                break
            if i % gap == 0:  # 每隔gap张图输出一次
                cv2.imencode(type, image)[1].tofile(frames_path + "\\%d.bmp" % (i / gap))
    else:  # 结尾帧有要求，遍历至指定帧
        segment = [int(rate * start_time), int(rate * end_time)]
        print('该视频每秒' + str(int(rate)) + '帧', '一共' + str(int(frames)) + '帧')
        print('本次输出' + str((segment[1] - segment[0]) // gap) + '帧')

        for i in tqdm(range(segment[0], segment[1])):
            if i < segment[0]:
                continue
            elif i > segment[1]:
                break
            _, image = vidcap.read()
            if i % gap == 0:  # 每隔gap张图输出一次
                cv2.imencode(type, image)[1].tofile(frames_path + "\\%d.bmp" % (i / gap))


if __name__ == '__main__':
    video2frame("../testdata/WavingTrees.mp4",r"C:\Users\86137\Desktop\sa",1)
    print("This is frame2video.py")
