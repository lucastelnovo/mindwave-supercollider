# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(859, 140)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.horizontalLayout.addWidget(self.startButton)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.deviceComboBox = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deviceComboBox.sizePolicy().hasHeightForWidth())
        self.deviceComboBox.setSizePolicy(sizePolicy)
        self.deviceComboBox.setObjectName(_fromUtf8("deviceComboBox"))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.deviceComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.deviceComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.eyeBlinkSensitivity = QtGui.QLineEdit(self.centralwidget)
        self.eyeBlinkSensitivity.setObjectName(_fromUtf8("eyeBlinkSensitivity"))
        self.horizontalLayout_2.addWidget(self.eyeBlinkSensitivity)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lowerEyeBlinkFrequency = QtGui.QLineEdit(self.centralwidget)
        self.lowerEyeBlinkFrequency.setObjectName(_fromUtf8("lowerEyeBlinkFrequency"))
        self.horizontalLayout_2.addWidget(self.lowerEyeBlinkFrequency)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.higherEyeBlinkFrequency = QtGui.QLineEdit(self.centralwidget)
        self.higherEyeBlinkFrequency.setObjectName(_fromUtf8("higherEyeBlinkFrequency"))
        self.horizontalLayout_2.addWidget(self.higherEyeBlinkFrequency)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 84, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSave_state = QtGui.QAction(MainWindow)
        self.actionSave_state.setObjectName(_fromUtf8("actionSave_state"))
        self.actionLoad_state = QtGui.QAction(MainWindow)
        self.actionLoad_state.setObjectName(_fromUtf8("actionLoad_state"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.deviceComboBox, self.eyeBlinkSensitivity)
        MainWindow.setTabOrder(self.eyeBlinkSensitivity, self.lowerEyeBlinkFrequency)
        MainWindow.setTabOrder(self.lowerEyeBlinkFrequency, self.higherEyeBlinkFrequency)
        MainWindow.setTabOrder(self.higherEyeBlinkFrequency, self.startButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.startButton.setText(_translate("MainWindow", "Start/Stop", None))
        self.label.setText(_translate("MainWindow", "Mindwave device", None))
        self.deviceComboBox.setItemText(0, _translate("MainWindow", "/dev/rfcomm0", None))
        self.deviceComboBox.setItemText(1, _translate("MainWindow", "/dev/rfcomm1", None))
        self.deviceComboBox.setItemText(2, _translate("MainWindow", "/dev/rfcomm2", None))
        self.deviceComboBox.setItemText(3, _translate("MainWindow", "/dev/ttyUSB0", None))
        self.deviceComboBox.setItemText(4, _translate("MainWindow", "/dev/ttyUSB1", None))
        self.deviceComboBox.setItemText(5, _translate("MainWindow", "/dev/ttyUSB2", None))
        self.deviceComboBox.setItemText(6, _translate("MainWindow", "/dev/ttyS0", None))
        self.deviceComboBox.setItemText(7, _translate("MainWindow", "/dev/ttyS1", None))
        self.deviceComboBox.setItemText(8, _translate("MainWindow", "/dev/ttyS2", None))
        self.deviceComboBox.setItemText(9, _translate("MainWindow", "/dev/tty0", None))
        self.deviceComboBox.setItemText(10, _translate("MainWindow", "/dev/tty1", None))
        self.deviceComboBox.setItemText(11, _translate("MainWindow", "/dev/tty2", None))
        self.label_2.setText(_translate("MainWindow", "Eye blink sensitivity", None))
        self.eyeBlinkSensitivity.setText(_translate("MainWindow", "0.45", None))
        self.label_3.setText(_translate("MainWindow", "Lower Eye blink frequency  (Hz)", None))
        self.lowerEyeBlinkFrequency.setText(_translate("MainWindow", "5.0", None))
        self.label_4.setText(_translate("MainWindow", "Higher Eye blink frequency (Hz)", None))
        self.higherEyeBlinkFrequency.setText(_translate("MainWindow", "20.0", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionSave_state.setText(_translate("MainWindow", "Save state", None))
        self.actionLoad_state.setText(_translate("MainWindow", "Load state", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

