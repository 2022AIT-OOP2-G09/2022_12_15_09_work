from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import time
import image_processing
import os

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

#
@app.route("/input_image" , methods=["GET"])
def Input_IMG():
    IMG_LIST = os.listdir('./static/input_image')
    IMG_LIST = ['input_image/' + i for i in IMG_LIST]
    imagelist=IMG_LIST
    return render_template("input_image.html", imagelist = imagelist)

#
@app.route("/frame_image" , methods=["GET"])
def Frame_IMG():
    IMG_LIST = os.listdir('static/face_detection_frame')
    IMG_LIST = ['face_detection_frame/' + i for i in IMG_LIST]
    imagelist=IMG_LIST
    return render_template("frame_image.html", imagelist = imagelist)

#
@app.route("/mosaic_image" , methods=["GET"])
def Mosaic_IMG():
    IMG_LIST = os.listdir('face_detection_mosaic')
    IMG_LIST = ['face_detection_mosaic/' + i for i in IMG_LIST]
    imagelist=IMG_LIST
    return render_template("mosaic_image.html", imagelist = imagelist)

#
@app.route("/gray_image" , methods=["GET"])
def Glay_IMG():
    IMG_LIST = os.listdir('static/output_grayscale_image')
    IMG_LIST = ['output_grayscale_image/' + i for i in IMG_LIST]
    imagelist=IMG_LIST
    return render_template("gray_image.html", imagelist = imagelist)

#
@app.route("/canny_image" , methods=["GET"])
def Canny_IMG():
    IMG_LIST = os.listdir('static/output_cannyfilter_image')
    IMG_LIST = ['output_cannyfilter_image/' + i for i in IMG_LIST]
    imagelist=IMG_LIST
    return render_template("canny_image.html", imagelist = imagelist)
    
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # URLでhttp://127.0.0.1:5000/uploadを指定したときはGETリクエストとなるのでこっち
    if request.method == 'GET':
        return render_template('upload.html')
    # formでsubmitボタンが押されるとPOSTリクエストとなるのでこっち
    elif request.method == 'POST':
        file = request.files['example']
        file.save(os.path.join('./static/input_image', file.filename))
        return redirect(url_for('uploaded_file', filename=file.filename))


@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
    return render_template('uploaded_file.html', filename=filename)



if __name__ == "__main__":

    observer = Observer()
    # 監視するフォルダを第２引数に指定
    observer.schedule(image_processing.ChangeHandler(), './static/input_image', recursive=True)
    # 監視を開始する
    observer.start()
    while True:
        time.sleep(5)
        app.run(debug=True)