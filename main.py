import sys
import os
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.textEdit = QtWidgets.QTextEdit()
        self.listWidget = QtWidgets.QListWidget()

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.textEdit)
        vbox.addWidget(self.listWidget)

        self.select_ws()
        self.process()

    def select_ws(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбери директорию")

        # name_ship = input('Введите название судна')

        self.textEdit.setPlainText(self.dir)
        if self.dir:
            for root, dirs, files in os.walk(self.dir):
                for file_name in files:
                    if file_name.endswith(".png"):  # !!! установите свое ".ws"

                        path = os.path.join(root, file_name)  # !!! +++
                        #                        self.listWidget.addItem(file_name)
                        self.listWidget.addItem(path)  # !!! +++

    # Изменить в функции поиск. Необходимо выводить список папок, содержащих переменную
    def process(self):
        list_item = [self.listWidget.item(row).text() for row in range(self.listWidget.count())]
        # print(*list_item, sep='\n')

        data = pd.DataFrame(dict(
            Путь=[self.dir],
            Список=[list_item]))
        print(data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
