#Developed by Elementz Engineers Guild Pvt Ltd
from PyQt4 import QtGui
from PyQt4 import QtCore

import GSMUtility, sys
import serial
import serial.tools.list_ports
import time


send_flag = 0
baud_rate = 9600
com_port = None
open_button = 0
portOpen = False
GSM_port = serial.Serial()
Console_Data=''
ScriptData=''
number=''
smsnum=''
sms_body=''
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

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MainGUIClass(QtGui.QMainWindow, GSMUtility.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainGUIClass, self).__init__(parent)
        self.setupUi(self)
        self.Thread = WorkThread()
        QtCore.QObject.connect(self.findButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.port_update)
        QtCore.QObject.connect(self.portComboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.port_select)
        QtCore.QObject.connect(self.baudcomboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.baud_select)
        QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connect_disconnect)
        QtCore.QObject.connect(self.Thread, QtCore.SIGNAL(_fromUtf8("SERIAL_DATA")), self.serial_data)
        QtCore.QObject.connect(self.SendButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_script)
        QtCore.QObject.connect(self.ScriptLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.ScriptText)
        QtCore.QObject.connect(self.Call_Button,  QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallText)
        QtCore.QObject.connect(self.NumberlineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.callno)
        QtCore.QObject.connect(self.Halt_Button,  QtCore.SIGNAL(_fromUtf8("clicked()")), self.end_call)
        QtCore.QObject.connect(self.lineEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.smsno)
        QtCore.QObject.connect(self.plainTextEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.smsbody)
        QtCore.QObject.connect(self.pushButton_4,  QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendfunc)
    def port_update(self):
        try:
          self.portComboBox.clear()
          ports = list(serial.tools.list_ports.comports())
          num_port = len(ports)
          for i in range(num_port):
             self.portComboBox.addItem("")
            # for i in range(num_port):
             self.portComboBox.setItemText(i, ports[i][0])
          self.port_select(ports[0][0])
        except:
           print 'Port Not Found'

    def port_select(self, port):
        GSM_port.close
        global portOpen
        portOpen = False
        GSM_port.port = port
        # print GSM_port.port
        # print type(GSM_port.port)

    def baud_select(self, baud):
        GSM_port.close
        global portOpen
        portOpen = False
        GSM_port.baudrate = baud
        # print GSM_port.baudrate
        # print type(GSM_port.baudrate)

    def connect_disconnect(self):
        global Console_Data
        # global baud_rate
        try:

            global portOpen
            if(portOpen):

                GSM_port.close()
                portOpen=False
                self.connectButton.setText("Connect")
                self.SerialConsole.setPlainText('Port Closed')
            else:

                GSM_port.open()
                portOpen=True
                self.connectButton.setText("Disconnect")
                #self.SerialConsole.setPlainText('Port Opened')
                #GSM_port.write('AT'+"\r\n")
                self.SerialConsole.setPlainText('Port Opened')

        except:
            print "Error:Port may be used by another application"

    # def serial_data(self,data):
    def serial_data(self):
        global Console_Data
        self.SerialConsole.setPlainText(Console_Data)
    def ScriptText(self,data):
        global ScriptData
        ScriptData=data
    def send_script(self):
        global ScriptData
        # try:
        print ScriptData
        GSM_port.write(str(ScriptData)+"\r\n")
        # except:
        #     print "Send Failed"
    def CallText(self):

       global number
       try:
         print number
         GSM_port.write('ATD'+str(number)+';'+"\r\n")
       except:
         print "Call Failed"
    def callno(self,data):
        global number
        number=data
    def end_call(self):
        GSM_port.write('ATH'+"\r\n")
    def smsno(self,data1):
        global smsnum
        smsnum=data1
    def smsbody(self,sms_data):
          sms_data='he has a cat'
          global sms_body
          sms_body=sms_data


    def sendfunc(self):

          global sms_body
          global smsnum
          print sms_body

          # print type(self.plainTextEdit.toPlainText())
          # print (str(self.plainTextEdit.toPlainText()))
          # print type(str(self.plainTextEdit.toPlainText()))
          GSM_port.write('AT+CMGS="'+str(smsnum)+'"'+chr(13))

          time.sleep(2)

          GSM_port.write(str(self.plainTextEdit.toPlainText())+ chr(26))




class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        global portOpen
        while True:
            while portOpen:
                # try:
                    d = GSM_port.read()
                    # sys.stdout.write(d)
                    global Console_Data
                    Console_Data+=d
                    self.emit(QtCore.SIGNAL("SERIAL_DATA"))
                    # self.emit(QtCore.SIGNAL("SERIAL_DATA"),QtCore.QChar()
                    self.emit(QtCore.SIGNAL("SERIAL_DATA"),QtCore.QString(d))
                # except:
                #     print 'nothing'
            # print 'loop'


if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    app = MainGUIClass()
    app.show()
    app.Thread.start()
    sys.exit(a.exec_())

