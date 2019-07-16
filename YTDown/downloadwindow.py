# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YTDown\downloadwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadWindow(object):
    def setupUi(self, DownloadWindow):
        DownloadWindow.setObjectName("DownloadWindow")
        DownloadWindow.resize(509, 111)
        self.centralWidget = QtWidgets.QWidget(DownloadWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralWidget)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.urlLine = QtWidgets.QLineEdit(self.centralWidget)
        self.urlLine.setObjectName("urlLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.urlLine)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.titleLine = QtWidgets.QLineEdit(self.centralWidget)
        self.titleLine.setObjectName("titleLine")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.titleLine)
        self.downloadBut = QtWidgets.QPushButton(self.centralWidget)
        self.downloadBut.setObjectName("downloadBut")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.downloadBut)
        DownloadWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(DownloadWindow)
        QtCore.QMetaObject.connectSlotsByName(DownloadWindow)

    def retranslateUi(self, DownloadWindow):
        _translate = QtCore.QCoreApplication.translate
        DownloadWindow.setWindowTitle(_translate("DownloadWindow", "DownloadWindow"))
        self.label_2.setText(_translate("DownloadWindow", "Url"))
        self.label.setText(_translate("DownloadWindow", "Title"))
        self.downloadBut.setText(_translate("DownloadWindow", "Download"))

