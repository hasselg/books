# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'books_viewer.ui'
#
# Created: Sat Nov 27 20:18:51 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_book_viewer_form(object):
    def setupUi(self, book_viewer_form):
        book_viewer_form.setObjectName(_fromUtf8("book_viewer_form"))
        book_viewer_form.resize(800, 600)
        self.centralwidget = QtGui.QWidget(book_viewer_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.web_viewer = QtWebKit.QWebView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web_viewer.sizePolicy().hasHeightForWidth())
        self.web_viewer.setSizePolicy(sizePolicy)
        self.web_viewer.setUrl(QtCore.QUrl(_fromUtf8("http://www.google.com/")))
        self.web_viewer.setObjectName(_fromUtf8("web_viewer"))
        self.horizontalLayout.addWidget(self.web_viewer)
        book_viewer_form.setCentralWidget(self.centralwidget)

        self.retranslateUi(book_viewer_form)
        QtCore.QObject.connect(self.web_viewer, QtCore.SIGNAL(_fromUtf8("titleChanged(QString)")), book_viewer_form.setWindowTitle)
        QtCore.QMetaObject.connectSlotsByName(book_viewer_form)

    def retranslateUi(self, book_viewer_form):
        book_viewer_form.setWindowTitle(QtGui.QApplication.translate("book_viewer_form", "Books!", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
