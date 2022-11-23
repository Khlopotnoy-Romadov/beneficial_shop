from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.uic.properties import QtGui
import interface
from PyQt5 import QtWidgets
from pyowm.utils.config import get_default_config
from best_product import list_of_purchases

class Main(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.pushButton_searchAddress.pressed.connect(self.go)
        self.pushButton_searchGoods.pressed.connect(self.result)
        # self.pushButton_close.pressed.connect(self.close)

    def go(self):
        street = self.lineEdit_street.text()
        number = self.lineEdit_number.text()
        self.do(street, number)

    def do(self, street, number):
        print(street + " " + number)

        self.listWidget_goods.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget_goods.itemSelectionChanged.connect(self.best)

    def best(self):
        goods = [item.text() for item in self.listWidget_goods.selectedItems()]
        self.result(goods)

    def result(self, lst):
        print(list_of_purchases(lst))

if __name__ == "__main__":
    App = QtWidgets.QApplication([])
    window = Main()
    window.show()
    App.exec()