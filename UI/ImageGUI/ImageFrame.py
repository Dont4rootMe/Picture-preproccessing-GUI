from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFileDialog, QPushButton
from PyQt6.QtGui import QPixmap

from UI.ImageGUI.ImageBox import ImageBox


class ImageFrame(QWidget):
    def __init__(self, topWidget, engine):
        super().__init__(topWidget)
        self.engine = engine

        # vertical layout for image and upload
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # block of image
        self.image = ImageBox(self, engine)
        self.layout.addWidget(self.image)

        # upload block
        upload_block = QWidget(self)
        block_layout = QHBoxLayout()

        upload_button = QPushButton('Upload file')
        upload_button.clicked.connect(self.upload_pic)
        block_layout.addWidget(upload_button)

        upload_label = QLabel('Выберите изображение')
        block_layout.addWidget(upload_label)

        upload_block.setLayout(block_layout)
        upload_block.setMaximumWidth(300)
        upload_block.setMinimumWidth(100)

        self.layout.addWidget(upload_block)

    def upload_pic(self):
        file_input = QFileDialog()
        if file_input.exec():
            self.engine.upload_picture(file_input.selectedFiles()[0])
            # self.engine.set_picture(QPixmap())
            # self.image.refresh_pic()
