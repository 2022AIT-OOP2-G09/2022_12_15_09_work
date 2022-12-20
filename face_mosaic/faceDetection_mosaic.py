# 顔検出してモザイクするクラス
# OpenCVを使用しています　opencv-python varsion: 4.6.0.66
# クラスの説明
# パブリック関数
# ・顔検出してモザイクする（ファイルパス:str）
#   戻り値　なし
#   ファイルパスから画像を開き
# 　顔検出検出してモザイク処理
# 　出力画像を保存　画像は　face_detection_mosaic/　の下に保存します
# 　
# このサイトをもとにコードを作成しました
# https://note.nkmk.me/python-opencv-mosaic/

import numpy as np
import cv2
import os

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

# For debug code
if __name__ == "__main__":
    source_pathList = [
        'source/BL004-kopwowatasu20140810_TP_V4.jpg',
        'source/OOK99_facebookiine20131223_TP_V4.jpg',
        'source/TSUCH160130520I9A6560_TP_V4.jpg'
        ]
    for source_path in source_pathList:
        faceDetection_mosaic.Create_faceMosaicImage(source_path)
    # faceDetection_mosaic.Create_faceMosaicImage('source/TSUCH160130520I9A6560_TP_V4.jpg')