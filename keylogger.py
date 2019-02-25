# from PyQt4 import QtGui, QtCore
# 
# class Window(QtGui.QWidget):
#     def __init__(self):
#         QtGui.QWidget.__init__(self)
#         self.button = QtGui.QPushButton('Test', self)
#         self.button.clicked.connect(self.handleButton)
#         layout = QtGui.QVBoxLayout(self)
#         layout.addWidget(self.button)
#
#     def handleButton(self):
#         modifiers = QtGui.QApplication.keyboardModifiers()
#         if modifiers == QtCore.Qt.ShiftModifier:
#             print('Shift+Click')
#         elif modifiers == QtCore.Qt.ControlModifier:
#             print('Control+Click')
#         elif modifiers == (QtCore.Qt.ControlModifier |
#                            QtCore.Qt.ShiftModifier):
#             print('Control+Shift+Click')
#         else:
#             print('Click')
#
# if __name__ == '__main__':
#
#     import sys
#     app = QtGui.QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
#
# def keyPressEvent(self, event):
#     self.firstrelease = True
#     astr = "pressed: " + str(event.key())
#     self.keylist.append(astr)
#
# def keyReleaseEvent(self, event):
#     if self.firstrelease == True:
#         self.processmultikeys(self.keylist)
#
#     self.firstrelease = False
#     del self.keylist[-1]
#
# def processmultikeys(self,keyspressed):
#     # your logic here
#     print(keyspressed)
#
#
#
# #with KeyPoller() as keyPoller:
# #    while True:
# #        c = keyPoller.poll()
# #        if not c is None:
# #            if c == "c":
# #                break
# #            print(c)
#
#
#
#
