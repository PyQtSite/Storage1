from sys import argv

from PyQt5.QtWidgets import QComboBox, QLineEdit, QListWidget, QCheckBox, QListWidgetItem, QApplication, QWidget


# 这个不带全选功能
class ComboCheckBox(QComboBox):
    def __init__(self, items, parent=None):  # items==[str,str...]
        super(ComboCheckBox, self).__init__(parent)
        self.items = items
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        qListWidget = QListWidget()

        self.row_num = len(self.items)
        for i in range(self.row_num):
            self.qCheckBox.append(QCheckBox())
            qItem = QListWidgetItem(qListWidget)
            self.qCheckBox[i].setText(self.items[i])
            qListWidget.setItemWidget(qItem, self.qCheckBox[i])
            self.qCheckBox[i].stateChanged.connect(self.show)

        self.setLineEdit(self.qLineEdit)
        self.setModel(qListWidget.model())
        self.setView(qListWidget)

    def Selectlist(self):
        Outputlist = []
        for i in range(self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.qCheckBox[i].text())
        return Outputlist

    def show(self):
        show = ''
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in self.Selectlist():
            show += i + ';'
        self.qLineEdit.setText(show)
        self.qLineEdit.setReadOnly(True)

# 这个带全选功能
class ComboCheckBox2(QComboBox):
    def __init__(self, items, parent=None):  # items==[str,str...]
        super(ComboCheckBox2, self).__init__(parent)
        self.items = items
        self.items.insert(0, '全部')
        self.row_num = len(self.items)
        self.Selectedrow_num = 0
        self.qCheckBox = []
        self.qLineEdit = QLineEdit()
        self.qLineEdit.setReadOnly(True)
        self.qListWidget = QListWidget()
        self.addQCheckBox(0)
        self.qCheckBox[0].stateChanged.connect(self.All)
        for i in range(1, self.row_num):
            self.addQCheckBox(i)
            self.qCheckBox[i].stateChanged.connect(self.show)
        self.setModel(self.qListWidget.model())
        self.setView(self.qListWidget)
        self.setLineEdit(self.qLineEdit)

    def addQCheckBox(self, i):
        self.qCheckBox.append(QCheckBox())
        qItem = QListWidgetItem(self.qListWidget)
        self.qCheckBox[i].setText(self.items[i])
        self.qListWidget.setItemWidget(qItem, self.qCheckBox[i])

    def Selectlist(self):
        Outputlist = []
        for i in range(1, self.row_num):
            if self.qCheckBox[i].isChecked() == True:
                Outputlist.append(self.qCheckBox[i].text())
        self.Selectedrow_num = len(Outputlist)
        return Outputlist

    def show(self):
        show = ''
        Outputlist = self.Selectlist()
        self.qLineEdit.setReadOnly(False)
        self.qLineEdit.clear()
        for i in Outputlist:
            show += i + ';'
        if self.Selectedrow_num == 0:
            self.qCheckBox[0].setCheckState(0)
        elif self.Selectedrow_num == self.row_num - 1:
            self.qCheckBox[0].setCheckState(2)
        else:
            self.qCheckBox[0].setCheckState(1)
        self.qLineEdit.setText(show)
        self.qLineEdit.setReadOnly(True)

    def All(self, zhuangtai):
        if zhuangtai == 2:
            for i in range(1, self.row_num):
                self.qCheckBox[i].setChecked(True)
        elif zhuangtai == 1:
            if self.Selectedrow_num == 0:
                self.qCheckBox[0].setCheckState(2)
        elif zhuangtai == 0:
            self.clear()

    def clear(self):
        for i in range(self.row_num):
            self.qCheckBox[i].setChecked(False)


class MyUi(QWidget):
    def __init__(self):
        super(MyUi, self).__init__()
        self.resize(300, 300)
        # 第一个是不带全选功能，
        self.a = ComboCheckBox(['1', '2'], self)
        self.a.setFixedSize(100, 40)

        # 这个带全选功能
        self.b = ComboCheckBox2(['1', '2'], self)
        self.b.setFixedSize(100, 40)

        self.b.move(120, 0)


if __name__ == '__main__':
    app = QApplication(argv)
    window = MyUi()
    window.show()
    exit(app.exec_())
