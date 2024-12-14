from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets  import (QTabWidget, QStackedWidget)
import sqlite3
import login
import client
from enum import Enum
import datetime
import master

class Status(Enum):

    NEW = 'Новая заявка'
    PROCESS = "В процессе ремонта"
    GREEN = 'Готова к выдаче'

def connect_to_db():
    import sqlite3
    cx = sqlite3.connect("zyv.db")
    return cx

class Login(QtWidgets.QMainWindow, login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.authBtn.clicked.connect(self.auth)

    def auth(self):
        db = connect_to_db()
        login = self.login.text()
        password = self.password.text()

        cursor = db.cursor()
        cursor.execute("SELECT userID, type, fio, phone FROM users WHERE login = ? AND password = ?", (login, password))

        requests = cursor.fetchone()

        if  requests[1] == "Заказчик":
            self.open_window = Client(requests[0], requests[2], requests[3])
            self.open_window.show()
            self.close()

        if requests[1] == "Мастер":
            self.open_window = Master(requests[0], requests[2], requests[3])
            self.open_window.show()
            self.close()




class Client(QtWidgets.QMainWindow, client.Ui_MainWindow):
    def __init__(self, id, fio, phone):
        super().__init__()
        self.setupUi(self)

        self.id =  id
        self.fio = fio
        self.phone = phone

        self.label_2.setText(fio)

        self.pushButton.clicked.connect(self.open_data)
        self.addBtn.clicked.connect(self.add_data)
        self.updateBtn.clicked.connect(self.update_data)


    def open_data(self):

        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM requests WHERE clientID = {self.id}")
        requests = cursor.fetchall()

        self.tableWidget.setColumnCount(len(requests[0]))
        column_header = [desc[0] for desc in cursor.description]
        self.tableWidget.setHorizontalHeaderLabels(column_header)

        self.tableWidget.setRowCount(len(requests))

        for row_id, request in enumerate(requests):
            for col_id, value in enumerate(request):
                self.tableWidget.setItem(row_id, col_id, QtWidgets.QTableWidgetItem(str(value)))


    def add_data(self):


        date = datetime.date.today()
        type_org = self.client.text()
        model = self.model.text()
        problem = self.opisanie.text()
        status = Status.NEW.value
        end_date = 'None'
        repair = 'None'
        master = 'None'


        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("insert into requests (startDate, orgTechType, orgTechModel, problemDescryption, requestStatus, completionDate, repairParts, masterID, clientID) values (?,?,?,?,?,?,?,?,?)", (date,type_org,model,problem,status,end_date,repair,master, self.id))

        db.commit()
        db.close()



    def update_data(self):

        where_id = self.id_column.text()
        type_org = self.client_2.text()
        model = self.model_2.text()
        problem = self.opisanie.text()



        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("UPDATE requests SET orgTechType = ?, orgTechModel = ?, problemDescryption = ? WHERE requestID = ?", (type_org, model, problem, where_id))

        db.commit()
        db.close()


class Master(QtWidgets.QMainWindow, master.Ui_MainWindow):
    def __init__(self, id, fio, phone):
        super().__init__()
        self.setupUi(self)
        self.label_2.setText(fio)
        self.pushButton.clicked.connect(self.open_data)
        self.updateBtn.clicked.connect(self.update_data)
        self.id = id

    def open_data(self):

        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM requests WHERE masterID = {self.id}")
        requests = cursor.fetchall()

        self.tableWidget.setColumnCount(len(requests[0]))
        column_header = [desc[0] for desc in cursor.description]
        self.tableWidget.setHorizontalHeaderLabels(column_header)

        self.tableWidget.setRowCount(len(requests))

        for row_id, request in enumerate(requests):
            for col_id, value in enumerate(request):
                self.tableWidget.setItem(row_id, col_id, QtWidgets.QTableWidgetItem(str(value)))
    def update_data(self):

        where_id = self.id_column.text()
        type_org = self.client_2.text()
        model = self.model_2.text()
        problem = self.opisanie_2.text()



        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("UPDATE requests SET requestStatus = ?, completionDate = ?, repairParts = ? WHERE requestID = ?", (type_org, model, problem, where_id))

        db.commit()
        db.close()

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())

