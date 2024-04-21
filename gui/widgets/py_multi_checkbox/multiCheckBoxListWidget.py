from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QListWidget, QListWidgetItem

class MultiCheckBoxListWidget(QListWidget):
    checkedSignal = Signal(int, Qt.CheckState)

    def __init__(self):
        super().__init__()
        self.itemChanged.connect(self.__sendCheckedSignal)

    def __sendCheckedSignal(self, item):
        r_idx = self.row(item)
        state = item.checkState()
        self.checkedSignal.emit(r_idx, state)

    def addItems(self, items) -> None:
        for item in items:
            self.addItem(item)

    def addItem(self, item) -> None:
        if isinstance(item, dict):
            model = item.get("model", "")
            algorithm = item.get("algorithm", "")
            environment = item.get("environment", "")
            task = item.get("task", "")
            item_text = f"{model}:  {algorithm} - {environment} - {task}"
            item = QListWidgetItem(item_text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            item.setData(Qt.UserRole, {
                "model": model,
                "algorithm": algorithm,
                "environment": environment,
                "task": task
            })
            super().addItem(item)

    def toggleState(self, state):
        for i in range(self.count()):
            item = self.item(i)
            if item.checkState() != state:
                item.setCheckState(state)

    def filterItems(self, algorithm=None, environment=None, task=None):
        for i in range(self.count()):
            item = self.item(i)
            item_data = item.data(Qt.UserRole)
            match_algorithm = algorithm is None or item_data.get("algorithm") in algorithm
            match_environment = environment is None or item_data.get("environment") in environment
            match_task = task is None or item_data.get("task") in task
            item.setHidden(not (match_algorithm and match_environment and match_task))

    def getAllItems(self):
        print("----------------------------------------")
        for i in range(self.count()):
            item = self.item(i)
            print(item.data(Qt.UserRole))
        print("----------------------------------------")

    def uncheckAllRows(self):
        for i in range(self.count()):
            item = self.item(i)
            item.setCheckState(Qt.Unchecked)

    def checkAllRows(self):
        for i in range(self.count()):
            item = self.item(i)
            item.setCheckState(Qt.Checked)

    def getCheckedRows(self):
        return self.__getFlagRows(Qt.Checked)

    def getUncheckedRows(self):
        return self.__getFlagRows(Qt.Unchecked)

    def __getFlagRows(self, flag: Qt.CheckState):
        flag_lst = []
        for i in range(self.count()):
            item = self.item(i)
            if item.checkState() == flag:
                flag_lst.append(i)
        return flag_lst

    def removeCheckedRows(self):
        self.__removeFlagRows(Qt.Checked)

    def removeUncheckedRows(self):
        self.__removeFlagRows(Qt.Unchecked)

    def __removeFlagRows(self, flag):
        flag_lst = self.__getFlagRows(flag)
        flag_lst = reversed(flag_lst)
        for i in flag_lst:
            self.takeItem(i)
