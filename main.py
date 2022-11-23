from PyQt5.QtWidgets import QAbstractItemView
import interface
from PyQt5 import QtWidgets
from best_product import list_of_purchases

class Main(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.pushButton_searchAddress.pressed.connect(self.go)
        self.listWidget_goods.setSelectionMode(QAbstractItemView.MultiSelection)
        self.pushButton_searchGoods.pressed.connect(self.result)

    def go(self):
        street = self.lineEdit_street.text()
        number = self.lineEdit_number.text()
        print(street + " " + number)

    def result(self):
        goods = [item.text() for item in self.listWidget_goods.selectedItems()]
        otvet = list_of_purchases(goods)
        print(goods)
        print(otvet)
        self.label_result.setText('Магазин: ' + '"' + str(otvet[0]) + '"' + '. Адрес: ' + str(otvet[1]))

if __name__ == "__main__":
    App = QtWidgets.QApplication([])
    window = Main()
    window.show()
    App.exec()