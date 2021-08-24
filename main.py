import random
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from path import *

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setFixedSize(710, 510)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 432, 432))
        self.label.setPixmap(QtGui.QPixmap("pixel art.png"))
        self.label.setObjectName("label")

        X_OFFSET_ELEMS = 480

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 70, 200, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setTickInterval(3)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(number_of_head)
        self.horizontalSlider.valueChanged['int'].connect(self.sliderValue)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 130, 200, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setTickInterval(3)
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(number_of_glasses)
        self.horizontalSlider_2.valueChanged['int'].connect(self.sliderValue2)

        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 190, 200, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_3.setTickInterval(3)
        self.horizontalSlider_3.setMinimum(1)
        self.horizontalSlider_3.setMaximum(number_of_background)
        self.horizontalSlider_3.valueChanged['int'].connect(self.sliderValue3)

        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 250, 200, 22))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.horizontalSlider_4.setTickInterval(3)
        self.horizontalSlider_4.setMinimum(1)
        self.horizontalSlider_4.setMaximum(number_of_body)
        self.horizontalSlider_4.valueChanged['int'].connect(self.sliderValue4)

        self.horizontalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 310, 200, 22))
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.horizontalSlider_5.setTickInterval(3)
        self.horizontalSlider_5.setMinimum(1)
        self.horizontalSlider_5.setMaximum(number_of_scarf)
        self.horizontalSlider_5.valueChanged['int'].connect(self.sliderValue5)

        self.horizontalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 370, 200, 22))
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.horizontalSlider_6.setTickInterval(3)
        self.horizontalSlider_6.setMinimum(1)
        self.horizontalSlider_6.setMaximum(number_of_shirt)
        self.horizontalSlider_6.valueChanged['int'].connect(self.sliderValue6)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 430, 91, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(X_OFFSET_ELEMS + 110, 430, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 50, 80, 13))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 110, 80, 13))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 170, 80, 13))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 230, 80, 13))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 290, 80, 13))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 350, 80, 13))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 5, 80, 13))
        self.label_8.setObjectName("label_8")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.getRandom)
        self.pushButton_2.clicked.connect(self.getAll)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "hugo_artGenerator"))
        MainWindow.setWindowIcon(QIcon('heart.png'))
        self.pushButton.setText(_translate("MainWindow", "RANDOMIZE"))
        self.pushButton_2.setText(_translate("MainWindow", "GET ALL"))
        self.label_2.setText(_translate("MainWindow", "HEAD: "+str(number_of_head)))
        self.label_3.setText(_translate("MainWindow", "GLASSES: "+str(number_of_glasses)))
        self.label_4.setText(_translate("MainWindow", "BACK: "+str(number_of_background)))
        self.label_5.setText(_translate("Mainwindow",  "BODY: "+str(number_of_body)))
        self.label_6.setText(_translate("Mainwindow",  "SCARF: "+str(number_of_scarf)))
        self.label_7.setText(_translate("Mainwindow",  "SHIRT: "+str(number_of_shirt)))
        self.label_8.setText(_translate("Mainwindow", "TOTAL:"+str(TOTAL)))

    def getRandom(self):
        global x, y, z, q, w, e
        x = random.randint(1, number_of_body)
        y = random.randint(1, number_of_glasses)
        z = random.randint(1, number_of_head)
        q = random.randint(1, number_of_background)
        w = random.randint(1, number_of_scarf)
        e = random.randint(1, number_of_shirt)

        background = Image.open(f"source/background/background{q}.png")
        body = Image.open(f"source/body/body{x}.png")
        glasses = Image.open(f"source/glasses/glasses{y}.png")
        head = Image.open(f"source/head/head{z}.png")
        scarf = Image.open(f"source/scarf/scarf{w}.png")
        shirt = Image.open(f"source/shirt/shirt{e}.png")

        background.paste(body, None, body)
        background.paste(shirt, None, shirt)
        background.paste(scarf, None, scarf)
        background.paste(head, None, head)
        background.paste(glasses, None, glasses)

        background.save("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, z, q, w, e), "PNG")
        self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, z, q, w, e)))
        self.horizontalSlider.setValue(z)
        self.horizontalSlider_2.setValue(y)
        self.horizontalSlider_3.setValue(q)
        self.horizontalSlider_4.setValue(x)
        self.horizontalSlider_5.setValue(w)
        self.horizontalSlider_6.setValue(e)


    def getAll(self):
       for a in range(1,number_of_body+1):
           for b in range(1,number_of_glasses+1):
               for c in range(1,number_of_head+1):
                   for d in range(1,number_of_background+1):
                       for f in range(1, number_of_scarf+1):
                           for g in range(1, number_of_shirt+1):
                                background = Image.open(f"source/background/background{d}.png")
                                body = Image.open(f"source/body/body{a}.png")
                                glasses = Image.open(f"source/glasses/glasses{b}.png")
                                head = Image.open(f"source/head/head{c}.png")
                                scarf = Image.open(f"source/scarf/scarf{f}.png")
                                shirt = Image.open(f"source/shirt/shirt{g}.png")

                                background.paste(body, None, body)
                                background.paste(shirt, None, shirt)
                                background.paste(scarf, None, scarf)
                                background.paste(head, None, head)
                                background.paste(glasses, None, glasses)
                                background.save("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(a, b, c, d, f, g), "PNG")

    def sliderValue(self,value):
        global z
        try:
            background = Image.open(f"source/background/background{q}.png")
            body = Image.open(f"source/body/body{x}.png")
            glasses = Image.open(f"source/glasses/glasses{y}.png")
            head = Image.open(f"source/head/head{value}.png")
            scarf = Image.open(f"source/scarf/scarf{w}.png")
            shirt = Image.open(f"source/shirt/shirt{e}.png")

            background.paste(body, None, body)
            background.paste(shirt, None, shirt)
            background.paste(scarf, None, scarf)
            background.paste(head, None, head)
            background.paste(glasses, None, glasses)

            background.save("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, value, q, w, e), "PNG")
            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, value, q, w, e)))
            z = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first of all click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()


    def sliderValue2(self,value):
        global y
        try:
            background = Image.open(f"source/background/background{q}.png")
            body = Image.open(f"source/body/body{x}.png")
            glasses = Image.open(f"source/glasses/glasses{value}.png")
            head = Image.open(f"source/head/head{z}.png")
            scarf = Image.open(f"source/scarf/scarf{w}.png")
            shirt = Image.open(f"source/shirt/shirt{e}.png")

            background.paste(body, None, body)
            background.paste(shirt, None, shirt)
            background.paste(scarf, None, scarf)
            background.paste(head, None, head)
            background.paste(glasses, None, glasses)

            background.save("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, value, z, q, w, e), "PNG")
            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, value, z, q, w, e)))
            y = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first of all click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()

    def sliderValue3(self,value):
        global q
        try:
            background = Image.open(f"source/background/background{value}.png")
            body = Image.open(f"source/body/body{x}.png")
            glasses = Image.open(f"source/glasses/glasses{y}.png")
            head = Image.open(f"source/head/head{z}.png")
            scarf = Image.open(f"source/scarf/scarf{w}.png")
            shirt = Image.open(f"source/shirt/shirt{e}.png")

            background.paste(body, None, body)
            background.paste(shirt, None, shirt)
            background.paste(scarf, None, scarf)
            background.paste(head, None, head)
            background.paste(glasses, None, glasses)

            background.save("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, z, value, w, e), "PNG")
            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, z, value, w, e)))
            q = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()

    def sliderValue4(self,value):
        global x
        try:
            background = Image.open(f"source/background/background{q}.png")
            body = Image.open(f"source/body/body{value}.png")
            glasses = Image.open(f"source/glasses/glasses{y}.png")
            head = Image.open(f"source/head/head{z}.png")
            scarf = Image.open(f"source/scarf/scarf{w}.png")
            shirt = Image.open(f"source/shirt/shirt{e}.png")

            background.paste(body, None, body)
            background.paste(shirt, None, shirt)
            background.paste(scarf, None, scarf)
            background.paste(head, None, head)
            background.paste(glasses, None, glasses)

            background.save("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(value, y, z, q, w, e), "PNG")
            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(value, y, z, q, w, e)))
            x = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first of all click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()

    def sliderValue5(self,value):
        global w
        try:
            background = Image.open(f"source/background/background{q}.png")
            body = Image.open(f"source/body/body{x}.png")
            glasses = Image.open(f"source/glasses/glasses{y}.png")
            head = Image.open(f"source/head/head{z}.png")
            scarf = Image.open(f"source/scarf/scarf{value}.png")
            shirt = Image.open(f"source/shirt/shirt{e}.png")

            background.paste(body, None, body)
            background.paste(shirt, None, shirt)
            background.paste(scarf, None, scarf)
            background.paste(head, None, head)
            background.paste(glasses, None, glasses)

            background.save("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, z, q, value, e), "PNG")
            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, z, q, value, e)))
            w = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first of all click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()

    def sliderValue6(self,value):
        global e
        try:
            background = Image.open(f"source/background/background{q}.png")
            body = Image.open(f"source/body/body{x}.png")
            glasses = Image.open(f"source/glasses/glasses{y}.png")
            head = Image.open(f"source/head/head{z}.png")
            scarf = Image.open(f"source/scarf/scarf{w}.png")
            shirt = Image.open(f"source/shirt/shirt{value}.png")

            background.paste(body, None, body)
            background.paste(shirt, None, shirt)
            background.paste(scarf, None, scarf)
            background.paste(head, None, head)
            background.paste(glasses, None, glasses)

            background.save("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, z, q, w, value), "PNG")
            self.label.setPixmap(QtGui.QPixmap("myChar/newMergeChar{}+{}+{}+{}+{}+{}.png".format(x, y, z, q, w, value)))
            e = value
        except NameError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Dont be quick")
            msg.setInformativeText('Please first of all click RANDOMIZE')
            msg.setWindowTitle("Error")
            msg.exec_()

if __name__ == "__main__":

    while True:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

