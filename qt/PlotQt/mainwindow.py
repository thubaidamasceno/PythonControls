# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_FancyRLTools(object):
    def setupUi(self, FancyRLTools):
        FancyRLTools.setObjectName(_fromUtf8("FancyRLTools"))
        FancyRLTools.resize(335, 234)
        self.centralwidget = QtWidgets.QWidget(FancyRLTools)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.inputEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEdit.setObjectName(_fromUtf8("inputEdit"))
        self.gridLayout.addWidget(self.inputEdit, 1, 1, 1, 1)
        self.outputEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.outputEdit.setObjectName(_fromUtf8("outputEdit"))
        self.gridLayout.addWidget(self.outputEdit, 0, 1, 1, 1)
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.gridLayout.addWidget(self.convertButton, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.gridLayout.addWidget(self.clearButton, 4, 0, 1, 1)
        self.plotButton = QtWidgets.QPushButton(self.centralwidget)
        self.plotButton.setObjectName(_fromUtf8("plotButton"))
        self.gridLayout.addWidget(self.plotButton, 5, 0, 1, 1)
        FancyRLTools.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FancyRLTools)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 335, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMeters_to_Feet = QtWidgets.QMenu(self.menubar)
        self.menuMeters_to_Feet.setObjectName(_fromUtf8("menuMeters_to_Feet"))
        FancyRLTools.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FancyRLTools)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FancyRLTools.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMeters_to_Feet.menuAction())

        self.retranslateUi(FancyRLTools)
        QtCore.QMetaObject.connectSlotsByName(FancyRLTools)

    def retranslateUi(self, FancyRLTools):
        FancyRLTools.setWindowTitle(_translate("FancyRLTools", "The Fanciest Root Locus", None))
        self.convertButton.setText(_translate("FancyRLTools", "Convert", None))
        self.label.setText(_translate("FancyRLTools", "Radians", None))
        self.label_2.setText(_translate("FancyRLTools", "Degrees", None))
        self.clearButton.setText(_translate("FancyRLTools", "Clear", None))
        self.plotButton.setText(_translate("FancyRLTools", "Plot", None))
        self.menuMeters_to_Feet.setTitle(_translate("FancyRLTools", "The Fanciest Root Locus", None))

