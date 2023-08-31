import sys
import os
import get_address

# Interface Module
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from interface import Ui_MainWindow
import qdarkstyle

class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        self.initUI()

    def initUI(self):
        self.ui.btn_Start.clicked.connect(self.start)
        self.ui.btn_Close.clicked.connect(self.close)
        self.ui.btn_OpenFile.clicked.connect(self.openFile)

    def start(self):
        sender = self.sender()        
        self.ui.lbl_status.setText("Status: " + "Running")

        if sender.text() == "Start":
            print("run")
            mode_box = self.ui.mode_box.findChildren(QtWidgets.QRadioButton)
            for mode_box in mode_box:
                if mode_box.isChecked():
                    mode_box_selected = mode_box.text()
            get_address.etherscan_file(mode_box_selected, float(self.ui.txt_min_amount.text()), int(self.ui.txt_num_addresses.text()))
            self.ui.lbl_status.setText("Status: " + "Done")

        # print('button clicked')
        # print('name : ' + self.txt_name.text())
        # print('surname  : ' + self.txt_surname.text())

    def close(self):
        QtWidgets.QApplication.quit()

    def openFile(self):
        path = "C:\Code\Projects\Apps\greater_address.csv" 
        os.startfile(path)
        

def windows():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()

    sys.exit(app.exec())


windows()