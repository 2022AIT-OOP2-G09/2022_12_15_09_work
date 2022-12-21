import cv2
import os
import numpy

# 分類器ディレクトリ(以下から取得)
# https://github.com/opencv/opencv/blob/master/data/haarcascades/
# https://github.com/opencv/opencv_contrib/blob/master/modules/face/data/cascades/

class face_recognition:

    def img_processing(self):

        path = os.getcwd()
        os.chdir(path)
        print(path)

        cascade_path = "./module/haarcascade_frontalface_default.xml"
        # 使用ファイルと入出力ディレクトリ
        #とりあえず画像指定してる
        input_img = 'uchitane_far.png'
        image_path = "./static/input_image/" + input_img
        output_path = "./static/output_face_recognition"
        #ファイル読み込み
        image = cv2.imread(image_path)
        #グレースケール変換
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #カスケード分類器の特徴量を取得する
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
        color = (255, 255, 255) 

        if len(facerect) > 0:

            for rect in facerect:
                cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

            os.chdir(output_path)
            cv2.imwrite('output.jpg', image)
            os.chdir(path)

if __name__ == "__main__":
    app = face_recognition()
    app.img_processing()