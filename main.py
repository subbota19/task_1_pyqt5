import sys
import os

from PyQt5 import QtWidgets

import bus_timetable


class ExampleApp(QtWidgets.QMainWindow, bus_timetable.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.open_file)
        self.pushButton_3.clicked.connect(self.sort_text)
        self.pushButton_4.clicked.connect(self.save_file)
        self.pushButton.clicked.connect(self.create_file)
        self.pushButton_6.clicked.connect(self.enter_data)
        self.pushButton_5.clicked.connect(sys.exit)

    def create_file(self):
        self.textEdit.clear()
        self.pushButton_6.setEnabled(True)

    def sort_text(self):
        list_with_item = [item.split() for item in self.textEdit.toPlainText().split("\n")]
        list_with_item.sort(key=lambda i: eval(i[0]))
        self.textEdit.clear()
        for i in list_with_item:
            self.textEdit.append(' '.join(i))

    def save_file(self):
        file = open(QtWidgets.QFileDialog.getSaveFileName(self, "Choice directory")[0], 'w')
        for text in self.textEdit.toPlainText():
            file.write(text)
        file.close()

    def open_file(self):
        self.pushButton_6.setEnabled(True)
        self.textEdit.clear()
        file = open(QtWidgets.QFileDialog.getOpenFileName(self, "Choice directory")[0], 'r')
        try:
            self.textEdit.append(file.read())
        except:
            file.close()

    def enter_data(self):

        self.textEdit.append(self.lineEdit.text() + " " + self.lineEdit_2.text() +
                             " " + self.lineEdit_3.text() + " " + self.lineEdit_4.text() + " " + self.lineEdit_5.text())
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
