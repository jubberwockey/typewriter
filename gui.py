from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
    QLabel, QTextEdit, QPushButton)

from renderer import mathTex_to_QPixmap
import typewriter

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tw = typewriter.Typewriter()

        self.text_label = QLabel('Input here')
        self.text_edit = QTextEdit()

        # buttons invalidate space bar press registered on linux
        # self.generate_btn = QPushButton('Generate')

        self.output_text = ''
        # self.output_label = QLabel(self.output_text, self)
        self.output_label = QLabel()
        self.render_latex()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.text_label, 1, 0)
        # grid.addWidget(self.generate_btn, 3, 0)
        # grid.addWidget(self.text_edit, 1, 1, 2, 1)
        grid.addWidget(self.output_label, 3, 1)

        self.setLayout(grid)
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle('typewriter')
        self.show()


    def keyPressEvent(self, event):
        logging.info("Key pressed")

        if event.key() == Qt.Key_Escape:
            self.close()

        key_meta = {'id': str(event.key()),
                    'text': event.text(),
                    'modifier': str(int(event.modifiers()))}

        logging.debug("keyPressEvent: {id} '{text}' mod: {modifier}".format(**key_meta))

        if not event.isAutoRepeat():
            latex_str = self.tw.process_key_pressed(key_meta)
            self.render_latex(latex_str)


    def keyReleaseEvent(self, event):
        self.tw.process_key_released()
        logging.info("Key released")


    def render_latex(self, latex_str=None):
        # initialize
        if latex_str is None:
            self.pixmap = QPixmap()
        else:
            try:
                self.pixmap = mathTex_to_QPixmap(r'${latex_str}$'.format(latex_str=latex_str),
                                                 fontsize=24)
                self.output_label.setPixmap(self.pixmap)
            except:
                logging.error("latex render error")
