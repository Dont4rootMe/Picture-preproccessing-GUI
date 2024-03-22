from PyQt6.QtWidgets import QToolBox, QWidget, QVBoxLayout

from UI.tools.ColorDials import ColorDials
from UI.tools.CVtools import CVtools
from UI.tools.DefaultPalette import DefaultPalette
from UI.tools.CountObjects import CountObjects


class ToolsPaletes(QWidget):
    def __init__(self, topWidget, engine):
        super().__init__(topWidget)
        self.engine = engine

        layout = QVBoxLayout()
        tlbx = QToolBox()

        tlbx.addItem(ColorDials(self, engine), 'Точечные операции')
        tlbx.addItem(CVtools(self, engine), 'Морфологические операции')
        tlbx.addItem(CountObjects(self, engine), 'Подсчет объектов')
        tlbx.addItem(DefaultPalette(self, engine), 'demo изображения')

        layout.addWidget(tlbx)
        self.setLayout(layout)
