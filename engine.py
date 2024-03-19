from PyQt6.QtGui import QPixmap
from PIL import Image, ImageEnhance, ImageQt
import numpy as np
import cv2 as cv


class Engine:
    def reset(self):
        self.__whipe_dict()
        for upl in self.upload_actions:
            upl()

    def refresh(self):
        for refr in self.refresh_actions:
            refr()

    def __refresher__(func):
        def inner(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.refresh()
        return inner

    def __whipe_dict(self):
        self.actions = {
            'brightness': False,
            'contrast': False,
            'sharpness': False,
            'saturation': False,
            'color_enhancements': [1.0, 1.0, 1.0],
            'erosion': None,
            'dilation': None,
            'opening': None,
            'closing': None
        }

    def __init__(self):
        self.img = None
        self.modified = None
        self.refresh_actions = []
        self.upload_actions = []

        self.__whipe_dict()

    def on_change(self, func):
        self.refresh_actions.append(func)

    def on_upload(self, func):
        self.upload_actions.append(func)

    def pixmap_exist(self):
        return self.img is not None

    def get_pixmap(self):
        temp = self.img.copy()
        if self.actions['brightness']:
            enhancer = ImageEnhance.Brightness(temp)
            temp = enhancer.enhance(self.actions['brightness'])
        if self.actions['contrast']:
            enhancer = ImageEnhance.Contrast(temp)
            temp = enhancer.enhance(self.actions['contrast'])
        if self.actions['sharpness']:
            enhancer = ImageEnhance.Sharpness(temp)
            temp = enhancer.enhance(self.actions['sharpness'])
        if self.actions['saturation']:
            enhancer = ImageEnhance.Color(temp)
            temp = enhancer.enhance(self.actions['saturation'])

        Matrix = np.array(temp).astype(float)
        Matrix[..., 0] *= self.actions['color_enhancements'][0]
        Matrix[..., 1] *= self.actions['color_enhancements'][1]
        Matrix[..., 2] *= self.actions['color_enhancements'][2]
        temp = Image.fromarray(Matrix.astype(np.uint8))

        if self.actions['erosion'] is not None:
            Matrix = np.array(temp).astype(float)
            temp = cv.erode(Matrix, self.actions['erosion'], iterations=1)
            temp = Image.fromarray(temp.astype(np.uint8))

        if self.actions['dilation'] is not None:
            Matrix = np.array(temp).astype(float)
            temp = cv.dilate(Matrix, self.actions['dilation'], iterations=1)
            temp = Image.fromarray(temp.astype(np.uint8))

        if self.actions['opening'] is not None:
            Matrix = np.array(temp).astype(float)
            temp = cv.morphologyEx(
                Matrix, cv.MORPH_OPEN, self.actions['opening'])
            temp = Image.fromarray(temp.astype(np.uint8))

        if self.actions['closing'] is not None:
            Matrix = np.array(temp).astype(float)
            temp = cv.morphologyEx(
                Matrix, cv.MORPH_CLOSE, self.actions['closing'])
            temp = Image.fromarray(temp.astype(np.uint8))

        self.modified = temp
        return QPixmap.fromImage(ImageQt.ImageQt(temp))

    def upload_picture(self, path):
        self.img = Image.open(path)
        self.pixmap = QPixmap(path)

        self.reset()

    def save_picture(self, path):
        self.modified.save(path)

    @__refresher__
    def change_brightness(self, brightness):
        k = (brightness - 127) / 128 + 1.0
        self.actions['brightness'] = k

    @__refresher__
    def change_contrast(self, contrast):
        k = (contrast - 127) / 128 + 1.0
        self.actions['contrast'] = k

    @__refresher__
    def change_sharpness(self, sharpness):
        k = ((sharpness - 127) / 128) * 8 + 1.0
        self.actions['sharpness'] = k

    @__refresher__
    def change_saturation(self, saturation):
        k = ((saturation - 127) / 128) + 1.0
        self.actions['saturation'] = k

    @__refresher__
    def enhance_red(self, red):
        k = (red - 200) / 200 + 1.0
        self.actions['color_enhancements'][0] = k

    @__refresher__
    def enhance_green(self, green):
        k = (green - 200) / 200 + 1.0
        self.actions['color_enhancements'][1] = k

    @__refresher__
    def enhance_blue(self, blue):
        k = (blue - 200) / 200 + 1.0
        self.actions['color_enhancements'][2] = k

    @__refresher__
    def erosion_change(self, erosion):
        if erosion is None:
            self.actions['erosion'] = None
        kernel = np.ones(erosion, np.uint8)
        self.actions['erosion'] = kernel

    @__refresher__
    def dilation_change(self, dilation):
        if dilation is None:
            self.actions['dilation'] = None
        kernel = np.ones(dilation, np.uint8)
        self.actions['dilation'] = kernel

    @__refresher__
    def opening_change(self, opening):
        if opening is None:
            self.actions['opening'] = None
        kernel = np.ones(opening, np.uint8)
        self.actions['opening'] = kernel

    @__refresher__
    def closing_change(self, closing):
        if closing is None:
            self.actions['closing'] = None
        kernel = np.ones(closing, np.uint8)
        self.actions['closing'] = kernel
