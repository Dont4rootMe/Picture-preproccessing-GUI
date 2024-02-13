import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QFileDialog

from PyQt6.QtGui import QPixmap, QIcon

from UI.images.ImageFrame import ImageFrame
from UI.tools.ToolsPaletes import ToolsPaletes
from engine import Engine


class MainFrame(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = None

        self.setWindowTitle('Предобработчик изображений GUI')

        # main two columns of app
        layout = QHBoxLayout()
        self.setLayout(layout)

        engine = Engine()

        layout.addWidget(ImageFrame(self, engine))
        layout.addWidget(ToolsPaletes(self, engine))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./app_icon.png'))
    window = MainFrame()
    app.exec()
