from PyQt6.QtWidgets import QDial, QWidget, QCheckBox, QHBoxLayout, QLabel, QVBoxLayout, QFormLayout, QSlider
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt


class ColorDials(QWidget):
    class __dial_pair(QWidget):
        def __init__(self, topWidget, func, name):
            super().__init__(topWidget)

            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
            self.setLayout(layout)

            self.dial = QDial(self)
            self.dial.setNotchesVisible(True)
            self.dial.setRange(0, 256)
            self.dial.setValue(127)
            self.dial.setMaximumSize(QSize(50, 50))
            self.dial.setMinimumSize(QSize(30, 30))
            self.dial.valueChanged.connect(func)
            layout.addWidget(self.dial)

            self.label = QLabel(name)
            # self.label.setFixedSize(QSize(50, 10))
            layout.addWidget(self.label)
            layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        def clear(self):
            self.dial.setValue(127)

    def __init__(self, topWidget, engine):
        super().__init__(topWidget)
        self.engine = engine

        self.brightness = self.__dial_pair(
            self, engine.change_brightness, 'brightness')
        self.contrast = self.__dial_pair(
            self, engine.change_contrast, 'contrast')
        self.sharpness = self.__dial_pair(
            self, engine.change_sharpness, 'sharpness')
        self.saturation = self.__dial_pair(
            self, engine.change_saturation, 'saturation')

        self.layout_dials = QHBoxLayout()
        self.layout_dials.addStretch()
        self.layout_dials.addWidget(self.brightness)
        self.layout_dials.addWidget(self.contrast)
        self.layout_dials.addWidget(self.sharpness)
        self.layout_dials.addWidget(self.saturation)

        self.layout_enhancers = QFormLayout()
        self.red_slider = QSlider(Qt.Orientation.Horizontal)
        self.red_slider.setRange(0, 401)
        self.red_slider.setValue(200)
        self.red_slider.setFixedSize(QSize(200, 30))
        self.red_slider.valueChanged.connect(self.engine.enhance_red)
        self.layout_enhancers.addRow('red:', self.red_slider)

        self.green_slider = QSlider(Qt.Orientation.Horizontal)
        self.green_slider.setRange(0, 401)
        self.green_slider.setValue(200)
        self.green_slider.setFixedSize(QSize(200, 30))
        self.green_slider.valueChanged.connect(self.engine.enhance_green)
        self.layout_enhancers.addRow('green:', self.green_slider)

        self.blue_slider = QSlider(Qt.Orientation.Horizontal)
        self.blue_slider.setRange(0, 401)
        self.blue_slider.setValue(200)
        self.blue_slider.setFixedSize(QSize(200, 30))
        self.blue_slider.valueChanged.connect(self.engine.enhance_blue)
        self.layout_enhancers.addRow('blue:', self.blue_slider)

        self.layout_binarize = QHBoxLayout()
        self.use_binarize = QCheckBox('Binarize: ')
        self.use_binarize.stateChanged.connect(self.checkbox_binarize)
        self.layout_binarize.addWidget(self.use_binarize)

        self.binarize_slider = QSlider(Qt.Orientation.Horizontal)
        self.binarize_slider.setDisabled(True)
        self.binarize_slider.setRange(1, 255)
        self.binarize_slider.setValue(128)
        self.binarize_slider.setFixedSize(QSize(200, 30))
        self.binarize_slider.valueChanged.connect(self.engine.binarize)

        self.layout_binarize.addWidget(self.binarize_slider)

        self.layout = QVBoxLayout()
        self.layout.addItem(self.layout_dials)
        self.layout.addItem(self.layout_enhancers)
        self.layout.addItem(self.layout_binarize)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setLayout(self.layout)

        engine.on_upload(self.clear_dials)

    def checkbox_binarize(self, value):
        if value == 0:
            self.binarize_slider.setDisabled(True)
            self.engine.binarize(None)
        else:
            self.binarize_slider.setDisabled(False)
            self.engine.binarize(self.binarize_slider.value())

    def clear_dials(self):
        self.brightness.clear()
        self.contrast.clear()
        self.sharpness.clear()
        self.saturation.clear()

        self.red_slider.setValue(200)
        self.green_slider.setValue(200)
        self.blue_slider.setValue(200)

        self.use_binarize.setChecked(False)
        self.binarize_slider.setValue(128)
