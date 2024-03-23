from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QCheckBox, QSlider
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt


class CountObjects(QWidget):
    def __init__(self, topWidget, engine):
        super().__init__(topWidget)
        self.engine = engine

        self.LABEL_START = 'Число объектов: '

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button_layout = QHBoxLayout()

        button_count = QPushButton('Найти объекты')
        button_count.clicked.connect(self.engine.find_componens)
        button_layout.addWidget(button_count)

        self.label_count_objects = QLabel()
        self.engine.on_change(self.change_object_count)
        button_layout.addWidget(self.label_count_objects)

        self.checkbox = QCheckBox('показывать центры объектов')
        self.checkbox.stateChanged.connect(self.show_objects)

        layout.addItem(button_layout)

        clsize_layout = QHBoxLayout()
        label_size = QLabel('минимальный размер: ')
        min_clust_size_slider = QSlider(Qt.Orientation.Horizontal)
        min_clust_size_slider.setRange(0, 100)
        min_clust_size_slider.setValue(15)
        min_clust_size_slider.setFixedSize(QSize(200, 30))
        min_clust_size_slider.valueChanged.connect(
            self.engine.change_min_clustsize)

        clsize_layout.addWidget(label_size)
        clsize_layout.addWidget(min_clust_size_slider)

        layout.addItem(clsize_layout)

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
