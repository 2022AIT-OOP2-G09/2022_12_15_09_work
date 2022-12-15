#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os


class Cannyscale():
    def __init__(self):
        path = './input_image'
        inputlist = os.listdir(path)

    def convert_list(self):
        for i in inputlist:
            img = cv2.imread(f'./input_image/{i}',0)
            edges = cv2.Canny(img,100,200)
            cv2.imwrite(f'./output_cannyfilter_image/{i}',edges)

class GrayScale():
    def __init__(self):
        self.path = os.listdir('./input_image')
        self.threshold = 100
        
    def convert(self):
        for each_path in self.path:
            img = cv2.imread(f'input_image/{each_path}', 0)
            print(img)
            ret, img_thresh = cv2.threshold(img, self.threshold, 255, cv2.THRESH_BINARY)
            cv2.imwrite(f'output_grayscale_image/{each_path}', img_thresh)
        
if __name__ == "__main__":
    app = GrayScale()
    app = Cannyscale()
    app.convert()
    app.convert_list()

