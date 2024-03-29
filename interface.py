from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 937)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, 20, 1929, 1200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("tekstura-s-produktami-pitaniya.jpg"))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.lineEdit_street = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_street.setGeometry(QtCore.QRect(20, 130, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_street.setFont(font)
        self.lineEdit_street.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.lineEdit_street.setObjectName("lineEdit_street")
        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        self.label_heading.setGeometry(QtCore.QRect(20, 50, 941, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_heading.setFont(font)
        self.label_heading.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_heading.setObjectName("label_heading")
        self.lineEdit_number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_number.setGeometry(QtCore.QRect(442, 130, 351, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_number.setFont(font)
        self.lineEdit_number.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.pushButton_searchAddress = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_searchAddress.setGeometry(QtCore.QRect(794, 130, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_searchAddress.setFont(font)
        self.pushButton_searchAddress.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_searchAddress.setObjectName("pushButton_searchAddress")
        self.listWidget_goods = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_goods.setGeometry(QtCore.QRect(30, 270, 401, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listWidget_goods.setFont(font)
        self.listWidget_goods.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.listWidget_goods.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_goods.setObjectName("listWidget_goods")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_goods.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_goods.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_goods.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_goods.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_goods.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_goods.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_goods.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_goods.addItem(item)
        self.label_pick_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_pick_1.setGeometry(QtCore.QRect(30, 210, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_pick_1.setFont(font)
        self.label_pick_1.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_pick_1.setObjectName("label_pick_1")
        self.pushButton_searchGoods = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_searchGoods.setGeometry(QtCore.QRect(290, 470, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_searchGoods.setFont(font)
        self.pushButton_searchGoods.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_searchGoods.setObjectName("pushButton_searchGoods")
        self.label_headResult = QtWidgets.QLabel(self.centralwidget)
        self.label_headResult.setGeometry(QtCore.QRect(230, 530, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_headResult.setFont(font)
        self.label_headResult.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_headResult.setObjectName("label_headResult")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(230, 570, 551, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.label_result.setObjectName('rules')
        self.label_result.setWordWrap(True)
        self.listWidget_shops = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_shops.setGeometry(QtCore.QRect(535, 271, 411, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listWidget_shops.setFont(font)
        self.listWidget_shops.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.listWidget_shops.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_shops.setObjectName("listWidget_shops")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_shops.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_shops.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_shops.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_shops.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_shops.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_shops.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_shops.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_shops.addItem(item)
        self.label_pick_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_pick_2.setGeometry(QtCore.QRect(540, 210, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_pick_2.setFont(font)
        self.label_pick_2.setAcceptDrops(False)
        self.label_pick_2.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_pick_2.setWordWrap(True)
        self.label_pick_2.setObjectName("label_pick_2")

        self.label_pick_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_pick_1.setGeometry(QtCore.QRect(30, 210, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_pick_1.setFont(font)
        self.label_pick_1.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_pick_1.setObjectName("label_pick_1")

        self.label_more = QtWidgets.QLabel(self.centralwidget)
        self.label_more.setGeometry(QtCore.QRect(110, 660, 260, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_more.setFont(font)
        font.setWeight(75)
        self.label_more.setFont(font)
        self.label_more.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_more.setObjectName("label_more")

        self.label_more_inf = QtWidgets.QLabel(self.centralwidget)
        self.label_more_inf.setGeometry(QtCore.QRect(40, 710, 491, 211))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_more_inf.setFont(font)
        self.label_more_inf.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_more_inf.setText("")
        self.label_more_inf.setWordWrap(True)
        self.label_more_inf.setObjectName("label_more_inf")
        self.comboBox_feedback = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_feedback.setGeometry(QtCore.QRect(620, 750, 341, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_feedback.setFont(font)
        self.comboBox_feedback.setObjectName("comboBox_feedback")
        self.comboBox_feedback.addItem("")
        self.comboBox_feedback.addItem("")
        self.comboBox_feedback.addItem("")
        self.comboBox_feedback.addItem("")
        self.comboBox_feedback.addItem("")
        self.label_feedback = QtWidgets.QLabel(self.centralwidget)
        self.label_feedback.setGeometry(QtCore.QRect(620, 690, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_feedback.setFont(font)
        self.label_feedback.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_feedback.setWordWrap(True)
        self.label_feedback.setObjectName("label_feedback")
        self.label_thank = QtWidgets.QLabel(self.centralwidget)
        self.label_thank.setGeometry(QtCore.QRect(620, 870, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_thank.setFont(font)
        self.label_thank.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_thank.setWordWrap(True)
        self.label_thank.setObjectName("label_thank")
        self.comboBox_price = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_price.setGeometry(QtCore.QRect(240, 380, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_price.setFont(font)
        self.comboBox_price.setObjectName("comboBox_price")
        self.comboBox_price.addItem("")
        self.comboBox_price.addItem("")
        self.comboBox_price.addItem("")
        self.label_price = QtWidgets.QLabel(self.centralwidget)
        self.label_price.setGeometry(QtCore.QRect(30, 380, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_price.setFont(font)
        self.label_price.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_price.setWordWrap(True)
        self.label_price.setObjectName("label_price")
        self.label_distance = QtWidgets.QLabel(self.centralwidget)
        self.label_distance.setGeometry(QtCore.QRect(540, 380, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_distance.setFont(font)
        self.label_distance.setStyleSheet("background-color: rgba(255, 255, 255, 225);")
        self.label_distance.setWordWrap(True)
        self.label_distance.setObjectName("label_distance")
        self.comboBox_distance = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_distance.setGeometry(QtCore.QRect(750, 380, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_distance.setFont(font)
        self.comboBox_distance.setObjectName("comboBox_distance")
        self.comboBox_distance.addItem("")
        self.comboBox_distance.addItem("")
        self.comboBox_distance.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_street.setPlaceholderText(_translate("MainWindow", "Введите вашу улицу"))
        self.label_heading.setText(_translate("MainWindow", "Найдите самый выгодный магазин для покупки в вашем районе!"))
        self.lineEdit_number.setPlaceholderText(_translate("MainWindow", "Введите номер дома"))
        self.pushButton_searchAddress.setText(_translate("MainWindow", "Поиск"))
        __sortingEnabled = self.listWidget_goods.isSortingEnabled()
        self.listWidget_goods.setSortingEnabled(False)
        item = self.listWidget_goods.item(0)
        item.setText(_translate("MainWindow", "хлеб"))
        item = self.listWidget_goods.item(1)
        item.setText(_translate("MainWindow", "сыр"))
        item = self.listWidget_goods.item(2)
        item.setText(_translate("MainWindow", "колбаса"))
        item = self.listWidget_goods.item(3)
        item.setText(_translate("MainWindow", "молоко"))
        item = self.listWidget_goods.item(4)
        item.setText(_translate("MainWindow", "помидоры"))
        item = self.listWidget_goods.item(5)
        item.setText(_translate("MainWindow", "огурцы"))
        item = self.listWidget_goods.item(6)
        item.setText(_translate("MainWindow", "говядина"))
        item = self.listWidget_goods.item(7)
        item.setText(_translate("MainWindow", "свинина"))
        self.listWidget_goods.setSortingEnabled(__sortingEnabled)
        self.label_pick_1.setText(_translate("MainWindow", "Выберите необходимые продукты:"))
        self.pushButton_searchGoods.setText(_translate("MainWindow", "Найти лучший вариант покупки"))
        self.label_headResult.setText(_translate("MainWindow", "Лучший магазин для покупок ваших товаров"))
        __sortingEnabled = self.listWidget_shops.isSortingEnabled()
        self.listWidget_shops.setSortingEnabled(False)
        item = self.listWidget_shops.item(0)
        item.setText(_translate("MainWindow", "\"Шестёрочка\""))
        item = self.listWidget_shops.item(1)
        item.setText(_translate("MainWindow", "\"Диски\""))
        item = self.listWidget_shops.item(2)
        item.setText(_translate("MainWindow", "\"Компас\""))
        item = self.listWidget_shops.item(3)
        item.setText(_translate("MainWindow", "\"Повязка\""))
        item = self.listWidget_shops.item(4)
        item.setText(_translate("MainWindow", "\"Наша\""))
        item = self.listWidget_shops.item(5)
        item.setText(_translate("MainWindow", "\"Развилка\""))
        item = self.listWidget_shops.item(6)
        item.setText(_translate("MainWindow", "\"Преданный\""))
        item = self.listWidget_shops.item(7)
        item.setText(_translate("MainWindow", "\"Хорошо\""))
        self.listWidget_shops.setSortingEnabled(__sortingEnabled)
        self.label_pick_2.setText(_translate("MainWindow", "Выберите магазины, в которых у вас имеется скидочная карта:"))
        self.label_more.setText(_translate("MainWindow", "Подробная информация"))
        self.comboBox_feedback.setItemText(0, _translate("MainWindow", "1 (непригодно для использования)"))
        self.comboBox_feedback.setItemText(1, _translate("MainWindow", "2 (больше минусов, чем плюсов)"))
        self.comboBox_feedback.setItemText(2, _translate("MainWindow", "3 (приемлемо)"))
        self.comboBox_feedback.setItemText(3, _translate("MainWindow", "4 (комфортно пользоваться)"))
        self.comboBox_feedback.setItemText(4, _translate("MainWindow", "5 (всё супер)"))
        self.label_feedback.setText(_translate("MainWindow", "Поставьте оценку нашему приложению"))
        self.label_thank.setText(_translate("MainWindow", "Спасибо за оценку!"))
        self.comboBox_price.setItemText(0, _translate("MainWindow", "1 (не важно)"))
        self.comboBox_price.setItemText(1, _translate("MainWindow", "2 (важно)"))
        self.comboBox_price.setItemText(2, _translate("MainWindow", "3 (очень важно)"))
        self.label_price.setText(_translate("MainWindow", "Приоритет по цене"))
        self.label_distance.setText(_translate("MainWindow", "Приоритет по расстоянию"))
        self.comboBox_distance.setItemText(0, _translate("MainWindow", "1 (не важно)"))
        self.comboBox_distance.setItemText(1, _translate("MainWindow", "2 (важно)"))
        self.comboBox_distance.setItemText(2, _translate("MainWindow", "3 (очень важно)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
