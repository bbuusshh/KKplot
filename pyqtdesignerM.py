# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAINLay.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 673)
        MainWindow.setMaximumSize(QtCore.QSize(950, 673))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_f_beat = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f_beat.setMaximumSize(QtCore.QSize(109, 21))
        self.lineEdit_f_beat.setObjectName("lineEdit_f_beat")
        self.gridLayout_3.addWidget(self.lineEdit_f_beat, 1, 7, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setMaximumSize(QtCore.QSize(33, 16))
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 0, 5, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setMaximumSize(QtCore.QSize(16, 16))
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 1, 2, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setMaximumSize(QtCore.QSize(34, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_5)
        self.verticalLayout.addWidget(self.radioButton_5)
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setMaximumSize(QtCore.QSize(32, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        self.buttonGroup.addButton(self.radioButton_7)
        self.verticalLayout.addWidget(self.radioButton_7)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 4, 1, 1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setMaximumSize(QtCore.QSize(34, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_6)
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setMaximumSize(QtCore.QSize(32, 20))
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup_2.addButton(self.radioButton_8)
        self.verticalLayout_2.addWidget(self.radioButton_8)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 6, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_3, 2, 0, 1, 1)


        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setMaximumSize(QtCore.QSize(26, 16))
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 1, 0, 1, 1)
        self.lineEdit_n = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_n.setMaximumSize(QtCore.QSize(109, 21))
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.gridLayout_3.addWidget(self.lineEdit_n, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setMaximumSize(QtCore.QSize(31, 16))
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setMaximumSize(QtCore.QSize(38, 16))
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 0, 7, 1, 1)
        self.lineEdit_f_rep = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f_rep.setMaximumSize(QtCore.QSize(109, 21))
        self.lineEdit_f_rep.setObjectName("lineEdit_f_rep")
        self.gridLayout_3.addWidget(self.lineEdit_f_rep, 1, 3, 1, 1)
        self.lineEdit_f_ceo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f_ceo.setMaximumSize(QtCore.QSize(109, 21))
        self.lineEdit_f_ceo.setObjectName("lineEdit_f_ceo")
        self.gridLayout_3.addWidget(self.lineEdit_f_ceo, 1, 5, 1, 1)
        self.lineEdit_f_l = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f_l.setMaximumSize(QtCore.QSize(118, 21))
        self.lineEdit_f_l.setObjectName("lineEdit_f_l")
        self.gridLayout_3.addWidget(self.lineEdit_f_l, 1, 9, 1, 1)

        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setMaximumSize(QtCore.QSize(16, 16))
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 1, 8, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16, 16))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setMaximumSize(QtCore.QSize(57, 20))
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMaximumSize(QtCore.QSize(30, 16))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.comboBoxT_int = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxT_int.setMaximumSize(QtCore.QSize(61, 26))
        self.comboBoxT_int.setObjectName("comboBoxT_int")
        self.comboBoxT_int.addItem("")
        self.comboBoxT_int.addItem("")
        self.comboBoxT_int.addItem("")
        self.comboBoxT_int.addItem("")
        self.gridLayout_2.addWidget(self.comboBoxT_int, 0, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setMaximumSize(QtCore.QSize(33, 20))
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setMaximumSize(QtCore.QSize(44, 20))
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)
        self.comboBox_dev = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_dev.setMaximumSize(QtCore.QSize(77, 26))
        self.comboBox_dev.setObjectName("comboBox_f_ceo_2")
        self.comboBox_dev.addItem("")
        self.comboBox_dev.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_dev, 1, 1, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setMaximumSize(QtCore.QSize(29, 21))
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 4, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setMaximumSize(QtCore.QSize(54, 21))
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 5, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMaximumSize(QtCore.QSize(55, 20))
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 7, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setMaximumSize(QtCore.QSize(147, 32))
        self.gridLayout_2.addWidget(self.pushButton, 7, 1, 1, 2)
        self.comboBox_f_ceo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_f_ceo.setMaximumSize(QtCore.QSize(77, 26))
        self.comboBox_f_ceo.setObjectName("comboBox_f_ceo")
        self.comboBox_f_ceo.addItem("")
        self.comboBox_f_ceo.addItem("")
        self.comboBox_f_ceo.addItem("")
        self.comboBox_f_ceo.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_f_ceo, 2, 1, 1, 2)
        self.comboBox_f_beat = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_f_beat.setMaximumSize(QtCore.QSize(77, 26))
        self.comboBox_f_beat.setObjectName("comboBox_f_beat")
        self.comboBox_f_beat.addItem("")
        self.comboBox_f_beat.addItem("")
        self.comboBox_f_beat.addItem("")
        self.comboBox_f_beat.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_f_beat, 3, 1, 1, 2)
        self.lineEdit_f_srs = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f_srs.setMinimumSize(QtCore.QSize(125, 21))
        self.lineEdit_f_srs.setMaximumSize(QtCore.QSize(125, 21))
        self.lineEdit_f_srs.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_f_srs, 4, 1, 1, 1)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMaximumSize(QtCore.QSize(159, 41))
        self.textEdit.setObjectName("fileName")
        self.gridLayout_2.addWidget(self.textEdit, 5, 1, 1, 1)



        '''
        self.lineEdit_fileName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fileName.setMaximumSize(QtCore.QSize(125, 21))
        self.lineEdit_fileName.setObjectName("fileName")
        self.lineEdit_fileName.setToolTip('fileName')
        self.gridLayout_2.addWidget(self.lineEdit_fileName, 5, 1, 1, 1)

        '''
        self.gridLayout.addLayout(self.gridLayout_2, 0, 3, 1, 1)
        self.tabRel = QtWidgets.QTabWidget(self.centralwidget)
        self.tabRel.setObjectName("tabRel")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabRel.addTab(self.tab, "")
        self.win = pg.GraphicsWindow(parent = self.tab)
        self.win.setGeometry(0, 0, 685, 530)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabRel.addTab(self.tab_2, "")

        #spacerItem = QtWidgets.QSpacerItem(910, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)


        self.win_2 = pg.GraphicsWindow(parent = self.tab_2)
        self.win_2.setGeometry(0, 0, 685, 530)

        self.gridLayout.addWidget(self.tabRel, 0, 0, 1, 1)
        #spacerItem = QtWidgets.QSpacerItem(923, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #self.gridLayout.addItem(spacerItem, 1, 0, 2, 4)
        self.comboBox_f_ceo.raise_()
        self.comboBox_f_beat.raise_()
        self.lineEdit_f_l.raise_()
        self.lineEdit_f_ceo.raise_()
        self.lineEdit_f_rep.raise_()
        self.lineEdit_n.raise_()
        self.lineEdit_f_beat.raise_()
        self.comboBox_f_ceo.raise_()
        self.label_6.raise_()
        self.comboBoxT_int.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.comboBox_f_beat.raise_()
        #self.lineEdit_fileName.raise_()
        self.lineEdit_f_srs.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.label_27.raise_()
        self.checkBox.raise_()
        self.comboBox_f_ceo.raise_()
        self.tabRel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabRel.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_f_beat.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>f_ceo</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">f_ceo</p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">X</p></body></html>"))

        self.radioButton_6.setText(_translate("MainWindow", "+"))
        self.radioButton_8.setText(_translate("MainWindow", "-"))
        self.radioButton_5.setText(_translate("MainWindow", "+"))
        self.radioButton_7.setText(_translate("MainWindow", "-"))


        self.label_23.setText(_translate("MainWindow", "f_l ="))
        self.lineEdit_n.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>f_ceo</p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">f_rep</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">f_beat</p></body></html>"))
        self.lineEdit_f_rep.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>f_ceo</p></body></html>"))
        self.lineEdit_f_ceo.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>f_ceo</p></body></html>"))

        self.label_25.setText(_translate("MainWindow", "="))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">n</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Deviation</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "T_int"))
        self.comboBoxT_int.setToolTip(_translate("MainWindow", "meas interval\n"
""))
        self.comboBoxT_int.setItemText(0, _translate("MainWindow", "1ms"))
        self.comboBoxT_int.setItemText(1, _translate("MainWindow", "100ms"))
        self.comboBoxT_int.setItemText(2, _translate("MainWindow", "1s"))
        self.comboBoxT_int.setItemText(3, _translate("MainWindow", "10s"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">f_ceo</p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">f_beat</p></body></html>"))
        self.comboBox_dev.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>f_ceo channel</p></body></html>"))
        self.comboBox_dev.setItemText(0, _translate("MainWindow", "ADEV"))
        self.comboBox_dev.setItemText(1, _translate("MainWindow", "ODEV"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">f_srs</p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">fileName</p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "Save"))
        self.pushButton.setText(_translate("MainWindow", "New"))
        self.comboBox_f_ceo.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>f_ceo channel</p></body></html>"))
        self.comboBox_f_ceo.setItemText(0, _translate("MainWindow", "ch1"))
        self.comboBox_f_ceo.setItemText(1, _translate("MainWindow", "ch2"))
        self.comboBox_f_ceo.setItemText(2, _translate("MainWindow", "ch3"))
        self.comboBox_f_ceo.setItemText(3, _translate("MainWindow", "ch4"))
        self.comboBox_f_beat.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>f_beat [signal from beatings between laser and comb] channel</p></body></html>"))
        self.comboBox_f_beat.setItemText(0, _translate("MainWindow", "ch1"))
        self.comboBox_f_beat.setItemText(1, _translate("MainWindow", "ch2"))
        self.comboBox_f_beat.setItemText(2, _translate("MainWindow", "ch3"))
        self.comboBox_f_beat.setItemText(3, _translate("MainWindow", "ch4"))
        self.tabRel.setTabText(self.tabRel.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabRel.setTabText(self.tabRel.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

#import a_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
