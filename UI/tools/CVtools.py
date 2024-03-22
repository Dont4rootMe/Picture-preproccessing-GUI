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
        def _no_style(self):
            self.btnNone.setStyleSheet(None)
            self.btn22.setStyleSheet(None)
            self.btn33.setStyleSheet(None)
            self.btn44.setStyleSheet(None)
            self.btn55.setStyleSheet(None)

        def __clear_styles(func):
            def inner(self, *args, **kwargs):
                self._no_style()
                func(self, *args, **kwargs)
            return inner

        def __init__(self, topModel, engine):
            super().__init__(topModel)
            self.engine = engine

            self.btnNone = QPushButton('нет')
            self.btnNone.clicked.connect(self.btnNone_click)
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.btn22 = QPushButton('2x2')
            self.btn22.clicked.connect(self.btn22_click)
            self.btn33 = QPushButton('3x3')
            self.btn33.clicked.connect(self.btn33_click)
            self.btn44 = QPushButton('4x4')
            self.btn44.clicked.connect(self.btn44_click)
            self.btn55 = QPushButton('5x5')
            self.btn55.clicked.connect(self.btn55_click)

            layout = QHBoxLayout()
            layout.addWidget(self.btnNone)
            layout.addWidget(self.btn22)
            layout.addWidget(self.btn33)
            layout.addWidget(self.btn44)
            layout.addWidget(self.btn55)

            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            self.setLayout(layout)

        @__clear_styles
        def btnNone_click(self, event):
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change(None)

        @__clear_styles
        def btn22_click(self, event):
            self.btn22.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change((2, 2))

        @__clear_styles
        def btn33_click(self, event):
            self.btn33.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change((3, 3))

        @__clear_styles
        def btn44_click(self, event):
            self.btn44.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change((4, 4))

        @__clear_styles
        def btn55_click(self, event):
            self.btn55.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.erosion_change((5, 5))

    class __dilation_tool(QWidget):
        def _no_style(self):
            self.btnNone.setStyleSheet(None)
            self.btn22.setStyleSheet(None)
            self.btn33.setStyleSheet(None)
            self.btn44.setStyleSheet(None)
            self.btn55.setStyleSheet(None)

        def __clear_styles(func):
            def inner(self, *args, **kwargs):
                self._no_style()
                func(self, *args, **kwargs)
            return inner

        def __init__(self, topModel, engine):
            super().__init__(topModel)
            self.engine = engine

            self.btnNone = QPushButton('нет')
            self.btnNone.clicked.connect(self.btnNone_click)
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.btn22 = QPushButton('2x2')
            self.btn22.clicked.connect(self.btn22_click)
            self.btn33 = QPushButton('3x3')
            self.btn33.clicked.connect(self.btn33_click)
            self.btn44 = QPushButton('4x4')
            self.btn44.clicked.connect(self.btn44_click)
            self.btn55 = QPushButton('5x5')
            self.btn55.clicked.connect(self.btn55_click)

            layout = QHBoxLayout()
            layout.addWidget(self.btnNone)
            layout.addWidget(self.btn22)
            layout.addWidget(self.btn33)
            layout.addWidget(self.btn44)
            layout.addWidget(self.btn55)

            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            self.setLayout(layout)

        @__clear_styles
        def btnNone_click(self, event):
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change(None)

        @__clear_styles
        def btn22_click(self, event):
            self.btn22.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change((2, 2))

        @__clear_styles
        def btn33_click(self, event):
            self.btn33.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change((3, 3))

        @__clear_styles
        def btn44_click(self, event):
            self.btn44.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change((4, 4))

        @__clear_styles
        def btn55_click(self, event):
            self.btn55.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.dilation_change((5, 5))

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
        def _no_style(self):
            self.btnNone.setStyleSheet(None)
            self.btn22.setStyleSheet(None)
            self.btn33.setStyleSheet(None)
            self.btn44.setStyleSheet(None)
            self.btn55.setStyleSheet(None)

        def __clear_styles(func):
            def inner(self, *args, **kwargs):
                self._no_style()
                func(self, *args, **kwargs)
            return inner

        def __init__(self, topModel, engine):
            super().__init__(topModel)
            self.engine = engine

            self.btnNone = QPushButton('нет')
            self.btnNone.clicked.connect(self.btnNone_click)
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.btn22 = QPushButton('2x2')
            self.btn22.clicked.connect(self.btn22_click)
            self.btn33 = QPushButton('3x3')
            self.btn33.clicked.connect(self.btn33_click)
            self.btn44 = QPushButton('4x4')
            self.btn44.clicked.connect(self.btn44_click)
            self.btn55 = QPushButton('5x5')
            self.btn55.clicked.connect(self.btn55_click)

            layout = QHBoxLayout()
            layout.addWidget(self.btnNone)
            layout.addWidget(self.btn22)
            layout.addWidget(self.btn33)
            layout.addWidget(self.btn44)
            layout.addWidget(self.btn55)

            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            self.setLayout(layout)

        @__clear_styles
        def btnNone_click(self, event):
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change(None)

        @__clear_styles
        def btn22_click(self, event):
            self.btn22.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change((2, 2))

        @__clear_styles
        def btn33_click(self, event):
            self.btn33.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change((3, 3))

        @__clear_styles
        def btn44_click(self, event):
            self.btn44.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change((4, 4))

        @__clear_styles
        def btn55_click(self, event):
            self.btn55.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.opening_change((5, 5))

    class __closing_tool(QWidget):
        def _no_style(self):
            self.btnNone.setStyleSheet(None)
            self.btn22.setStyleSheet(None)
            self.btn33.setStyleSheet(None)
            self.btn44.setStyleSheet(None)
            self.btn55.setStyleSheet(None)

        def __clear_styles(func):
            def inner(self, *args, **kwargs):
                self._no_style()
                func(self, *args, **kwargs)
            return inner

        def __init__(self, topModel, engine):
            super().__init__(topModel)
            self.engine = engine

            self.btnNone = QPushButton('нет')
            self.btnNone.clicked.connect(self.btnNone_click)
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.btn22 = QPushButton('2x2')
            self.btn22.clicked.connect(self.btn22_click)
            self.btn33 = QPushButton('3x3')
            self.btn33.clicked.connect(self.btn33_click)
            self.btn44 = QPushButton('4x4')
            self.btn44.clicked.connect(self.btn44_click)
            self.btn55 = QPushButton('5x5')
            self.btn55.clicked.connect(self.btn55_click)

            layout = QHBoxLayout()
            layout.addWidget(self.btnNone)
            layout.addWidget(self.btn22)
            layout.addWidget(self.btn33)
            layout.addWidget(self.btn44)
            layout.addWidget(self.btn55)

            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            self.setLayout(layout)

        @__clear_styles
        def btnNone_click(self, event):
            self.btnNone.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change(None)

        @__clear_styles
        def btn22_click(self, event):
            self.btn22.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change((2, 2))

        @__clear_styles
        def btn33_click(self, event):
            self.btn33.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change((3, 3))

        @__clear_styles
        def btn44_click(self, event):
            self.btn44.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change((4, 4))

        @__clear_styles
        def btn55_click(self, event):
            self.btn55.setStyleSheet(CLICKED_BUTTON_STYLE)
            self.engine.closing_change((5, 5))

    def __init__(self, topModel, engine):
        super().__init__(topModel)
        self.engine = engine

        self.erosion_tool = self.__erosion_tool(self, self.engine)
        self.dilation_tool = self.__dilation_tool(self, self.engine)
        self.opening_tool = self.__opening_tool(self, self.engine)
        self.closing_tool = self.__closing_tool(self, self.engine)

        self.layout = QFormLayout()
        self.layout.addRow('Erosion: ', self.erosion_tool)
        self.layout.addRow('Dilation: ', self.dilation_tool)
        self.layout.addRow('Opening: ', self.opening_tool)
        self.layout.addRow('Closing: ', self.closing_tool)

        self.engine.on_upload(self.clear_styles)
        self.setLayout(self.layout)

    def clear_styles(self):
        self.erosion_tool._no_style()
        self.dilation_tool._no_style()
        self.opening_tool._no_style()
        self.closing_tool._no_style()

        self.erosion_tool.btnNone_click(None)
        self.dilation_tool.btnNone_click(None)
        self.opening_tool.btnNone_click(None)
        self.closing_tool.btnNone_click(None)
