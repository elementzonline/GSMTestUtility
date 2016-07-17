from PyQt4 import QtGui
from PyQt4 import QtCore

import GSMUtility, sys
import Call_form, sys
import sys
import linecache
import serial
import serial.tools.list_ports
import time
import StringIO


com_port_selection = ''
send_flag = 0
baud_rate = 9600
com_port = None
open_button = 0
portOpen = False
GSM_port = serial.Serial()
Console_Data = ''
ScriptData = ''
number = ''
smsnum = ''
c = 0
read_data = ''
apn = ''
server_ip = ''
port_no = ''
tcp_data = ''
source_address = ''
get_post = ''
tu_veriable = ''
ftp_server_name = ''
user_name = ''
ftp_password = ''
ftp_file_name = ''
ftp_directry = ''
incoming_call = False
count2=''
ftp_put_data=''
count3=''
count4=''

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


class DialogClass(QtGui.QDialog, Call_form.Ui_Dialog):
    def __init__(self, parent=None):
        super(DialogClass, self).__init__(parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Attend_Call)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Decline)
    def Attend_Call(self):
        GSM_port.write('ATA' + "\r\n")

    def Decline(self):
        global Console_Data
        global c
        global incoming_call
        GSM_port.write('ATH' + "\r\n")
        self.close()


class MainGUIClass(QtGui.QMainWindow, GSMUtility.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainGUIClass, self).__init__(parent)
        self.setupUi(self)
        self.Thread1 = WorkThread()
        QtCore.QObject.connect(self.findButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.port_update)
        QtCore.QObject.connect(self.portComboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.port_select)
        QtCore.QObject.connect(self.baudcomboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.baud_select)
        QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connect_disconnect)
        QtCore.QObject.connect(self.Thread1, QtCore.SIGNAL(_fromUtf8("SERIAL_DATA")), self.serial_data)
        QtCore.QObject.connect(self.Thread1, QtCore.SIGNAL(_fromUtf8("SERIAL_DATA")), self.Delete_Dialog)
        QtCore.QObject.connect(self.Thread1, QtCore.SIGNAL(_fromUtf8("INCOMING_CALL")), self.showno)
        QtCore.QObject.connect(self.Thread1, QtCore.SIGNAL(_fromUtf8("SERIAL_DATA")), self.print_http_get)
        QtCore.QObject.connect(self.Thread1, QtCore.SIGNAL(_fromUtf8("SERIAL_DATA")), self.on_off)
        QtCore.QObject.connect(self.SendButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_script)
        QtCore.QObject.connect(self.ScriptLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.ScriptText)
        QtCore.QObject.connect(self.Call_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallText)
        QtCore.QObject.connect(self.NumberlineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.callno)
        QtCore.QObject.connect(self.Halt_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.end_call)
        QtCore.QObject.connect(self.lineEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.smsno)
        QtCore.QObject.connect(self.plainTextEdit, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.smsbody)
        QtCore.QObject.connect(self.plainTextEdit_7, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.smsbody_second)
        QtCore.QObject.connect(self.plainTextEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.http_smsbody_second)
        QtCore.QObject.connect(self.plainTextEdit_4, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.ftp_smsbody_third)


        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendfunc)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.get_apn)
        QtCore.QObject.connect(self.lineEdit_4, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.get_ip)
        QtCore.QObject.connect(self.lineEdit_5, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.get_port)
        QtCore.QObject.connect(self.plainTextEdit_7, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.send_data)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connect_gprs)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.disconnect_gprs)
        QtCore.QObject.connect(self.pushButton_25, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_button)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clear_log)
        QtCore.QObject.connect(self.plainTextEdit_2, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.source_add)
        QtCore.QObject.connect(self.plainTextEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.get_data)
        QtCore.QObject.connect(self.plainTextEdit_4, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.FTP_data)
        QtCore.QObject.connect(self.plainTextEdit_7, QtCore.SIGNAL(_fromUtf8("textChanged()")), self.tcp_udp_data)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_fun)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.post_fun)
        QtCore.QObject.connect(self.lineEdit_16, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.http_apn)
        QtCore.QObject.connect(self.pushButton_26, QtCore.SIGNAL(_fromUtf8("clicked()")), self.session_close)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.tcp_udp)
        QtCore.QObject.connect(self.lineEdit_6, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.ftp_server)
        QtCore.QObject.connect(self.lineEdit_7, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.username)
        QtCore.QObject.connect(self.lineEdit_8, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.password)
        QtCore.QObject.connect(self.lineEdit_9, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.file_name)
        QtCore.QObject.connect(self.lineEdit_10, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.directry)
        QtCore.QObject.connect(self.lineEdit_11, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.ftp_apn)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ftp_push)
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ftp_get)
        QtCore.QObject.connect(self.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ftp_connect)
        QtCore.QObject.connect(self.pushButton_12, QtCore.SIGNAL(_fromUtf8("clicked()")), self.ftp_disconnect)

    def port_update(self):
        try:
            self.portComboBox.clear()
            initial = 'Select'
            ports = list(serial.tools.list_ports.comports())
            ports = [initial] + ports
            num_port = len(ports)
            for i in range(num_port):
                self.portComboBox.addItem("")
                if i == 0:
                    self.portComboBox.setItemText(i, ports[i])
                else:
                    self.portComboBox.setItemText(i, ports[i][0])
        except:
            self.SerialConsole.setPlainText('Port Not Found')

    def port_select(self, local_var):
        global com_port_selection
        GSM_port.close
        global portOpen
        portOpen = False
        com_port_selection = local_var

    def baud_select(self, baud):
        GSM_port.close
        global portOpen
        portOpen = False
        GSM_port.baudrate = baud

    def connect_disconnect(self):
          global Console_Data

          try:

            global portOpen
            if (portOpen):

                GSM_port.close()
                portOpen = False
                self.connectButton.setText("Connect")
                Console_Data = 'Port Closed'
                self.SerialConsole.setPlainText('Port Closed')
                self.findButton.setEnabled(True)
                self.portComboBox.setEnabled(True)
            else:
                GSM_port.port = str(com_port_selection)
                GSM_port.open()
                GSM_port.open()
                portOpen = True
                self.connectButton.setText("Disconnect")
                Console_Data = 'Port Opened'
                GSM_port.write('AT' + "\r\n")
                self.findButton.setEnabled(False)
                self.portComboBox.setEnabled(False)


          except:
             self.SerialConsole.setPlainText('Port May be Used By Another Application')

    def serial_data(self):
        global Console_Data
        global read_data
        with open('temp.txt', 'w') as FileHandle:
            FileHandle.write(read_data)
        self.SerialConsole.setPlainText(Console_Data)
        self.SerialConsole.verticalScrollBar().setSliderPosition(self.SerialConsole.verticalScrollBar().maximum());

    def ScriptText(self, data):
        global ScriptData
        ScriptData = data
        if ScriptData=='':
             self.SendButton.setEnabled(False)
        else:
             self.SendButton.setEnabled(True)


    def send_script(self):
        global ScriptData
        try:
           GSM_port.write(str(ScriptData) + "\r\n")
        except:
           self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1)Findport->select port.\n 2)select baud rate according to ur hardware->Connect')

    def callno(self, data):
        global number
        number = data
        if number=='':
             self.Call_Button.setEnabled(False)
        else:
             self.Call_Button.setEnabled(True)

    def CallText(self):
        global number
        try:
           GSM_port.write('ATD' + str(number) + ';' + "\r\n")
        except:
            self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1)Findport->select port.\n 2)select baud rate according to ur hardware->Connect')


    def end_call(self):
        try:
          GSM_port.write('ATH' + "\r\n")
        except:
            self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1)Findport->select port.\n 2)select baud rate according to ur hardware->Connect')

    def smsno(self, data1):

          global smsnum
          smsnum = data1
          if smsnum=='':
             self.pushButton_4.setEnabled(False)
          else:
             self.pushButton_4.setEnabled(True)



    def smsbody(self):

        count=len(self.plainTextEdit.toPlainText())
        self.lineEdit.setText(str(count))


    def sendfunc(self):

        global smsnum
        try:
           GSM_port.write('AT+CMGS="' + str(smsnum) + '"' + chr(13))
           time.sleep(2)
           GSM_port.write(str(self.plainTextEdit.toPlainText()) + chr(26))
        except:
            self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1)Findport->select port.\n 2)select baud rate according to ur hardware->Connect')

    def showno(self):
        global c
        global Console_Data
        global incoming_call

        if c != 0:
            local_var = ''
            local_var += Console_Data[c + 1:c + 13]
            if len(local_var) == 10:

                app2.numberLineedit.setText(str(Console_Data[c:c + 13]))
                incoming_call = True
                app2.exec_()
                incoming_call = False

    def Delete_Dialog(self):
        # global Console_Data
        global read_data

        local2 = 0
        local2 = read_data.rfind('NO CARRIER')
        if local2 >=0:
            read_data = ''
            local2 = 0
            app2.close()


    def get_apn(self, data2):
        global apn
        apn = data2
        global tu_veriable
        global server_ip
        global port_no
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '':
           self.pushButton_8.setEnabled(False)

        else:
             self.pushButton_8.setEnabled(True)
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '' or self.plainTextEdit_7.toPlainText()== '':
           self.pushButton_25.setEnabled(False)

        else:
             self.pushButton_25.setEnabled(True)

    def get_ip(self, data3):
        global server_ip
        server_ip = data3
        global tu_veriable
        global apn
        global port_no
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '':
           self.pushButton_8.setEnabled(False)

        else:
             self.pushButton_8.setEnabled(True)
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '' or self.plainTextEdit_7.toPlainText()== '':
           self.pushButton_25.setEnabled(False)

        else:
             self.pushButton_25.setEnabled(True)


    def get_port(self, data4):
        global port_no
        port_no = data4
        global tu_veriable
        global apn
        global server_ip
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '':
           self.pushButton_8.setEnabled(False)

        else:
             self.pushButton_8.setEnabled(True)
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '' or self.plainTextEdit_7.toPlainText()== '':
           self.pushButton_25.setEnabled(False)

        else:
             self.pushButton_25.setEnabled(True)

    def tcp_udp_data(self):
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '' or self.plainTextEdit_7.toPlainText()== '':
           self.pushButton_25.setEnabled(False)

        else:
             self.pushButton_25.setEnabled(True)

    def connect_gprs(self):
        try:
           global apn
           global server_ip
           global port_no
           global tu_veriable
           if tu_veriable == 'TCP':
              Console_Data = 'Please Wait Device is Getting Connected...\n'
              GSM_port.write('AT+CIPMUX=0' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+CSTT=' + '"' + str(apn) + '"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+CIICR' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+CIFSR' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+CIPSTART="TCP"' + ',''"' + str(server_ip) + '"' + ',''"' + str(port_no) + '"' + chr(13))

           elif tu_veriable == 'UDP':
              Console_Data = 'Please Wait Device is Getting Connected...\n'
              GSM_port.write('AT+CGATT?' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+CSTT=' + '"' + str(apn) + '"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+CIICR' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+CIFSR' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+CIPSTART="UDP"' + ',''"' + str(server_ip) + '"' + ',''"' + str(port_no) + '"' + chr(13))

        except:
            self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1) Findport->select port.\n 2)select baud rate according to ur hardware->Connect')


    def send_data(self, data5):
        global tcp_data
        tcp_data = data5

    def smsbody_second(self):
        global count2
        count2 = len(self.plainTextEdit_7.toPlainText())


    def http_smsbody_second(self):
        global count3
        count3 = len(self.plainTextEdit_3.toPlainText())

    def send_button(self):
        global tcp_data
        global tu_veriable
        global count2
        try:
          GSM_port.write('AT+CIPSEND='+str(count2) + chr(13))
          time.sleep(1)
          GSM_port.write(str(self.plainTextEdit_7.toPlainText()) + chr(26))
        except:
            self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1)Findport->select port.\n 2)select baud rate according to ur hardware->Connect')

    def source_add(self):
        global apn
        if apn == '' or self.plainTextEdit_2.toPlainText() == '':
            self.pushButton_3.setEnabled(False)
        else:
            self.pushButton_3.setEnabled(True)
        if apn == '' or self.plainTextEdit_2.toPlainText() == '' or   self.plainTextEdit_3.toPlainText()== '':
            self.pushButton_5.setEnabled(False)
        else:
            self.pushButton_5.setEnabled(True)


    def get_data(self):
        global apn
        if apn == '' or self.plainTextEdit_2.toPlainText() == '' or   self.plainTextEdit_3.toPlainText()== '':
            self.pushButton_5.setEnabled(False)
        else:
            self.pushButton_5.setEnabled(True)

    def http_apn(self, data8):
        global apn
        apn = data8
        if apn == '' or self.plainTextEdit_2.toPlainText() == '':
            self.pushButton_3.setEnabled(False)
        else:
            self.pushButton_3.setEnabled(True)
        if apn == '' or self.plainTextEdit_2.toPlainText() == '' or   self.plainTextEdit_4.toPlainText()== '':
            self.pushButton_5.setEnabled(False)
        else:
            self.pushButton_5.setEnabled(True)


    def get_fun(self):
        global read_data

        global source_address
        global get_post
        global apn
        try:
              GSM_port.write('AT+SAPBR=3,1,"Contype","GPRS"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+SAPBR=3,1,"APN",' + '"' + str(apn) + '"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+SAPBR=1,1' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+SAPBR=2,1' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+HTTPINIT' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+HTTPPARA="CID",1' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+HTTPPARA="URL",' + '"' + str(self.plainTextEdit_2.toPlainText()) + '"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+HTTPACTION=0' + chr(13))
              time.sleep(10)
              GSM_port.write('AT+HTTPREAD' + chr(13))


        except:
            self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1)Findport->select port.\n 2)select baud rate according to ur hardware->Connect')

    def print_http_get(self):
        global read_data
        x1 = 0
        x2=0
        x3 = 0
        x1 = read_data.rfind('OK')
        x2= read_data.rfind('+HTTPREAD:')
        with open('temp.txt', 'w') as FileHandle:
            FileHandle.write(read_data)
        with open("temp.txt", "r") as f:
            for line in f:
                if line.startswith('+HTTPREAD:'):
                    x3 = line.split(':')
                    x4=len(str(x3[1]))
                    if x1>0 and x2>0 and x1>x2:

                       self.plainTextEdit_3.setPlainText(str(read_data[x2 +10+x4:x1-1]).replace('<br/>','\n'))
                       x1=0
                       x2=0
                       read_data = ''


    def post_fun(self):

       try:
          global count3
          GSM_port.write('AT+SAPBR=3,1,"Contype","GPRS"' + chr(13))
          time.sleep(1)
          GSM_port.write('AT+SAPBR=3,1,"APN",' + '"' + str(apn) + '"' + chr(13))
          time.sleep(1)
          GSM_port.write('AT+SAPBR=1,1' + chr(13))
          time.sleep(1)
          GSM_port.write('AT+SAPBR=2,1' + chr(13))
          time.sleep(1)
          GSM_port.write('AT+HTTPINIT' + chr(13))
          time.sleep(1)
          GSM_port.write('AT+HTTPPARA="CID",1' + chr(13))
          time.sleep(1)
          GSM_port.write('AT+HTTPPARA="URL",' +'"'+str(self.plainTextEdit_2.toPlainText())+'"' + chr(13))
          time.sleep(1)
          GSM_port.write('AT+HTTPPARA="CONTENT",' + '"'+str(self.plainTextEdit_3.toPlainText())+'"' + chr(13))
          time.sleep(1)
          GSM_port.write('AT+HTTPDATA='+str(count3)+',10000' + chr(13))
          time.sleep(1)
          GSM_port.write('AT+HTTPACTION=1' + chr(13))
          time.sleep(10)
       except:
           self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1)Findport->select port.\n 2)select baud rate according to ur hardware->Connect')

    def session_close(self):
        try:
           GSM_port.write('AT+HTTPTERM' + chr(13))
        except:
            self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1)Findport->select port.\n 2)select baud rate according to ur hardware->Connect')

    def disconnect_gprs(self):
      try:
         GSM_port.write('AT+CIPSHUT' + chr(13))
      except:
           self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1)Findport->select port.\n 2)select baud rate according to ur hardware->Connect')


    def clear_log(self):
        global Console_Data
        Console_Data = ''
        self.SerialConsole.setPlainText(Console_Data)

    def tcp_udp(self, local1):
        global tu_veriable
        global apn
        global server_ip
        global port_no
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '':
           self.pushButton_8.setEnabled(False)

        else:
             self.pushButton_8.setEnabled(True)
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '' or self.plainTextEdit_7.toPlainText()== '':
           self.pushButton_25.setEnabled(False)

        else:
             self.pushButton_25.setEnabled(True)
        tu_veriable = local1
        if local1 == 'TCP':
            self.pushButton_8.setText("Connect TCP")
        elif local1 == 'UDP':
            self.pushButton_8.setText("Connect UDP")
        elif local1 == 'Select':
            var = self.pushButton_8
            var.setEnabled(False)
            self.pushButton_8.setText("Connect")

    def ftp_server(self, data6):
        global ftp_server_name
        ftp_server_name = data6
        global user_name
        global apn
        global user_name
        global ftp_file_name
        global ftp_directry
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '':
           self.pushButton_11.setEnabled(False)
        else:
              self.pushButton_11.setEnabled(True)
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '':
              self.pushButton_10.setEnabled(False)
        else:
              self.pushButton_10.setEnabled(True)
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '' or self.plainTextEdit_4.toPlainText()== '':
              self.pushButton_9.setEnabled(False)
        else:
              self.pushButton_9.setEnabled(True)


    def username(self, data7):
        global user_name
        user_name = data7
        global ftp_server_name
        global apn
        global ftp_password
        global ftp_file_name
        global ftp_directry
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '':
           self.pushButton_11.setEnabled(False)
        else:
              self.pushButton_11.setEnabled(True)
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '':

              self.pushButton_10.setEnabled(False)
        else:
              self.pushButton_10.setEnabled(True)
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '' or self.plainTextEdit_4.toPlainText()== '':
              self.pushButton_9.setEnabled(False)
        else:
              self.pushButton_9.setEnabled(True)


    def password(self, data8):
        global ftp_password
        ftp_password = data8
        global ftp_server_name
        global apn
        global user_name
        global ftp_file_name
        global ftp_directry
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '':
           self.pushButton_11.setEnabled(False)
        else:
              self.pushButton_11.setEnabled(True)
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '':
              self.pushButton_10.setEnabled(False)
        else:
              self.pushButton_10.setEnabled(True)
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '' or self.plainTextEdit_4.toPlainText()== '':
              self.pushButton_9.setEnabled(False)
        else:
              self.pushButton_9.setEnabled(True)


    def file_name(self, data9):
        global ftp_file_name
        ftp_file_name = data9
        global ftp_server_name
        global apn
        global user_name
        global ftp_password
        global ftp_directry

        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '':
              self.pushButton_10.setEnabled(False)
        else:
              self.pushButton_10.setEnabled(True)
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '' or self.plainTextEdit_4.toPlainText()== '':
              self.pushButton_9.setEnabled(False)
        else:
              self.pushButton_9.setEnabled(True)



    def directry(self, data10):
        global ftp_directry
        ftp_directry = data10
        global ftp_server_name
        global apn
        global user_name
        global ftp_password
        global ftp_file_name

        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '':
              self.pushButton_10.setEnabled(False)
        else:
              self.pushButton_10.setEnabled(True)
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '' or self.plainTextEdit_4.toPlainText()== '':
              self.pushButton_9.setEnabled(False)
        else:
              self.pushButton_9.setEnabled(True)


    def ftp_apn(self, data11):
        global apn
        apn = data11

    def FTP_data(self):
         if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '' or self.plainTextEdit_4.toPlainText()== '':
              self.pushButton_9.setEnabled(False)
         else:
              self.pushButton_9.setEnabled(True)

    def ftp_smsbody_third(self):
        global count4
        count4 = len(self.plainTextEdit_4.toPlainText())


    def ftp_connect(self):
        global apn
        global ftp_server_name
        global user_name
        global ftp_password

        try:
              GSM_port.write('AT+SAPBR=3,1,"Contype","GPRS"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+SAPBR=3,1,"APN","' + str(apn) + '"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+SAPBR =1,1' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+SAPBR=2,1' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+FTPCID=1' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+FTPSERV="' + str(ftp_server_name) + '"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+FTPUN="' + str(user_name) + '"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+FTPPW="' + str(ftp_password) + '"' + chr(13))
        except:
             self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1) Findport->select port.\n 2)select baud rate according to ur hardware->Connect')


    def ftp_disconnect(self):
        try:
              GSM_port.write('AT+FTPPUT=2,0' + chr(13))
        except:
             self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1) Findport->select port.\n 2)select baud rate according to ur hardware->Connect')


    def ftp_push(self):

        global ftp_file_name
        global ftp_directry
        try:
              GSM_port.write('AT+FTPPUTNAME="' + str(ftp_file_name) + '"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+FTPPUTPATH="' + str(ftp_directry) + '"' + chr(13))
              time.sleep(1)
              GSM_port.write('AT+FTPPUT=1' + chr(13))
              time.sleep(10)
              GSM_port.write('AT+FTPPUT=2,'+str(count4) + chr(13))
              time.sleep(1)
              GSM_port.write(str(self.plainTextEdit_4.toPlainText()) + chr(13))
              time.sleep(10)
              GSM_port.write('AT+FTPPUT=2,0' + chr(13))
        except:
             self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1) Findport->select port.\n 2)select baud rate according to ur hardware->Connect')

    def ftp_get(self):
        global ftp_file_name
        global ftp_directry

        try:
             GSM_port.write('AT+FTPGETNAME="' + str(ftp_file_name) + '"' + chr(13))
             time.sleep(1)
             GSM_port.write('AT+FTPGETPATH="' + str(ftp_directry) + '"' + chr(13))
             time.sleep(1)
             GSM_port.write('AT+FTPGET=1' + chr(13))
             time.sleep(10)
             GSM_port.write('AT+FTPGET=2,1024' + chr(13))

        except:
             self.SerialConsole.setPlainText('Please Connect The Hardware.\n 1) Findport->select port.\n 2)select baud rate according to ur hardware->Connect')

    def on_off(self):
        global smsnum
        global number
        global ScriptData
        global tu_veriable
        global apn
        global server_ip
        global port_no
        global ftp_server_name
        global user_name
        global ftp_password
        global ftp_directry
        global ftp_file_name
        if smsnum=='':
            self.pushButton_4.setEnabled(False)
        else:
            self.pushButton_4.setEnabled(True)
        if number=='':
             self.Call_Button.setEnabled(False)
        else:
             self.Call_Button.setEnabled(True)
        if ScriptData=='':
             self.SendButton.setEnabled(False)
        else:
             self.SendButton.setEnabled(True)
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '':
           self.pushButton_8.setEnabled(False)

        else:
             self.pushButton_8.setEnabled(True)
        if tu_veriable == '' or apn == '' or server_ip == '' or port_no == '' or self.plainTextEdit_7.toPlainText()== '':
           self.pushButton_25.setEnabled(False)

        else:
             self.pushButton_25.setEnabled(True)

        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '':
              self.pushButton_11.setEnabled(False)
        else:
              self.pushButton_11.setEnabled(True)

        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '':
              self.pushButton_10.setEnabled(False)
        else:
              self.pushButton_10.setEnabled(True)
        if ftp_server_name == '' or apn == '' or  user_name == '' or ftp_password == '' or ftp_file_name == '' or ftp_directry == '' or self.plainTextEdit_4.toPlainText()== '':
              self.pushButton_9.setEnabled(False)
        else:
              self.pushButton_9.setEnabled(True)
        if apn == '' or self.plainTextEdit_2.toPlainText()==  '':
            self.pushButton_3.setEnabled(False)
        else:
            self.pushButton_3.setEnabled(True)
        if apn == '' or self.plainTextEdit_2.toPlainText()== '' or   self.plainTextEdit_3.toPlainText()== '':
            self.pushButton_5.setEnabled(False)
        else:
            self.pushButton_5.setEnabled(True)

class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        global portOpen
        global incoming_call
        global read_data

        while True:
            while portOpen:
                global c
                d = GSM_port.read()
                global Console_Data
                Console_Data += d
                read_data+=d
                if incoming_call == False:
                    if ('+CLIP' in Console_Data):
                        c = Console_Data.rfind('+CLIP:')

                        c += 8
                    self.emit(QtCore.SIGNAL("INCOMING_CALL"))
                self.emit(QtCore.SIGNAL("SERIAL_DATA"))


if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    app = MainGUIClass()
    app.show()
    app2 = DialogClass()
    app.Thread1.start()
    sys.exit(a.exec_())
