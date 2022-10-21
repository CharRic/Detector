# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/10
@ Institution: XiaMen University
@ Name: frame2video.py
@ Version 1.0
@ information: Contain a function for organizing the frames to a video.
'''

from tqdm import tqdm
import cv2
from PIL import Image
import os
import numpy as np


def frame2video(im_dir, video_dir, fps=10, start_frame=0, stop_frame=-1):
    '''
    organizing the frames to a video.
    :param im_dir:  the root of directory frame exists
    :param video_dir:  the root+name of the generated video
    :param fps: frames per second
    :param start_frame: the index of the starting frame
    :param stop_frame: the index of the ending frame
    :return: None
    '''

    im_list = os.listdir(im_dir)
    try:
        im_list.sort(key=lambda x: int(x.split('.')[0]))  # 图片顺序按序号排列
    except:  # 帧存储形式存在问题
        print("please check the rule in ./Doc/doc.txt")
        exit(-1)

    img = Image.open(os.path.join(im_dir, im_list[0]))  # 打开一张图片
    img_size = img.size  # 获得图片大小，im_dir文件夹下的图片size需要一致
    image_type = im_list[0].split('.')[-1]  # 获取图像格式
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 生成视频格式（MP4）
    videoWriter = cv2.VideoWriter(video_dir, fourcc, fps, img_size)  # 使用VideoWriter编码视频

    if stop_frame == -1:  # 结尾帧无特别要求，则全部遍历
        total_frame = len(im_list)
        for i in tqdm(im_list):
            im_name = os.path.join(im_dir, i)
            frame = cv2.imdecode(np.fromfile(im_name, dtype=np.uint8), -1)  # 编码frame解码读入
            videoWriter.write(frame)  # 帧写入视频

    else:  # 结尾帧有要求，遍历至指定帧
        total_frame = stop_frame - start_frame
        for i in tqdm(range(start_frame, stop_frame)):
            im_name = os.path.join(im_dir, str(i) + '.' + image_type)
            frame = cv2.imdecode(np.fromfile(im_name, dtype=np.uint8), -1)  # 编码frame解码读入
            videoWriter.write(frame)  # 帧写入视频
    # 释放videoWriter
    videoWriter.release()
    print('视频共' + str(total_frame / fps) + '秒')


if __name__ == '__main__':
    print("This is frame2video.py")
