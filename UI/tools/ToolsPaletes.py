from PyQt6.QtWidgets import QToolBox, QWidget, QHBoxLayout, QLabel, QVBoxLayout

from UI.tools.ColorDials import ColorDials
from UI.tools.CVtools import CVtools
from UI.tools.DefaultPalette import DefaultPalette


class ToolsPaletes(QWidget):
    def __init__(self, topWidget, engine):
        super().__init__(topWidget)
        self.engine = engine

        layout = QVBoxLayout()
        tlbx = QToolBox()

        tlbx.addItem(ColorDials(self, engine), 'Палитра цветов')
        tlbx.addItem(CVtools(self, engine), 'средства OpenCV')
        tlbx.addItem(DefaultPalette(self, engine), 'demo изображения')

        layout.addWidget(tlbx)
        self.setLayout(layout)
