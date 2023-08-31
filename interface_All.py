import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
import qdarkstyle
import get_address


class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(1200, 300, 500,500)
        self.setWindowTitle("Ethereum Address Manager")
        self.setWindowIcon(QIcon("Escan.jpg"))
        self.initUI()

        # Dark Mode Style
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Enter your name")
        self.lbl_name.move(50,50)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Enter min amount")
        self.lbl_surname.move(50,90)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(200,50)
        self.txt_name.resize(200, 32)

        self.num_min_amount = QtWidgets.QLineEdit(self)
        self.num_min_amount.move(200,90)
        self.num_min_amount.resize(200, 32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('Save')
        self.btn_save.clicked.connect(self.clicked)
        self.btn_save.move(200, 130)

        self.lbl_status = QtWidgets.QLabel(self)
        self.lbl_status.setText('Status')
        self.lbl_status.move(200, 170)
        self.lbl_status.resize(200, 200)


    def running(self):
        sender = self.sender()
        if sender.text() == "Save":
            print("run")
            get_address.etherscan_file(float(self.num_min_amount.text()))
            self.lbl_status.setText("Status: " + "Done")



    def clicked(self):
        
        self.lbl_status.setText("Status: " + "Running")
        self.running()

        # print('button clicked')
        # print('name : ' + self.txt_name.text())
        # print('surname  : ' + self.txt_surname.text())





def windows():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec())


windows()