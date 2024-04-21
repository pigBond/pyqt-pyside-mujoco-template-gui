from qt_core import *
from .multiCheckBoxListWidget import MultiCheckBoxListWidget
from gui.widgets import *


class PyMultiCheck(QWidget):
    def __init__(self,main_window,json_data):
        super().__init__()
        self.main_window=main_window
        self.filterConditions = {
            "algorithm": None,
            "environment": None,
            "task": None,
        }  # 定义筛选条件的字典
        self.multiCheckBoxListWidget = None

        self.jsonData = json_data
        self.__initUi()

    def updateFilterConditions(self, algorithm=None, environment=None, task=None):
        print("切换--", algorithm, "--", environment, "--", task)
        if algorithm is not None:
            if self.filterConditions["algorithm"] is None:
                self.filterConditions["algorithm"] = [algorithm]
            else:
                if algorithm in self.filterConditions["algorithm"]:
                    self.filterConditions["algorithm"].remove(algorithm)
                else:
                    self.filterConditions["algorithm"].append(algorithm)
        else:
            self.filterConditions["algorithm"] = None

        if environment is not None:
            if self.filterConditions["environment"] is None:
                self.filterConditions["environment"] = [environment]
            else:
                if environment in self.filterConditions["environment"]:
                    self.filterConditions["environment"].remove(environment)
                else:
                    self.filterConditions["environment"].append(environment)
        else:
            self.filterConditions["environment"] = None

        if task is not None:
            if self.filterConditions["task"] is None:
                self.filterConditions["task"] = [task]
            else:
                if task in self.filterConditions["task"]:
                    self.filterConditions["task"].remove(task)
                else:
                    self.filterConditions["task"].append(task)
        else:
            self.filterConditions["task"] = None

        print("筛选字典 = ", self.filterConditions)
        # 应用当前的筛选条件
        self.multiCheckBoxListWidget.filterItems(
            algorithm=self.filterConditions["algorithm"],
            environment=self.filterConditions["environment"],
            task=self.filterConditions["task"],
        )

    def __initUi(self):

        # -------------------------------------复选框------------------------------------------------------
        # 全选复选框
        allCheckBox = QCheckBox("Check all")
        # 算法筛选复选框
        algorithmCheckBoxes = []
        for algorithm in set(item["algorithm"] for item in self.jsonData):
            checkBox = QCheckBox(algorithm)
            checkBox.stateChanged.connect(
                lambda state, algo=algorithm: self.updateFilterConditions(
                    algorithm=algo if state == 2 else None,
                    environment=self.filterConditions["environment"],
                    task=self.filterConditions["task"],
                )
            )
            algorithmCheckBoxes.append(checkBox)

        # 环境筛选复选框
        environmentCheckBoxes = []
        for environment in set(item["environment"] for item in self.jsonData):
            checkBox = QCheckBox(environment)
            checkBox.stateChanged.connect(
                lambda state, env=environment: self.updateFilterConditions(
                    algorithm=self.filterConditions["algorithm"],
                    environment=env if state == 2 else None,
                    task=self.filterConditions["task"],
                )
            )
            environmentCheckBoxes.append(checkBox)

        # 任务筛选复选框
        taskCheckBoxes = []
        for task in set(item["task"] for item in self.jsonData):
            checkBox = QCheckBox(task)
            checkBox.stateChanged.connect(
                lambda state, t=task: self.updateFilterConditions(
                    algorithm=self.filterConditions["algorithm"],
                    environment=self.filterConditions["environment"],
                    task=t if state == 2 else None,
                )
            )
            taskCheckBoxes.append(checkBox)
        # ----------------------------------------------------------------------------------------------

        # 测试输出代码
        getAllChecked_btn = QPushButton("Get Checked")
        unCheckAll_btn = QPushButton("Uncheck ALl")
        deleteAllCard_btn = QPushButton("Delete ALl")

        self.multiCheckBoxListWidget = MultiCheckBoxListWidget()

        self.multiCheckBoxListWidget.addItems(self.jsonData)

        # -------------------------------------按钮click------------------------------------------------------
        def on_button_2_clicked():
            allCheckBox.setCheckState(Qt.Unchecked)
            for checkBox in (
                algorithmCheckBoxes + environmentCheckBoxes + taskCheckBoxes
            ):
                checkBox.setCheckState(Qt.Unchecked)
            self.multiCheckBoxListWidget.uncheckAllRows()

        def on_button_clicked():
            self.confirmAction()

        def closeAllSubWindows():
            allCheckBox.setCheckState(Qt.Unchecked)
            # 获取MDI区域内的所有子窗口
            subWindows = self.main_window.ui.load_pages.mdiArea_show.subWindowList()
            
            # 遍历所有子窗口并关闭它们
            for window in subWindows:
                window.close()

        getAllChecked_btn.clicked.connect(on_button_clicked)
        unCheckAll_btn.clicked.connect(on_button_2_clicked)
        deleteAllCard_btn.clicked.connect(closeAllSubWindows)
        # ---------------------------------------------------------------------------------------------------

        # # 连接全选复选框的状态变化信号到相应的槽函数
        # allCheckBox.stateChanged.connect(
        #     lambda state: self.multiCheckBoxListWidget.toggleState(state)
        # )
        def allCheckBox_changed():
            if allCheckBox.isChecked():
                self.multiCheckBoxListWidget.checkAllRows()
            else:
                self.multiCheckBoxListWidget.uncheckAllRows()

        # 连接全选复选框的状态变化信号到相应的槽函数
        allCheckBox.stateChanged.connect(allCheckBox_changed)

        self.multiCheckBoxListWidget.getAllItems()

        # 布局设置
        lay = QGridLayout()
        lay.addWidget(allCheckBox, 0, 0, 1, 3)  # 全选复选框跨三列

        self.addSeparator(lay, 1)  # 在全选复选框和算法标签之间添加分界线

        # 为算法复选框添加标签
        algorithmLabel = QLabel("算法")
        lay.addWidget(algorithmLabel, 2, 0, 1, 3)  # 标签跨三列
        self.addCheckBoxesInGrid(algorithmCheckBoxes, lay, 3, 3)  # 算法类开始于第4行

        self.addSeparator(lay, 10)  # 添加分界线
        # 为环境复选框添加标签
        environmentLabel = QLabel("环境")
        lay.addWidget(environmentLabel, 11, 0, 1, 3)  # 标签跨三列
        self.addCheckBoxesInGrid(environmentCheckBoxes, lay, 12, 3)  # 环境类

        self.addSeparator(lay, 20)  # 再次添加分界线
        # 为任务复选框添加标签
        taskLabel = QLabel("任务")
        lay.addWidget(taskLabel, 21, 0, 1, 3)  # 标签跨三列
        self.addCheckBoxesInGrid(taskCheckBoxes, lay, 22, 3)  # 任务类

        lay.addWidget(self.multiCheckBoxListWidget, 30, 0, 1, 3)  # 列表控件跨三列
        lay.addWidget(getAllChecked_btn, 31, 0)
        lay.addWidget(unCheckAll_btn, 31, 1)
        lay.addWidget(deleteAllCard_btn, 31, 2)

        # 设置列间的水平间距
        lay.setHorizontalSpacing(10)  # 这里的10可以根据实际需要进行调整

        self.setLayout(lay)

    def addCheckBoxesInGrid(self, checkBoxes, layout, start_row, items_per_row):
        row = start_row
        column = 0
        for index, checkBox in enumerate(checkBoxes):
            layout.addWidget(checkBox, row, column)
            column += 1
            if (index + 1) % items_per_row == 0:
                row += 1
                column = 0

    def addSeparator(self, layout, row):
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator, row, 0, 1, 3)  # 分界线跨三列

    def getAllChecked_btn_function(self):
        # checked_data = self.multiCheckBoxListWidget.getCheckedItemsData()
        checked_data = self.multiCheckBoxListWidget.getCheckedRows()
        print("Checked items:", checked_data)
        for i in checked_data:
            # print("-- ", self.jsonData[i])
            self.addCard(self.jsonData[i])

    def confirmAction(self):
        reply = QMessageBox.question(
            self,
            "确认操作",
            "是否输出？选择是或否",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.getAllChecked_btn_function()
        else:
            print("操作取消")

    # TODO：这里需要传入card需要展示的信息，使用数据列表循环使用addCard一次性添加多个窗口
    def addCard(self,card_info):
        # print("card_info = ",card_info)
        subWindow = QMdiSubWindow()
        subWindow.setWindowTitle(f"模型：{card_info['model']}")
        # subWindow.resize(250, 250)
        subWindow.setFixedSize(310, 250)
        py_card = PyCard(card_info,self.main_window)
        subWindow.setWidget(py_card)
        # 将子窗口添加到MDI区域
        self.main_window.ui.load_pages.mdiArea_show.addSubWindow(subWindow)
        subWindow.show()

