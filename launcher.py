from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import pyperclip
import webbrowser

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.dictionary = {}

        #Window Settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 890)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Class Selector ComboBox
        self.classSelector = QtWidgets.QComboBox(self.centralwidget)
        self.classSelector.setGeometry(QtCore.QRect(20, 470, 321, 171))
        self.classSelector.setObjectName("classSelector")
        self.classSelector.addItem("")
        self.classSelector.addItem("MGT310")
        self.classSelector.addItem("CIS341.1")
        self.classSelector.addItem("C100")

        #Add Class Label
        self.addClassLabel = QtWidgets.QLabel(self.centralwidget)
        self.addClassLabel.setGeometry(QtCore.QRect(20, 20, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addClassLabel.setFont(font)
        self.addClassLabel.setObjectName("addClassLabel")

        #Join Class Button
        self.joinButton = QtWidgets.QPushButton(self.centralwidget)
        self.joinButton.setGeometry(QtCore.QRect(640, 470, 321, 171))
        self.joinButton.setObjectName("joinButton")
        self.joinButton.clicked.connect(lambda: joinPressed(self.classSelector.currentText()))

        #Class Name LineEdit
        self.className = QtWidgets.QLineEdit(self.centralwidget)
        self.className.setGeometry(QtCore.QRect(140, 170, 231, 21))
        self.className.setObjectName("className")

        #Class ID LineEdit
        self.classID = QtWidgets.QLineEdit(self.centralwidget)
        self.classID.setGeometry(QtCore.QRect(140, 220, 231, 21))
        self.classID.setObjectName("classID")

        #Class Password LineEdit
        self.classPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.classPassword.setGeometry(QtCore.QRect(140, 270, 231, 20))
        self.classPassword.setObjectName("classPassword")

        #Class Name Label
        self.classNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.classNameLabel.setGeometry(QtCore.QRect(20, 170, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.classNameLabel.setFont(font)
        self.classNameLabel.setObjectName("classNameLabel")

        #Class Password Label
        self.classPasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.classPasswordLabel.setGeometry(QtCore.QRect(20, 270, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.classPasswordLabel.setFont(font)
        self.classPasswordLabel.setObjectName("classPasswordLabel")

        #Class ID Label
        self.classIDLabel = QtWidgets.QLabel(self.centralwidget)
        self.classIDLabel.setGeometry(QtCore.QRect(20, 220, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.classIDLabel.setFont(font)
        self.classIDLabel.setObjectName("classIDLabel")

        #Submit New Call Info Button
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(114, 330, 131, 31))
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(lambda: submitPressed(self.dictionary, self.className.text, self.classID.text, self.classPassword.text))

        #Main Window and bar info
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.classSelector.setItemText(0, _translate("MainWindow", ""))
        self.addClassLabel.setText(_translate("MainWindow", "Add a new zoom class:"))
        self.joinButton.setText(_translate("MainWindow", "Join the selected class!"))
        self.classNameLabel.setText(_translate("MainWindow", "Class Name:"))
        self.classPasswordLabel.setText(_translate("MainWindow", "Invitation Password:"))
        self.classIDLabel.setText(_translate("MainWindow", "Invitation ID:"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))

#classes are 0, 2, and 4 in list format
def joinPressed(text):
    with open('class_file.csv', newline='') as csvfile:
        read = list(csv.reader(csvfile, delimiter=' '))
        mgtInfo = str(read[0])
        cisInfo = str(read[2])
        cInfo = str(read[4])

        mgtInfo = mgtInfo.replace("[", "")
        mgtInfo = mgtInfo.replace("'", "")
        mgtInfo = mgtInfo.replace(",", "")
        mgtInfo = mgtInfo.replace("]", "")
        mgtSplit = mgtInfo.split()
        managementClassID = mgtSplit[0]
        managementClassPassword = mgtSplit[1]

        cisInfo = cisInfo.replace("[", "")
        cisInfo = cisInfo.replace("'", "")
        cisInfo = cisInfo.replace(",", "")
        cisInfo = cisInfo.replace("]", "")
        cisSplit = cisInfo.split()
        cisClassID = cisSplit[0]
        cisClassPassword = cisSplit[1]
    
        cInfo = cInfo.replace("[", "")
        cInfo = cInfo.replace("'", "")
        cInfo = cInfo.replace(",", "")
        cInfo = cInfo.replace("]", "")
        cSplit = cInfo.split()
        cClassID = cSplit[0]
        cClassPassword = cSplit[1]

        # Using classIDs and classPasswords to now connect with zoom and open up.
        if(text == "MGT310"):
            url = ("https://zoom.us/wc/" + managementClassID + "/join?prefer=1&un=TWFsYWNoaSBMaWJlcmRh&pwd=" + managementClassPassword)
            webbrowser.open(url, new=2, autoraise=True)

        if(text == "CIS341.1"):
            url = ("https://zoom.us/wc/" + cisClassID + "/join?prefer=1&un=TWFsYWNoaSBMaWJlcmRh&pwd=" + cisClassPassword)
            webbrowser.open(url, new=2, autoraise=True)

        if(text == "C100"):
            url = ("https://zoom.us/wc/" + cClassID + "/join?prefer=1&un=TWFsYWNoaSBMaWJlcmRh&pwd=" + cClassPassword)
            webbrowser.open(url, new=2, autoraise=True)

        #Username: TWFsYWNoaSBMaWJlcmRh

def submitPressed(dictionary, name, id, password):
        print(name)
        print(id)
        print(password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

