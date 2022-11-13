# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/10
@ Institution: XiaMen University
@ Name: eval.py
@ Version 1.1
@ information: Contain a function for calculating the MSE loss between a reference image and a list of result images.
'''
from skimage.metrics import mean_squared_error


def MSE_LOSS(img1=None, img2=None):
    '''

    :param img1: list of result images
    :param img2: reference image
    :return:  A list: MSE Loss between reference image and result images in a list.
    '''
    if img1 is None:
        img1 = []
    result = []

    for i in img1:
        result.append(round(mean_squared_error(i, img2), 2))  # 精确到两位小数
    return result
