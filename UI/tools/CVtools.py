from PyQt6.QtWidgets import QWidget, QLabel, QFormLayout, QButtonGroup, QPushButton, QHBoxLayout

CLICKED_BUTTON_STYLE = '''
    background-color: #4e80ee;
    border-radius: 4px; 
    padding: 14px; 
    padding-top: 2px; 
    padding-bottom: 2px; 
    margin: 1px;
    margin-top: 1px;
    margin-bottom: 1px;
'''


class CVtools(QWidget):
    class __erosion_tool(QWidget):
        def __clear_styles(func):
            def inner(self, *args, **kwargs):
                self.btnNone.setStyleSheet(None)
                self.btn33.setStyleSheet(None)
                self.btn55.setStyleSheet(None)
                self.btn77.setStyleSheet(None)
                self.btn99.setStyleSheet(None)
                func(self, *args, **kwargs)
            return inner

        def __init__(self, topModel, engine):
            super().__init__(topModel)
            self.engine = engine

            self.btnNone = QPushButton('нет')
            self.btnNone.clicked.connect(self.btnNone_click)
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.btn33 = QPushButton('3x3')
            self.btn33.clicked.connect(self.btn33_click)
            self.btn55 = QPushButton('5x5')
            self.btn55.clicked.connect(self.btn55_click)
            self.btn77 = QPushButton('9x9')
            self.btn77.clicked.connect(self.btn77_click)
            self.btn99 = QPushButton('15x15')
            self.btn99.clicked.connect(self.btn99_click)

            layout = QHBoxLayout()
            layout.addWidget(self.btnNone)
            layout.addWidget(self.btn33)
            layout.addWidget(self.btn55)
            layout.addWidget(self.btn77)
            layout.addWidget(self.btn99)

            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            self.setLayout(layout)

        @__clear_styles
        def btnNone_click(self, event):
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change(None)

        @__clear_styles
        def btn33_click(self, event):
            self.btn33.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change((3, 3))

        @__clear_styles
        def btn55_click(self, event):
            self.btn55.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change((5, 5))

        @__clear_styles
        def btn77_click(self, event):
            self.btn77.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change((9, 9))

        @__clear_styles
        def btn99_click(self, event):
            self.btn99.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change((15, 15))

    class __dilation_tool(QWidget):
        def __clear_styles(func):
            def inner(self, *args, **kwargs):
                self.btnNone.setStyleSheet(None)
                self.btn33.setStyleSheet(None)
                self.btn55.setStyleSheet(None)
                self.btn77.setStyleSheet(None)
                self.btn99.setStyleSheet(None)
                func(self, *args, **kwargs)
            return inner

        def __init__(self, topModel, engine):
            super().__init__(topModel)
            self.engine = engine

            self.btnNone = QPushButton('нет')
            self.btnNone.clicked.connect(self.btnNone_click)
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.btn33 = QPushButton('3x3')
            self.btn33.clicked.connect(self.btn33_click)
            self.btn55 = QPushButton('5x5')
            self.btn55.clicked.connect(self.btn55_click)
            self.btn77 = QPushButton('9x9')
            self.btn77.clicked.connect(self.btn77_click)
            self.btn99 = QPushButton('15x15')
            self.btn99.clicked.connect(self.btn99_click)

            layout = QHBoxLayout()
            layout.addWidget(self.btnNone)
            layout.addWidget(self.btn33)
            layout.addWidget(self.btn55)
            layout.addWidget(self.btn77)
            layout.addWidget(self.btn99)

            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            self.setLayout(layout)

        @__clear_styles
        def btnNone_click(self, event):
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change(None)

        @__clear_styles
        def btn33_click(self, event):
            self.btn33.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change((3, 3))

        @__clear_styles
        def btn55_click(self, event):
            self.btn55.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change((5, 5))

        @__clear_styles
        def btn77_click(self, event):
            self.btn77.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change((9, 9))

        @__clear_styles
        def btn99_click(self, event):
            self.btn99.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change((15, 15))

    class __action_button(QPushButton):
        def __init__(self, topModel, func):
            super().__init__(topModel)
            self.func = func

            self.setText('применить')
            self.clicked.connect(self.action)
            self.setCheckable(True)
            self.setChecked(False)

        def action(self, checked):
            if checked:
                self.setStyleSheet(CLICKED_BUTTON_STYLE)
            else:
                self.setStyleSheet(None)
            self.func(checked)

    class __opening_tool(QWidget):
        def __clear_styles(func):
            def inner(self, *args, **kwargs):
                self.btnNone.setStyleSheet(None)
                self.btn33.setStyleSheet(None)
                self.btn55.setStyleSheet(None)
                self.btn77.setStyleSheet(None)
                self.btn99.setStyleSheet(None)
                func(self, *args, **kwargs)
            return inner

        def __init__(self, topModel, engine):
            super().__init__(topModel)
            self.engine = engine

            self.btnNone = QPushButton('нет')
            self.btnNone.clicked.connect(self.btnNone_click)
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.btn33 = QPushButton('3x3')
            self.btn33.clicked.connect(self.btn33_click)
            self.btn55 = QPushButton('5x5')
            self.btn55.clicked.connect(self.btn55_click)
            self.btn77 = QPushButton('9x9')
            self.btn77.clicked.connect(self.btn77_click)
            self.btn99 = QPushButton('15x15')
            self.btn99.clicked.connect(self.btn99_click)

            layout = QHBoxLayout()
            layout.addWidget(self.btnNone)
            layout.addWidget(self.btn33)
            layout.addWidget(self.btn55)
            layout.addWidget(self.btn77)
            layout.addWidget(self.btn99)

            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            self.setLayout(layout)

        @__clear_styles
        def btnNone_click(self, event):
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change(None)

        @__clear_styles
        def btn33_click(self, event):
            self.btn33.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change((3, 3))

        @__clear_styles
        def btn55_click(self, event):
            self.btn55.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change((5, 5))

        @__clear_styles
        def btn77_click(self, event):
            self.btn77.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change((9, 9))

        @__clear_styles
        def btn99_click(self, event):
            self.btn99.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change((15, 15))

    class __closing_tool(QWidget):
        def __clear_styles(func):
            def inner(self, *args, **kwargs):
                self.btnNone.setStyleSheet(None)
                self.btn33.setStyleSheet(None)
                self.btn55.setStyleSheet(None)
                self.btn77.setStyleSheet(None)
                self.btn99.setStyleSheet(None)
                func(self, *args, **kwargs)
            return inner

        def __init__(self, topModel, engine):
            super().__init__(topModel)
            self.engine = engine

            self.btnNone = QPushButton('нет')
            self.btnNone.clicked.connect(self.btnNone_click)
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.btn33 = QPushButton('3x3')
            self.btn33.clicked.connect(self.btn33_click)
            self.btn55 = QPushButton('5x5')
            self.btn55.clicked.connect(self.btn55_click)
            self.btn77 = QPushButton('9x9')
            self.btn77.clicked.connect(self.btn77_click)
            self.btn99 = QPushButton('15x15')
            self.btn99.clicked.connect(self.btn99_click)

            layout = QHBoxLayout()
            layout.addWidget(self.btnNone)
            layout.addWidget(self.btn33)
            layout.addWidget(self.btn55)
            layout.addWidget(self.btn77)
            layout.addWidget(self.btn99)

            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            self.setLayout(layout)

        @__clear_styles
        def btnNone_click(self, event):
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change(None)

        @__clear_styles
        def btn33_click(self, event):
            self.btn33.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change((3, 3))

        @__clear_styles
        def btn55_click(self, event):
            self.btn55.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change((5, 5))

        @__clear_styles
        def btn77_click(self, event):
            self.btn77.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change((9, 9))

        @__clear_styles
        def btn99_click(self, event):
            self.btn99.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change((15, 15))

    def __init__(self, topModel, engine):
        super().__init__(topModel)
        self.engine = engine

        self.layout = QFormLayout()
        self.layout.addRow(
            'Erosion: ', self.__erosion_tool(self, self.engine))
        self.layout.addRow(
            'Dilation: ', self.__dilation_tool(self, self.engine))
        self.layout.addRow(
            'Opening: ', self.__opening_tool(self, self.engine))
        self.layout.addRow(
            'Closing: ', self.__closing_tool(self, self.engine))

        self.setLayout(self.layout)
