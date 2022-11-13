# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/11
@ Institution: XiaMen University
@ Name: tracking_tool.py
@ Version 1.1
@ information:用于目标跟踪的工具函数
'''
import math

import numpy as np


# 核 profile
def kernel_profile(x):
    if type(x) == np.ndarray:
        return np.where(x ** 2 > 1, 0, 1 - x)
    if x ** 2 > 1:
        return 0
    else:
        return 1 - x


def cal_C(roi):
    '''
    计算常量C
    :param roi: 目标区域
    :return: C，归一化权重
    '''
    (height, width, c) = roi.shape  # 目标区域格式
    x_center = np.asarray([height / 2, width / 2])  # 中心点位置
    i_j = np.zeros((height, width, 2))  # 坐标矩阵
    for i in range(height):
        for j in range(width):
            i_j[i, j] = np.asarray([i, j])
    # 归一化权重计算，加入空间位置信息
    normalized_weight = kernel_profile(np.sum(((i_j - x_center) ** 2), 2) / sum(x_center ** 2))
    # 计算C
    C = 1 / sum(sum(normalized_weight))
    return C, normalized_weight


def cal_hist(roi, normalized_weight, C, bin, channel):
    '''
    计算统计直方图
    :param roi: 目标区域
    :param normalized_weight: 归一化权重
    :param C: 常量C
    :param bin: 直方图bin
    :param channel: 输入通道数，3
    :return: 直方图，索引矩阵
    '''
    hist = np.zeros(bin ** channel)
    (height, width, c) = roi.shape
    # 索引矩阵，哈希方式存储
    hi = np.floor(np.divide(roi, 16))
    hi = hi[:, :, 0] * 256 + hi[:, :, 1] * 16 + hi[:, :, 0]
    # 统计直方图
    for i in range(height):
        for j in range(width):
            hist[int(hi[i, j])] = hist[int(hi[i, j])] + normalized_weight[i, j]
    hist = hist * C
    return hist, hi


def cal_w(hist_present, model_hist):
    '''
    计算w
    :param hist_present: 当前的直方图
    :param model_hist: 模型直方图
    :return: w
    '''
    w = np.sqrt(np.divide(model_hist, hist_present, out=np.zeros_like(hist_present), where=hist_present != 0))
    return w


def cal_y1(w, statistic_hist, i_j):
    '''
    计算y1
    :param w:w
    :param statistic_hist: 模型直方图
    :param i_j: 坐标矩阵
    :return: y1
    '''
    # 分母部分
    down_ = sum(sum(w[statistic_hist.astype(np.int)]))

    # 分子部分
    w0 = w[statistic_hist.astype(np.int)]
    w_h, w_w = w0.shape
    w0 = w0.reshape(w_h, w_w, 1)
    up_ = np.sum(np.sum(w0 * i_j, 0), 0)

    y1 = up_ / down_
    return y1


def mean_shift(frame, track_window, model_hist, normalized_weight, C, end_iteration=20, end_epsilon=1):
    '''
    均值漂移函数
    :param frame: 当前帧
    :param track_window: 上一个目标框
    :param model_hist: 模型直方图
    :param normalized_weight: 归一化权重
    :param C: 常量C
    :param end_iteration: 迭代次数上限
    :param end_epsilon: ε
    :return: 当前帧的目标框
    '''

    height, width = track_window[3], track_window[2]
    new_window = track_window.copy()
    iter = 0
    # 初始化坐标矩阵
    i_j = np.zeros((height, width, 2))
    for i in range(height):
        for j in range(width):
            i_j[i, j] = np.asarray([i - height / 2, j - width / 2])

    # 迭代次数限制
    while iter < end_iteration:
        iter = iter + 1
        # 获取目标区域
        roi = frame[int(track_window[1]):int(track_window[1] + track_window[3]),
              int(track_window[0]):int(track_window[0] + track_window[2])]
        # 计算模型直方图
        hist, statistic_hist = cal_hist(roi, normalized_weight, C, 16, 3)
        # 计算w
        w = cal_w(hist, model_hist)
        # 计算位移量
        shift_value = cal_y1(w, statistic_hist, i_j)
        # 判断下一个框所在位置有无超出边界。
        if (track_window[0] + int(shift_value[1]) + width < frame.shape[1]) and (
                track_window[1] + int(shift_value[0]) + height < frame.shape[0]):
            # 更新目标框
            new_window[0] = track_window[0] + shift_value[1]
            new_window[1] = track_window[1] + shift_value[0]
        # 结束条件判断
        if math.sqrt(np.sum(shift_value ** 2)) < end_epsilon:
            break
    new_window[0] = int(new_window[0])
    new_window[1] = int(new_window[1])
    return new_window


if __name__ == '__main__':
    print("this is tracking_tool.py")
