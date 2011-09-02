# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'books_viewer.ui'
#
# Created: Thu Sep  1 20:37:43 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_book_viewer_form(object):
    def setupUi(self, book_viewer_form):
        book_viewer_form.setObjectName("book_viewer_form")
        book_viewer_form.resize(800, 600)
        self.centralwidget = QtGui.QWidget(book_viewer_form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.web_viewer = QtWebKit.QWebView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web_viewer.sizePolicy().hasHeightForWidth())
        self.web_viewer.setSizePolicy(sizePolicy)
        self.web_viewer.setUrl(QtCore.QUrl("http://www.google.com/"))
        self.web_viewer.setObjectName("web_viewer")
        self.horizontalLayout.addWidget(self.web_viewer)
        book_viewer_form.setCentralWidget(self.centralwidget)

        self.retranslateUi(book_viewer_form)
        QtCore.QObject.connect(self.web_viewer, QtCore.SIGNAL("titleChanged(QString)"), book_viewer_form.setWindowTitle)
        QtCore.QMetaObject.connectSlotsByName(book_viewer_form)

    def retranslateUi(self, book_viewer_form):
        book_viewer_form.setWindowTitle(QtGui.QApplication.translate("book_viewer_form", "Books!", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
