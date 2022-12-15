#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os


def Cannydef():
    path = './input_image'
    inputlist = os.listdir(path)

    for i in inputlist:
        img = cv2.imread(f'./input_image/{i}',0)
        edges = cv2.Canny(img,100,200)
        cv2.imwrite(f'./output_cannyfilter_image/{i}',edges)