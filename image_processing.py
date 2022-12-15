#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os


class Cannyclass():
    def __init__(self):
        self.path = os.listdir('./input_image')

    def convert_canny(self):
        for each_path in self.path:
            img = cv2.imread(f'./input_image/{each_path}',0)
            edges = cv2.Canny(img,100,200)
            cv2.imwrite(f'./output_cannyfilter_image/{each_path}',edges)

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

class faceDetection_mosaic:

    def Create_faceMosaicImage(source_path:str) -> None:
        source_name = os.path.basename(source_path)
        output_path = "face_detection_mosaic/" + source_name

        # 画像読み込み
        src_img = cv2.imread(source_path)
        # 画像から顔検出してモザイクをかける
        output_img = faceDetection_mosaic.__faceMosaic(src_img)
        # 画像保存
        cv2.imwrite(output_path, output_img)

    def __faceMosaic(src):
        # 画像から顔検出してモザイクをかけるメソッド
        face_cascade_path = 'face_mosaic/haarcascade_frontalface_default.xml'
        face_cascade = cv2.CascadeClassifier(face_cascade_path)

        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(src_gray)

        for x, y, w, h in faces:
            dst_face = faceDetection_mosaic.__mosaic_area(src, x, y, w, h)

        return dst_face

    def __mosaic_area(src, x, y, width, height, ratio=0.1):
        # 範囲指定のモザイクをかけるメソッド
        dst = src.copy()
        dst[y:y + height, x:x + width] = faceDetection_mosaic.__mosaic(dst[y:y + height, x:x + width], ratio)
        return dst
    def __mosaic(src, ratio=0.1):
        # モザイクをかけるメソッド
        small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

if __name__ == "__main__":
    app = GrayScale()
    app.convert()
    app = Cannyclass()
    app.convert_canny()
    app = faceDetection_mosaic()
    app.Create_faceMosaicImage()

