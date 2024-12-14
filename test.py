import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)

    mywindow = QWidget()
    mywindow.resize(250, 150)

    mywindow.setWindowTitle('My Window')
    mywindow.show()

    sys.exit(app.exec_())