from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFileDialog, QPushButton
from PyQt6.QtGui import QDragEnterEvent, QPixmap
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt


class ImageBox(QLabel):
    def __init__(self, topWidget, engine):
        super().__init__(topWidget)
        self.engine = engine
        self.engine.on_change(self.refresh_pic)
        self.engine.on_upload(self.refresh_pic)

        if not self.engine.pixmap_exist():
            self.pixels = QPixmap('images/app_images/default_photo.png')

        self.setPixmap(self.pixels)
        self.setScaledContents(True)
        self.setMaximumSize(QSize(300, 300))
        self.setMinimumSize(QSize(100, 100))

    def refresh_pic(self):
        if self.engine.pixmap_exist():
            self.setPixmap(self.engine.get_pixmap())

    def mouseDoubleClickEvent(self, event):
        file_input = QFileDialog()
        if file_input.exec():
            self.engine.upload_picture(file_input.selectedFiles()[0])
