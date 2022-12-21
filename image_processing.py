#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.utils import secure_filename
from watchdog.events import FileSystemEventHandler
import cv2
import numpy as np
import os


class Cannyclass():
    def __init__(self):
        self.path = os.listdir('./static/input_image')

    def convert_canny(self):
        for each_path in self.path:
            img = cv2.imread(f'./static/input_image/{each_path}',0)
            edges = cv2.Canny(img,100,200)
            cv2.imwrite(f'./static/output_cannyfilter_image/{each_path}',edges)

class GrayScale():
    def __init__(self):
        self.path = os.listdir('./static/input_image')
        self.threshold = 100
        
    def convert(self):
        for each_path in self.path:
            img = cv2.imread(f'./static/input_image/{each_path}', 0)
            print(img)
            ret, img_thresh = cv2.threshold(img, self.threshold, 255, cv2.THRESH_BINARY)
            cv2.imwrite(f'./static/output_grayscale_image/{each_path}', img_thresh)

class ChangeHandler(FileSystemEventHandler):
    # すべてのイベント
    def on_any_event(self, event):
        app = GrayScale()
        app.convert()
        app = Cannyclass()
        app.convert_canny()
        print("aaaaaaa")

if __name__ == "__main__":
    app = GrayScale()
    app.convert()
    app = Cannyclass()
    app.convert_canny()

