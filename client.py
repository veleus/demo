# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 290, 721, 281))
        self.tableWidget.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(244, 244, 244);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.client = QtWidgets.QLineEdit(self.centralwidget)
        self.client.setGeometry(QtCore.QRect(30, 70, 113, 21))
        self.client.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(244, 244, 244);")
        self.client.setAlignment(QtCore.Qt.AlignCenter)
        self.client.setObjectName("client")
        self.model = QtWidgets.QLineEdit(self.centralwidget)
        self.model.setGeometry(QtCore.QRect(170, 70, 113, 21))
        self.model.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(244, 244, 244);")
        self.model.setAlignment(QtCore.Qt.AlignCenter)
        self.model.setObjectName("model")
        self.opisanie = QtWidgets.QLineEdit(self.centralwidget)
        self.opisanie.setGeometry(QtCore.QRect(310, 70, 113, 21))
        self.opisanie.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(244, 244, 244);")
        self.opisanie.setAlignment(QtCore.Qt.AlignCenter)
        self.opisanie.setObjectName("opisanie")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(450, 70, 101, 23))
        self.addBtn.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.addBtn.setObjectName("addBtn")
        self.client_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.client_2.setGeometry(QtCore.QRect(170, 120, 113, 21))
        self.client_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(244, 244, 244);")
        self.client_2.setAlignment(QtCore.Qt.AlignCenter)
        self.client_2.setObjectName("client_2")
        self.opisanie_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.opisanie_2.setGeometry(QtCore.QRect(450, 120, 113, 21))
        self.opisanie_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(244, 244, 244);")
        self.opisanie_2.setAlignment(QtCore.Qt.AlignCenter)
        self.opisanie_2.setObjectName("opisanie_2")
        self.model_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.model_2.setGeometry(QtCore.QRect(310, 120, 113, 21))
        self.model_2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(244, 244, 244);")
        self.model_2.setText("")
        self.model_2.setAlignment(QtCore.Qt.AlignCenter)
        self.model_2.setObjectName("model_2")
        self.id_column = QtWidgets.QLineEdit(self.centralwidget)
        self.id_column.setGeometry(QtCore.QRect(30, 120, 113, 21))
        self.id_column.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(244, 244, 244);")
        self.id_column.setAlignment(QtCore.Qt.AlignCenter)
        self.id_column.setObjectName("id_column")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(590, 120, 151, 23))
        self.updateBtn.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.updateBtn.setObjectName("updateBtn")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 20, 241, 31))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Заказчик"))
        self.client.setPlaceholderText(_translate("MainWindow", "Тип техники"))
        self.model.setPlaceholderText(_translate("MainWindow", "Модель"))
        self.opisanie.setPlaceholderText(_translate("MainWindow", "Описание проблемы"))
        self.addBtn.setText(_translate("MainWindow", "Добавить заявку"))
        self.client_2.setPlaceholderText(_translate("MainWindow", "Тип техники"))
        self.opisanie_2.setPlaceholderText(_translate("MainWindow", "Описание проблемы"))
        self.model_2.setPlaceholderText(_translate("MainWindow", "Модель"))
        self.id_column.setPlaceholderText(_translate("MainWindow", "ID Заявки"))
        self.updateBtn.setText(_translate("MainWindow", "Обновить данные по ID"))
        self.pushButton.setText(_translate("MainWindow", "Открыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
