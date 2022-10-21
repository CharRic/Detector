# -*- coding: utf-8 -*-
'''
@ Author : Dai Licun
@ Time: 2022/10
@ Institution: XiaMen University
@ Name: rename_.py
@ Version 1.0
@ information: Contain a function for renaming the bmps under the path; especially for the resource from "https://www.microsoft.com/en-us/download/confirmation.aspx?id=54651"
'''

import os
from tqdm import tqdm


def rename(path):
    im_list = os.listdir(path)
    for i in tqdm(range(len(im_list))):
        new_name = str(int(im_list[i][1:6])) + ".bmp"
        os.rename(os.path.join(path, im_list[i]), os.path.join(path, new_name))
    im_list = os.listdir(path)


if __name__ == '__main__':
    # rename("D:\Download\TimeOfDay")
    print("this is for rename")
