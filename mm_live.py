## Laser Channel is being set up from the source yet


import pyqtdesignerM
#import liveplt
from pyqtdesignerM import Ui_MainWindow
import allantools
import time
import datetime
import pandas as pd
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
import random
from scipy.ndimage.filters import median_filter,gaussian_filter,uniform_filter
import ctypes
from ctypes import wintypes
import os
from ctypes import *

## Laser Channel is being set up from the source yet




'''
def GetRep():
    rpt = c_char_p(".".encode('ascii'))
    kplusk.FX_GetReport(pointer(rpt))
    data = []
    if rpt.value != None:
        if len(rpt.value) > 30:
            data.append(procLine(rpt.value))
    return data
'''
n_ = 1000000
f_l_ = 0
f_rep_ = 985.500
f_ceo_ = 0
f_beat_ = 0
f_srs = 200
sign_1 = 1
sign_2 = 1
laserCh = 'ch2'
n_save = 10
ch_beat = 'ch2'
#self.m_ui.comboBox_f_ceo.currentText() = 'ch1'






class Window(QMainWindow):


    #kplusk.FX_OpenPort.restype = ctypes.c_long

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.rate_ = 1
        self.OpenPort()

        self.m_ui = Ui_MainWindow()
        self.m_ui.setupUi(self)

        self.m_ui.radioButton_6.setChecked(True)

        self.m_ui.radioButton_6.toggled.connect(self.on_radio_button_toggled_1)
        #self.m_ui.radioButton_8.toggled.connect(self.on_radio_button_toggled_1)

        self.m_ui.radioButton_5.setChecked(True)
        self.m_ui.radioButton_5.toggled.connect(self.on_radio_button_toggled_2)
        #self.m_ui.radioButton_7.toggled.connect(self.on_radio_button_toggled_2)


        self.m_ui.lineEdit_f_rep.returnPressed.connect(self.f_rep)
        self.m_ui.lineEdit_n.returnPressed.connect(self.mode_num)
        self.m_ui.comboBox_f_ceo.setCurrentIndex(0)
        self.m_ui.comboBox_f_ceo.currentTextChanged.connect(self.f_ceo)
        self.m_ui.comboBox_f_beat.setCurrentIndex(1)
        self.m_ui.comboBox_f_beat.currentTextChanged.connect(self.f_beat)
        self.m_ui.comboBoxT_int.currentTextChanged.connect(self.timeint)
        self.m_ui.comboBoxT_int.setCurrentIndex(2)
        self.m_ui.lineEdit_f_srs.setText(str(f_srs))
        self.m_ui.lineEdit_f_srs.returnPressed.connect(self.f_srs)
        self.m_ui.comboBox_dev.setCurrentIndex(0)
        self.m_ui.comboBox_dev.currentTextChanged.connect(self.dev)



        self.m_ui.lineEdit_f_rep.setText(str(f_rep_))
        self.m_ui.lineEdit_n.setText(str(n_))

        self.m_ui.pushButton.clicked.connect(self.butt_new)

        self.m_ui.checkBox.toggled.connect(self.StartSaveData)
        #print(self.m_ui.comboBox_dev.currentText())






        data = np.empty(300)


        p1 = self.m_ui.win.addPlot(rowspan=2)
        p1.setLabel('left', text='Allan deviation abs', units='Hz')
        p1.setLabel('bottom', text='Taus', units='s')
        #p1.setLogMode(True, True)
        p1.showGrid(x=True,y=True,alpha=0.2)
        p1.getAxis('bottom').setLogMode(False)
        p1.getAxis('left').setLogMode(False)




        self.curve1 = p1.plot(data, symbol='o',pen=(55,55,55),
                              symbolPen = None,symbolBrush = (55,55,55),
                              symbolSize=5)
        p1.setDownsampling(mode='mean', auto=True)
        p1.setClipToView(True)
        p11 = self.m_ui.win.addPlot()
        p11.setLabel('left', text='Laser freq', units='Hz')
        p11.setLabel('bottom', text='Taus', units='s')
        p11.showGrid(x=True,y=True,alpha=0.2)


        self.curve11 = p11.plot(data, symbol=None,pen=(55,55,55), symbolPen = None,symbolBrush = (55,55,55), symbolSize=5, name="symbol='star'")
        p11.setDownsampling(mode='mean', auto=True)
        p11.setClipToView(True)
        self.m_ui.win.nextRow()
        p12 = self.m_ui.win.addPlot()
        p12.setLabel('left', text='Laser freq', units='Hz')
        p12.setLabel('bottom', text='Taus', units='s')
        p12.showGrid(x=True,y=True,alpha=0.2)

        self.curve12 = p12.plot(data, symbol=None,pen=(55,55,55),
                                symbolPen = None,symbolBrush = (55,55,55),
                                symbolSize=5)
        p12.setDownsampling(mode='mean', auto=True)
        p12.setClipToView(True)
        p2 = self.m_ui.win_2.addPlot()
        p2.setLabel('left', text='Allan deviation rel', units='unit')
        p2.setLabel('bottom', text='Taus', units='s')
        p2.showGrid(x=True,y=True,alpha=0.2)
        p2.getAxis('left').setLogMode(False)
        p2.getAxis('bottom').setLogMode(False)
        self.curve2 = p2.plot(data, symbol='o',pen=(55,55,55), symbolPen = None,symbolBrush = (55,55,55), symbolSize=5, name="symbol='star'")
        p2.setDownsampling(mode='mean', auto=True)
        p2.setClipToView(True)
        self.Data = pd.DataFrame([])

        #timerCallback = functools.partial(selfupdate, initParams=curve1)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(50)

    def OpenPort(self):
        global kplusk
        kplusk = WinDLL("KK_FX80E")
        kplusk.KK_SetOutputPath(os.curdir)
        s1 = c_char_p("USB: 000000B9".encode('ascii'))
        print(kplusk.FX_OpenPort(pointer(s1)))
        print(s1.value)
        self.SendCommand('E') # frequency from averaged phase advance
        self.SendCommand('4') # ch 1 2 3 4
        self.SendCommand(' ') # 1ms

    def SendCommand(self, command):
        try:
            Comm = c_char_p((command).encode('ascii'))
            SendCommand_ = kplusk.FX_SendCommand(pointer(Comm))
            #print('$'+command)
            if SendCommand_ !=1: print ("Command failed"), SendCommand_
            #else: print("coool")
        except ValueError:
            print('Upsss')



    def procLine(self, line):
         line = str(line)[:-1]
         line = list(filter(lambda x: ('.' in x), line.split(' ')))
         line = [float(i.replace(';', '')) for i in line]
         return line


    def filename(self):
         global f_rep_, n_, f_srs
         fname = str(datetime.datetime.now())[5:-10] + ',rep'+str(f_rep_)+',srs'+str(f_srs)+',n'+str(n_) + 'sgn:'+ str(sign_1)+str(sign_2)+'.txt'
         fname = fname.replace(':', '')

         self.m_ui.textEdit.setText(fname)
         #print(fname)
         return fname
	#data = []

    def GetData(self, filename):
        f = open(filename)
        data = []
        for i in f.readlines():
            data.append(self.procLine(i))
        data = pd.DataFrame(data, columns = ['ch1', 'ch2', 'ch3', 'ch4'])
        return data


    def update(self):
        n_save = 10
        data = 0
        self.m_ui.lineEdit_f_ceo.setText(str(round(f_ceo_,1)))
        self.m_ui.lineEdit_f_beat.setText(str(round(f_beat_,1)))
        self.f_l()
        self.m_ui.lineEdit_f_srs.returnPressed.connect(self.f_srs)
        self.SaveData()
        self.m_ui.lineEdit_f_l.setText(str(round(f_l_,1)))
        try:
             data = self.GetRep()
             chN = self.m_ui.comboBox_f_beat.currentText()
             self.Data = self.Data.append(data)
             '''
             self.allanData(self.Data, self.rate_, 'freq', self.curve1)
             self.allanData(self.Data, self.rate_, 'freq', self.curve2)
             self.laser(self.Data, chN, self.curve11)
             self.laser(self.Data, chN, self.curve12)
             self.f_ceo(self.Data)
             self.f_beat(self.Data)
             '''
        except:
             pass

             #data = self.GetData('180302_1_Frequ.txt')
             #print (data)
             '''
             if len(data)>0 and data:
                  chN = self.m_ui.comboBox_f_beat.currentText()
                  #a = data.iloc[0]
                  self.Data = self.Data.append(data)
                  print(self.Data)


             '''




    def butt_new(self):
         self.Data = pd.DataFrame([])

    def GetRep(self):
         global kplusk
         rpt = c_char_p(".".encode('ascii'))
         kplusk.FX_GetReport(pointer(rpt))
         data = []
         if rpt.value != None:
              if len(rpt.value) > 30:
                    data.append(self.procLine(rpt.value))
         #print (data)
         if np.array(data).shape[1] == 4:
              return pd.DataFrame(data, columns=['ch1', 'ch2', 'ch3', 'ch4'])
         if np.array(data).shape[1] == 3:
              return pd.DataFrame(data, columns=['ch1', 'ch2', 'ch3'])
         if np.array(data).shape[1] == 2:
              return pd.DataFrame(data, columns=['ch1', 'ch2'])
         if np.array(data).shape[1] == 1:
              return pd.DataFrame(data, columns=['ch1'])
         else: print('shit')


    def StartSaveData(self):
        global n_save
        if self.m_ui.checkBox.isChecked():
             self.fname = self.filename()
             self.f = open(self.fname,'w')

    def SaveData(self):
        global n_save
        if self.m_ui.checkBox.isChecked():
            #print('Pressed')
            try:
                #print(np.array(self.Data).shape[0] % n_save)
                if np.array(self.Data).shape[0] % n_save==0:
                    #print(np.array(self.Data).shape)
                    #print(self.Data.iloc[-n_save:].values[:-1])
                    self.f = open(self.fname,'a')
                    #self.Data.iloc[-n_save:][1:].to_csv(self.fname, mode='a')
                    self.f.write(str(self.Data.iloc[-n_save:].values[:-1]).replace(']','').replace('[','')+os.linesep)
                    self.f.close()
            except Exception as e:
                    print(e)

            #print('STOP')


    def timeint(self):
        try:
            if self.m_ui.comboBoxT_int.currentText() == '1ms':
                 #print('1ms')
                 n_save = 100
                 self.SendCommand(' ')
                 self.rate_ = 1000
                 self.Data = pd.DataFrame([])

            if self.m_ui.comboBoxT_int.currentText() == '100ms':
               #print('100ms')
                 n_save = 10
                 self.rate_ = 10
                 self.SendCommand('&')
                 self.Data = pd.DataFrame([])

            if self.m_ui.comboBoxT_int.currentText() == '1s':
                 self.SendCommand(')')
                 n_save = 1
                 self.rate_ = 1
                 self.Data = pd.DataFrame([])

            if self.m_ui.comboBoxT_int.currentText() == '10s':
                 self.SendCommand('-')
                 n_save = 1
                 self.rate_ = 0.1
                 self.Data = pd.DataFrame([])
        except Exception as e:
            print (e)
            pass



    def f_l(self):
         global f_l_, f_rep_, f_ceo_, n_, sign_1, sign_2, f_srs
         f_l_ = n_ * f_rep_ + sign_1 * (f_ceo_-f_srs) + sign_2 * f_beat_
         return f_l_


    def laser(self, data, chN, curve):
         data = data[chN]
         data = np.array(data.iloc[-200:])
         #print(data)
         if curve == self.curve12:
             data = gaussian_filter(data, 50)
         curve.setData(data)

    def allanData(self,data, rate, data_type, curve):
         chN = self.m_ui.comboBox_f_beat.currentText()
         data = np.array(data[chN])
         if curve == self.curve2:
             data = data/np.mean(data)
         #taus=np.logspace(0.0, 3.0, np.array(y).shape[0])
         if self.m_ui.comboBox_dev.currentText()  == 'ADEV':
             (t2, ad, ade, ns) = allantools.adev(data,data_type=data_type, rate=rate)
         if self.m_ui.comboBox_dev.currentText()  == 'ODEV':
             (t2, ad, ade, adn) = allantools.oadev(data,rate=rate,data_type=data_type,taus='octave')

         #ad = [x if x!=0.0 else 0.001 for x in ad]
         #t2 = [x if x!=0.0 else 0.001 for x in t2]
         #print(t2, ad)
         curve.setData(t2, ad)



    def on_radio_button_toggled_1(self):
         global sign_1
         radiobutton_1 = self.sender()
         if radiobutton_1.isChecked():
              sign_1 = 1
              print(sign_1)
         else:
              sign_1 = -1
              print(sign_1)

    def on_radio_button_toggled_2(self):
        global sign_2
        radiobutton = self.sender()

        if radiobutton.isChecked():
            sign_2 = 1
            print(sign_2)

        else:
            sign_2 = -1
            print(sign_2)



    def f_rep(self):
        global f_rep_
        f_rep_ = float(self.m_ui.lineEdit_f_rep.text())
        self.m_ui.lineEdit_f_rep.setText(str(f_rep_))

    def f_srs(self):
        global f_srs
        f_srs = float(self.m_ui.lineEdit_f_srs.text())
        #print(f_srs)
        self.m_ui.lineEdit_f_srs.setText(str(f_srs))


    def mode_num(self):
        global n_
        n_ = float(self.m_ui.lineEdit_n.text())
        self.m_ui.lineEdit_n.setText(str(n_))


    def f_ceo(self, data):
        global f_ceo_
        chN = self.m_ui.comboBox_f_ceo.currentText()
        try:
            f_ceo_ = float(data[chN][-1:])
            self.m_ui.lineEdit_4.setText(str(f_ceo_))

        except:
            pass

    def f_beat(self, data):
        global f_beat_
        chN = self.m_ui.comboBox_f_beat.currentText()
        try:
            f_beat_ = float(data[chN][-1:])

        except:
            pass


    def dev(self):
        global dev
        dev = self.m_ui.comboBox_dev.currentText()
#    @pyqtSlot()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
