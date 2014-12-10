# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sumit\workspace\spreader\src\spreader.ui'
#
# Created: Tue May 06 15:52:38 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(399, 545)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 381, 261))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 40, 351, 121))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.wpmlabel = QtGui.QLabel(self.tab)
        self.wpmlabel.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.wpmlabel.setObjectName(_fromUtf8("wpmlabel"))
        self.chunklabel = QtGui.QLabel(self.tab)
        self.chunklabel.setGeometry(QtCore.QRect(80, 10, 151, 16))
        self.chunklabel.setObjectName(_fromUtf8("chunklabel"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 180, 361, 52))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.dial_1 = QtGui.QDial(self.layoutWidget)
        self.dial_1.setMinimum(1)
        self.dial_1.setMaximum(9)
        self.dial_1.setPageStep(1)
        self.dial_1.setNotchesVisible(True)
        self.dial_1.setObjectName(_fromUtf8("dial_1"))
        self.horizontalLayout_2.addWidget(self.dial_1)
        self.dial_2 = QtGui.QDial(self.layoutWidget)
        self.dial_2.setMaximum(9)
        self.dial_2.setPageStep(1)
        self.dial_2.setNotchesVisible(True)
        self.dial_2.setObjectName(_fromUtf8("dial_2"))
        self.horizontalLayout_2.addWidget(self.dial_2)
        self.dial_3 = QtGui.QDial(self.layoutWidget)
        self.dial_3.setMaximum(9)
        self.dial_3.setPageStep(1)
        self.dial_3.setNotchesVisible(True)
        self.dial_3.setObjectName(_fromUtf8("dial_3"))
        self.horizontalLayout_2.addWidget(self.dial_3)
        self.wordChunkSlider = QtGui.QSlider(self.layoutWidget)
        self.wordChunkSlider.setMinimum(1)
        self.wordChunkSlider.setMaximum(5)
        self.wordChunkSlider.setPageStep(1)
        self.wordChunkSlider.setOrientation(QtCore.Qt.Horizontal)
        self.wordChunkSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.wordChunkSlider.setTickInterval(1)
        self.wordChunkSlider.setObjectName(_fromUtf8("wordChunkSlider"))
        self.horizontalLayout_2.addWidget(self.wordChunkSlider)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 361, 221))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.layoutWidget1 = QtGui.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 265, 361, 31))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.newbtn = QtGui.QPushButton(self.layoutWidget1)
        self.newbtn.setObjectName(_fromUtf8("newbtn"))
        self.horizontalLayout.addWidget(self.newbtn)
        self.pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.playPausebtn = QtGui.QPushButton(self.layoutWidget1)
        self.playPausebtn.setCheckable(True)
        self.playPausebtn.setChecked(False)
        self.playPausebtn.setAutoExclusive(False)
        self.playPausebtn.setFlat(False)
        self.playPausebtn.setObjectName(_fromUtf8("playPausebtn"))
        self.horizontalLayout.addWidget(self.playPausebtn)
        self.plainTextEdit_temp = QtGui.QPlainTextEdit(Dialog)
        self.plainTextEdit_temp.setGeometry(QtCore.QRect(20, 300, 361, 231))
        self.plainTextEdit_temp.setObjectName(_fromUtf8("plainTextEdit_temp"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "sadfasdf", None))
        self.wpmlabel.setText(_translate("Dialog", "WPM:", None))
        self.chunklabel.setText(_translate("Dialog", "Wods per Chunk", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Read", None))
        self.plainTextEdit.setPlainText(_translate("Dialog", "sadfsadlfkmasdfklnasdfasmdkf,asdfkm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Write", None))
        self.newbtn.setText(_translate("Dialog", "From ClipBoard", None))
        self.pushButton.setText(_translate("Dialog", "From \"write\" tab", None))
        self.playPausebtn.setText(_translate("Dialog", "Play", None))

