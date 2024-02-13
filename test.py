from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.central_widget = QtWidgets.QWidget()
        self.central_layout = QtWidgets.QVBoxLayout()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.central_layout)
        # Lets create some widgets inside
        self.label = QtWidgets.QLabel()
        self.list_view = QtWidgets.QListView()
        self.push_button = QtWidgets.QPushButton()
        self.label.setText(
            'Hi, this is a label. And the next one is a List View :')
        self.push_button.setText('Push Button Here')
        # Lets add the widgets
        self.central_layout.addWidget(self.label)
        self.central_layout.addWidget(self.list_view)
        self.central_layout.addWidget(self.push_button)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
