from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QCheckBox
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize


class CountObjects(QWidget):
    def __init__(self, topWidget, engine):
        super().__init__(topWidget)
        self.engine = engine

        self.LABEL_START = 'Число объектов: '

        layout = QHBoxLayout()

        button_count = QPushButton('Найти объекты')
        button_count.clicked.connect(self.engine.find_componens)
        layout.addWidget(button_count)

        self.label_count_objects = QLabel()
        self.engine.on_change(self.change_object_count)
        layout.addWidget(self.label_count_objects)

        self.checkbox = QCheckBox('показывать центры объектов')
        self.checkbox.stateChanged.connect(self.show_objects)

        self.setLayout(layout)
        self.change_object_count()

        self.engine.on_change(self.change_object_count)
        self.engine.on_upload(self.clearing)

    def change_object_count(self):
        count = self.engine.get_count()
        self.label_count_objects.setText(self.LABEL_START + str(count))

    def show_objects(self, value):
        self.engine.set_object_show(value != 0)

    def clearing(self):
        self.checkbox.setChecked(False)
        self.label_count_objects.setText(self.LABEL_START)
