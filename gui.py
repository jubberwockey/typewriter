from PyQt4 import QtGui, QtCore
import sys


class MainWindow(QtGui.QMainWindow):
    # initialize instance
    def __init__(self):
        # super gives parent class
        # initialize methods from parent class
        super().__init__()
        self.create_ui()

    def create_ui(self):

        # define open entry
        open_file = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.setStatusTip('Open new File')
        open_file.triggered.connect(self.show_file_dialog)

        # define quit entry
        exit_program = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exit_program.setShortcut('Ctrl+Q')
        exit_program.setStatusTip('Exit application')
        exit_program.triggered.connect(QtGui.qApp.quit)

        # define menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(open_file)
        file_menu.addAction(exit_program)

        # add status bar
        self.statusBar()

        # add fields
        text_edit = QtGui.QTextEdit()
        button = QtGui.QPushButton('press me')

        grid = QtGui.QGridLayout()
        grid.addWidget(button, 0,0)
        grid.addWidget(text_edit, 2, 0, 1, 1)


        self.center = QtGui.QWidget()
        self.center.setLayout(grid)
        self.setCentralWidget(self.center)


        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('typewriter')
        self.show()


    def show_file_dialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        f = open(fname, 'r')
        with f:
            data = f.read()
            self.text_edit.setText(data)

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
#        self.drawPoints(qp)
        qp.end()

def main():

    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()