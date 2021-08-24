import random
from itertools import product

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from path import attrs_labels, LABEL_TO_COUNT, LABEL_TO_PATH, TOTAL


IMG_X = 432
IMG_Y = 432


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        BASE_Y = 70
        FIRST_ELEM_OFFSET = 70
        PER_ELEM_OFFSET = 60
        WINDOW_HEIGHT = BASE_Y + FIRST_ELEM_OFFSET + PER_ELEM_OFFSET * len(attrs_labels)
        # if we have very few attributes, image should be still visible
        WINDOW_HEIGHT = max(IMG_Y + 20, WINDOW_HEIGHT)
        MainWindow.resize(700, WINDOW_HEIGHT)
        MainWindow.setFixedSize(710, WINDOW_HEIGHT + 10)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, IMG_X, IMG_Y))
        self.label.setPixmap(QtGui.QPixmap("pixel art.png"))
        self.label.setObjectName("label")

        self.vals = [0 for i in range(len(attrs_labels))]

        X_OFFSET_ELEMS = 480
        BASE_Y_OFFSET = FIRST_ELEM_OFFSET
        Y_OFFSET_STEP = PER_ELEM_OFFSET
        SLIDER_WIDTH = 200
        SLIDER_HEIGHT = 22

        for idx, label in enumerate(attrs_labels):
            slider = QtWidgets.QSlider(self.centralwidget)
            slider.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, BASE_Y_OFFSET + idx * Y_OFFSET_STEP, SLIDER_WIDTH, SLIDER_HEIGHT))
            slider.setOrientation(QtCore.Qt.Horizontal)
            slider.setObjectName("horizontalSlider")
            slider.setTickInterval(3)
            slider.setMinimum(1)
            slider.setMaximum(LABEL_TO_COUNT[label])

            def sliderValForLabel(label):
                def sliderValue(value):
                    label_idx = attrs_labels.index(label)
                    self.vals[label_idx] = value
                    self.build_img_for_val(self.vals)
                    self.label.setPixmap(
                        QtGui.QPixmap(f'myChar/newChar{"+".join([str(i) for i in self.vals])}.png'))
                return sliderValue

            slider.valueChanged['int'].connect(sliderValForLabel(label))
            setattr(self, f'horizontalSlider{idx + 1}', slider)

        BUTTONS_Y_OFFSET = BASE_Y_OFFSET + len(attrs_labels) * Y_OFFSET_STEP
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, BUTTONS_Y_OFFSET, 91, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(X_OFFSET_ELEMS + 110, BUTTONS_Y_OFFSET, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        BASE_Y_OFFSET = 50
        Y_OFFSET_STEP = 60
        for i in range(len(attrs_labels)):
            label_widget = QtWidgets.QLabel(self.centralwidget)
            label_widget.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, BASE_Y_OFFSET + i * Y_OFFSET_STEP, SLIDER_WIDTH, 16))
            label_widget.setObjectName(f'label_{i+1}')
            setattr(self, f'label_{i+1}', label_widget)

        self.total_label = QtWidgets.QLabel(self.centralwidget)
        self.total_label.setGeometry(QtCore.QRect(X_OFFSET_ELEMS, 5, 80, 13))
        self.total_label.setObjectName("label_total")

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
        for idx, label in enumerate(attrs_labels):
            label_widget = getattr(self, f'label_{idx+1}')
            label_widget.setText(_translate("MainWindow", f"{label.upper()}: "+str(LABEL_TO_COUNT[label])))

        self.total_label.setText(_translate("Mainwindow", "TOTAL:"+str(TOTAL)))

    def getRandom(self):
        vals = [random.randint(1, LABEL_TO_COUNT[label]) for label in attrs_labels]
        self.build_img_for_val(vals)
        self.label.setPixmap(QtGui.QPixmap(f'myChar/newChar{"+".join([str(i) for i in vals])}.png'))
        self.vals = vals

        for idx, i in enumerate(vals):
            slider = getattr(self, f'horizontalSlider{idx+1}')
            slider.setValue(i)

    def build_img_for_val(self, vals):
        layers = [Image.open(LABEL_TO_PATH[label].format(val)) for val, label in zip(vals, attrs_labels)]
        res_img = layers[0]
        for layer in layers[1:]:
            res_img.paste(layer, None, layer)
        res_img.save(f'myChar/newChar{"+".join([str(i) for i in vals])}.png', 'PNG')
        return res_img

    def getAll(self):
        counts_list = [list(range(1, LABEL_TO_COUNT[label] + 1)) for label in attrs_labels]
        [self.build_img_for_val(val) for val in product(*counts_list)]


if __name__ == "__main__":
    while True:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
