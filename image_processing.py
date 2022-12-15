#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os

path = './input_image'
inputlist = os.listdir(path)

for i in inputlist:
    img = cv2.imread(inputlist[i],0)
    edges = cv2.Canny(img,100,200)
    cv2.imwrite('/output_cannyfilter_image/{inputlist[i]}',edges)
