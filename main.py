from PyQt5.QtWidgets import QAbstractItemView
import interface
from PyQt5 import QtWidgets
from best_product import best_shop
from data import discount
from data import shops
from best_product import distance
from best_product import discount_card
from adresses import df

class Main(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        #self.pushButton_searchAddress.pressed.connect(self.go)
        self.listWidget_goods.setSelectionMode(QAbstractItemView.MultiSelection)
        self.pushButton_searchGoods.pressed.connect(self.result)

    # def go(self):
    #     street = self.lineEdit_street.text()
    #     number = self.lineEdit_number.text()
    #
    #     address = "ул. " + street + ", д. " + number


    def result(self):
        street = self.lineEdit_street.text()
        number = self.lineEdit_number.text()
        address = "ул. " + street + ", д. " + number

        goods = [item.text() for item in self.listWidget_goods.selectedItems()]
        discounts = [item.text() for item in self.listWidget_shops.selectedItems()]

        price = self.comboBox_price.currentText()
        distance = self.comboBox_distance.currentText()

        lst_discs = discount(discounts)

        otvet = best_shop(goods, address, int(price[0]), int(distance[0]), lst_discs)

        self.label_result.setText('Магазин: ' + '"' + str(otvet[0]) + '"' + '. Адрес: ' + str(otvet[1]) +
        '. Расстояние от дома: ' + str(otvet[2][otvet[0]]) + '. Сумма покупки: ' + str(otvet[3][otvet[0]]))

        self.label_more_inf.setText('Магазин' + ' ' + 'Расстояние до дома' + " " + "Цена" + "\n" +
              'Шестёрочка' + " " + str(otvet[2]['Шестёрочка']) + " " + str(otvet[3]['Шестёрочка']) + "\n" +
              'Диски' + " " + str(otvet[2]['Диски']) + " " + str(otvet[3]['Диски']) + "\n" +
              'Компас' + " " + str(otvet[2]['Компас']) + " " + str(otvet[3]['Компас']) + "\n" +
              "Повязка" + " " + str(otvet[2]['Повязка']) + " " + str(otvet[3]['Повязка']) + "\n" +
              "Наша" + " " + str(otvet[2]['Наша']) + " " + str(otvet[3]['Наша']) + "\n" +
              "Развилка" + " " + str(otvet[2]['Развилка']) + " " + str(otvet[3]['Развилка']) + "\n" +
              "Преданный" + " " + str(otvet[2]['Преданный']) + " " + str(otvet[3]['Преданный']) + "\n" +
              "Хорошо" + " " + str(otvet[2]['Хорошо']) + " " + str(otvet[3]['Хорошо']) + "\n")


if __name__ == "__main__":
    App = QtWidgets.QApplication([])
    window = Main()
    window.show()
    App.exec()