import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog

from PyQt6.QtGui import QIcon

from UI.ImageGUI.ImageFrame import ImageFrame
from UI.tools.ToolsPaletes import ToolsPaletes
from engine import Engine


class MainFrame(QWidget):
    class __ext_buttons(QWidget):
        def __init__(self, topWidget, engine):
            super().__init__(topWidget)
            self.engine = engine

            self.setFixedWidth(400)

            layout = QHBoxLayout()
            self.setLayout(layout)

            saveButton = QPushButton('сохранить картинку')
            saveButton.clicked.connect(self.savePicture)
            layout.addWidget(saveButton)

            saveButton = QPushButton('отменить фильтры')
            saveButton.clicked.connect(engine.reset)
            layout.addWidget(saveButton)

        def savePicture(self):
            if self.engine.pixmap_exist():
                path = QFileDialog.getSaveFileName(
                    self, 'Save File', "pic (*.png)")[0]
                if len(path) != 0:
                    try:
                        self.engine.save_picture(path)
                    except:
                        print('some thing went terribly wrong on the saving')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = None

        self.setWindowTitle('Предобработчик изображений GUI')

        mainlayout = QVBoxLayout()
        self.setLayout(mainlayout)

        # main two columns of app
        innerlayout = QHBoxLayout()
        mainlayout.addItem(innerlayout)

        engine = Engine()

        innerlayout.addWidget(ImageFrame(self, engine))
        innerlayout.addWidget(ToolsPaletes(self, engine))

        mainlayout.addWidget(self.__ext_buttons(self, engine))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('images/app_images/app_icon.png'))
    window = MainFrame()
    app.exec()
