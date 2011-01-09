#!/usr/bin/env pythonw
import os
import sys

import cherry_server as books_server

from PyQt4 import QtCore, QtGui
from books_viewer import Ui_book_viewer_form

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except:
    _fromUtf8 = lambda s: s

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_book_viewer_form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    # Start the embedded server
    sys.path.append(os.getcwd())
    os.environ['DJANGO_SETTINGS_MODULE'] = 'books.settings'
    server = books_server.Server()
    server.start()

    # Launch the Viewer
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.ui.web_viewer.setUrl(QtCore.QUrl(_fromUtf8("http://localhost:8080/books/library/")))
    myapp.show()

    # Wait until the viewer window is closed
    app.exec_()

    # Shutdown the embedded server
    server.stop()

