import cv2
import os

class GrayScale():
    def __init__(self):
        self.path = os.listdir('./input_image')
        self.threshold = 100
        
    def convert(self):
        for each_path in self.path:
            img = cv2.imread(f'input_image/{each_path}', 0)
            ret, img_thresh = cv2.threshold(img, self.threshold, 255, cv2.THRESH_BINARY)
            cv2.imwrite(f'output_grayscale_image/{each_path}', img_thresh)
        
if __name__ == "__main__":
    app = GrayScale()
    app.convert()