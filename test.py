from qt_core import *

class CheckableListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        
        # 创建勾选框来过滤性别
        self.maleCheckBox = QCheckBox("Male", self)
        self.maleCheckBox.stateChanged.connect(self.filterItems)
        self.layout.addWidget(self.maleCheckBox)
        
        self.femaleCheckBox = QCheckBox("Female", self)
        self.femaleCheckBox.stateChanged.connect(self.filterItems)
        self.layout.addWidget(self.femaleCheckBox)
        
        # 创建并填充列表
        self.listWidget = QListWidget(self)
        self.populateList()
        self.layout.addWidget(self.listWidget)

    def populateList(self):
        # 假设的人名和性别数据
        people = [("John", "Male"), ("Jane", "Female"), ("Dave", "Male"), ("Diana", "Female")]
        for name, gender in people:
            item = QListWidgetItem(name)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked)
            item.setData(Qt.UserRole, gender)
            self.listWidget.addItem(item)

    def filterItems(self):
        for index in range(self.listWidget.count()):
            item = self.listWidget.item(index)
            gender = item.data(Qt.UserRole)
            should_show = ((gender == "Male" and self.maleCheckBox.isChecked()) or
                           (gender == "Female" and self.femaleCheckBox.isChecked()))
            self.listWidget.setItemHidden(item, not should_show)

if __name__ == '__main__':
    app = QApplication([])
    window = CheckableListWidget()
    window.show()
    app.exec_()
