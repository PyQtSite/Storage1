# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q111sub.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Q1111(object):
    def setupUi(self, Q1111):
        Q1111.setObjectName("Q1111")
        Q1111.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Q1111)
        self.pushButton.setGeometry(QtCore.QRect(140, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Q1111)
        QtCore.QMetaObject.connectSlotsByName(Q1111)

    def retranslateUi(self, Q1111):
        _translate = QtCore.QCoreApplication.translate
        Q1111.setWindowTitle(_translate("Q1111", "Form"))
        self.pushButton.setText(_translate("Q1111", "OK"))
