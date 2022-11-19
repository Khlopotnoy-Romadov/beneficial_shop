import interface
from PyQt5 import QtWidgets
from pyowm.utils.config import get_default_config

class Main(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.pushButton_searchAddress.pressed.connect(self.go)

    def go(self):
        street = self.lineEdit_street.text()
        number = self.lineEdit_number.text()
        self.do(street, number)

    def do(self, street, number):
        print(street + " " + number)

App = QtWidgets.QApplication([])
window = Main()
window.show()
App.exec()