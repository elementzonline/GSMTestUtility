from PyQt4 import QtGui
from PyQt4 import QtCore

import GSMUtility, sys
import sys
import linecache
import serial
import serial.tools.list_ports
import time
import StringIO

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
sms_body = ''
c = 0
apn = ''
server_ip = ''
port_no = ''
tcp_data = ''
source_address = ''
get_post = ''
tu_veriable=''
ftp_server_name=''
user_name=''
ftp_password=''
ftp_file_name=''
ftp_directry=''
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
        self.Thread1 = WorkThread()
        QtCore.QObject.connect(self.findButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.port_update)
        QtCore.QObject.connect(self.portComboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.port_select)
        QtCore.QObject.connect(self.baudcomboBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), self.baud_select)
        QtCore.QObject.connect(self.connectButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connect_disconnect)
        QtCore.QObject.connect(self.Thread1, QtCore.SIGNAL(_fromUtf8("SERIAL_DATA")), self.serial_data)
        QtCore.QObject.connect(self.Thread1, QtCore.SIGNAL(_fromUtf8("SERIAL_DATA")), self.showno)
        QtCore.QObject.connect(self.SendButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_script)
        QtCore.QObject.connect(self.ScriptLineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.ScriptText)
        QtCore.QObject.connect(self.Call_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CallText)
        QtCore.QObject.connect(self.NumberlineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.callno)
        QtCore.QObject.connect(self.Halt_Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.end_call)
        QtCore.QObject.connect(self.lineEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.smsno)
        QtCore.QObject.connect(self.plainTextEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.smsbody)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sendfunc)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.accept_call)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.decline)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.get_apn)
        QtCore.QObject.connect(self.lineEdit_4, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.get_ip)
        QtCore.QObject.connect(self.lineEdit_5, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.get_port)
        QtCore.QObject.connect(self.plainTextEdit_7, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.send_data)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connect_gprs)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.disconnect_gprs)
        QtCore.QObject.connect(self.pushButton_25, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_button)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clear_log)
        QtCore.QObject.connect(self.plainTextEdit_2, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.source_add)
        QtCore.QObject.connect(self.plainTextEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.get_data)
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
            ports = list(serial.tools.list_ports.comports())
            num_port = len(ports)
            for i in range(num_port):
                self.portComboBox.addItem("")
                # for i in range(num_port):
                self.portComboBox.setItemText(i, ports[i][0])
            self.port_select(ports[0][0])
        except:
             self.SerialConsole.setPlainText('Port Not Found')

    def port_select(self, port):
        GSM_port.close
        global portOpen
        portOpen = False
        GSM_port.port = port

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
            else:

                GSM_port.open()
                portOpen = True
                self.connectButton.setText("Disconnect")
                Console_Data = 'Port Opened'
                GSM_port.write("\n" + 'AT' + "\r\n")
                # self.SerialConsole.setPlainText('Port Opened')

        except:
             self.SerialConsole.setPlainText('Port May be Used By Another Application')


    def serial_data(self):
        global Console_Data
        self.SerialConsole.setPlainText(Console_Data)

    def ScriptText(self, data):
        global ScriptData
        ScriptData = data

    def send_script(self):
        global ScriptData
        GSM_port.write(str(ScriptData) + "\r\n")

    def callno(self, data):
        global number
        number = data

    def CallText(self):
          global number
          GSM_port.write('ATD' + str(number) + ';' + "\r\n")




    def end_call(self):
        GSM_port.write('ATH' + "\r\n")


    def smsno(self, data1):
        global smsnum
        smsnum = data1

    def smsbody(self, sms_data):

        global sms_body
        sms_body = sms_data

    def sendfunc(self):

        global sms_body
        global smsnum
        GSM_port.write('AT+CMGS="' + str(smsnum) + '"' + chr(13))
        time.sleep(2)
        GSM_port.write(str(self.plainTextEdit.toPlainText()) + chr(26))

    def accept_call(self):
        GSM_port.write('ATA' + chr(13))

    def decline(self):
        GSM_port.write('ATH' + chr(13))

    def showno(self):
      global c
      global Console_Data
      if c!=0 :
        self.lineEdit.setText(str(Console_Data[c:c+13]))
        if Console_Data[c+31:c+41]=='NO CARRIER' or Console_Data[c+29:c+32]=='ADH':
             self.lineEdit.setText('')

    def get_apn(self,data2):
        global apn
        apn = data2

    def get_ip(self,data3):
        global server_ip
        server_ip=data3

    def get_port(self,data4):
        global port_no
        port_no=data4


    def connect_gprs(self,data5):
         global apn
         global server_ip
         global port_no
         global tu_veriable
         tu_veriable=data5
         # try:
         if tu_veriable=='TCP':
             Console_Data='Please Wait Device is Getting Connected...\n'
             GSM_port.write('AT+CIPMUX=0'+ chr(13))
             time.sleep(1)
             GSM_port.write('AT+CSTT='+'"'+str(apn)+'"' + chr(13))
             time.sleep(1)
             GSM_port.write('AT+CIICR'+ chr(13))
             time.sleep(1)
             GSM_port.write('AT+CIFSR'+ chr(13))
             time.sleep(1)
             GSM_port.write('AT+CIPSTART="TCP"'+',''"'+str(server_ip)+'"'+',''"'+str(port_no)+'"'+chr(13))

         elif tu_veriable=='UDP':
             Console_Data='Please Wait Device is Getting Connected...\n'
             GSM_port.write('AT+CGATT?'+ chr(13))
             time.sleep(1)
             GSM_port.write('AT+CSTT='+'"'+str(apn)+'"' + chr(13))
             time.sleep(1)
             GSM_port.write('AT+CIICR'+ chr(13))
             time.sleep(1)
             GSM_port.write('AT+CIFSR'+ chr(13))
             time.sleep(1)
             GSM_port.write('AT+CIPSTART="UDP"'+',''"'+str(server_ip)+'"'+',''"'+str(port_no)+'"'+chr(13))

         # except:
         #     Console_Data='Please Select either TCP or UDP from the Drop Down Menu'
         #     self.SerialConsole.setPlainText(Console_Data)


    def send_data(self,data5):
        global tcp_data
        tcp_data=data5

    def send_button(self):
        global tcp_data
        global tu_veriable
        GSM_port.write('AT+CIPSEND'+ chr(13))
        time.sleep(1)
        GSM_port.write(str(self.plainTextEdit_7.toPlainText()) + chr(26))

    def source_add(self,data6):
        global source_address
        source_address=data6

    def get_data(self,data7):
        global get_post
        get_post=data7

    def http_apn(self,data8):
        global apn
        apn=data8

    def get_fun(self):
        global source_address
        global get_post
        global new_apn
        GSM_port.write('AT+SAPBR=3,1,"Contype","GPRS"'+chr(13))
        # time.sleep(1)
        GSM_port.write('AT+SAPBR=3,1,"APN",'+'"'+str(new_apn)+'"'+chr(13))
        # time.sleep(1)
        GSM_port.write('AT+SAPBR=1,1'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+SAPBR=2,1'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+SAPBR=0,1'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+HTTPINIT'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+HTTPPARA="CID",1'+chr(13))
        # time.sleep(1)
        GSM_port.write('AT+HTTPPARA="URL",'+'"'+str(self.plainTextEdit_2.toPlainText())+'"'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+HTTPACTION=0'+chr(13))
        # time.sleep(1)
        # # GSM_port.write('AT+HTTPDATA'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+HTTPREAD'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+HTTTERM'+chr(13))


    def post_fun(self):

        GSM_port.write('AT+HTTPINIT'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+HTTPPARA="CID",1'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+HTTPPARA="URL",'+'"'+str(self.plainTextEdit_2.toPlainText())+'"'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+HTTDATA=100,10000'+chr(13))
        time.sleep(1)
        GSM_port.write('AT+HTTPACTION=1'+chr(13))
        time.sleep(1)

    def session_close(self):
        GSM_port.write('AT+HTTPTERM'+chr(13))


    def disconnect_gprs(self):
        # global tu_veriable
        # if tu_veriable=='TCP':
            GSM_port.write('AT+CIPSHUT'+chr(13))
        # elif tu_veriable=='UDP':
        #     GSM_port.write('AT+CIPCLOSE'+chr(13))


    def clear_log(self):
        global Console_Data
        Console_Data=''
        self.SerialConsole.setPlainText(Console_Data)

    def tcp_udp(self,local1):
        global tu_veriable
        global portOpen
        tu_veriable=local1

        if local1=='TCP':
           self.pushButton_8.setText("Connect TCP")
        elif local1=='UDP':
           self.pushButton_8.setText("Connect UDP")
        elif local1=='Select':
            self.pushButton_8.setEnabled(False)
            self.pushButton_8.setText("Connect")

    def ftp_server(self,data6):
        global ftp_server_name
        ftp_server_name=data6

    def username(self,data7):
        global user_name
        user_name=data7

    def password(self,data8):
        global ftp_password
        ftp_password=data8

    def file_name(self,data9):
        global ftp_file_name
        ftp_file_name=data9

    def directry(self,data10):
        global ftp_directry
        ftp_directry=data10

    def ftp_apn(self,data11):
        global apn
        apn=data11

    def ftp_connect(self):
        global apn
        global ftp_server_name
        global user_name
        global ftp_password
        GSM_port.write('AT+SAPBR=3,1,"Contype","GPRS"' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+SAPBR=3,1,"APN","'+str(apn)+'"' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+SAPBR =1,1' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+SAPBR=2,1' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPCID=1' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPSERV="'+str(ftp_server_name)+'"' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPUN="'+str(user_name)+'"' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPPW="'+str(ftp_password)+'"' + chr(13))
    def ftp_disconnect(self):
        GSM_port.write('AT+FTPPUT=2,0' + chr(13))


    def ftp_push(self):

        global ftp_file_name
        global ftp_directry
        GSM_port.write('AT+FTPPUTNAME="'+str(ftp_file_name)+'"' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPPUTPATH="'+str(ftp_directry)+'"' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPPUT=1' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPPUT=2,10' + chr(13))
        time.sleep(1)
        GSM_port.write(str(self.plainTextEdit_4.toPlainText()) + chr(13))



    def ftp_get(self):
        global ftp_file_name
        global ftp_directry
        GSM_port.write('AT+FTPGETNAME="'+str(ftp_file_name)+'"' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPGETPATH="'+str(ftp_directry)+'"' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPGET=1' + chr(13))
        time.sleep(1)
        GSM_port.write('AT+FTPGET=2,1024' + chr(13))
        time.sleep(1)



class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        global portOpen

        while True:
            while portOpen:
                global c
                d = GSM_port.read()
                global Console_Data
                Console_Data += d

                if ('+CLIP' in Console_Data):
                    c=Console_Data.rfind('+CLIP:')
                    c+=8
                self.emit(QtCore.SIGNAL("SERIAL_DATA"))




if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    app = MainGUIClass()
    app.show()
    app.Thread1.start()
    sys.exit(a.exec_())
