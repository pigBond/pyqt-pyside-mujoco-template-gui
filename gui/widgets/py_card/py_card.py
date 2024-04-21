# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from gui.widgets import *
from gui.core.functions import *
from gui.uis.cards.ui_py_card import Ui_Card

class PyCard(QWidget):
    def __init__(self,card_info,main_window,parent=None):
        super(PyCard, self).__init__(parent)
        self.ui = Ui_Card()
        self.ui.setupUi(self)
        self.card_info=card_info
        self.main_window=main_window
        self.__initUi()

    def __initUi(self):
        # 设置字体样式和大小
        font = QFont()
        font.setPointSize(3)  # 设置字体大小为8点
        font.setFamily("Arial")  # 可以选择字体样式为Arial
        print(self.card_info)
        for key, value in self.card_info.items():
            name_=""
            if key=="model":
                name_="模型"
            elif key=="algorithm":
                name_="算法"
            elif key=="environment":
                name_="环境"
            elif key=="task":
                name_="任务"
            label = QLabel(f"{name_}: {value}")  # 创建标签，显示key和value
            label.setStyleSheet("QLabel { font-size: 8pt; }")
            self.ui.label_info_layout.addWidget(label)  # 将标签添加到布局中

        self.icon_button_1 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_play.svg"),
            parent = self,
            app_parent = self.main_window.ui.central_widget,
            tooltip_text = "开始",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.main_window.themes["app_color"]["green"],
            icon_color = self.main_window.themes["app_color"]["icon_color"],
            icon_color_hover = self.main_window.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.main_window.themes["app_color"]["white"],
            icon_color_active = self.main_window.themes["app_color"]["icon_active"],
            bg_color = self.main_window.themes["app_color"]["blue"],
            bg_color_hover = self.main_window.themes["app_color"]["dark_three"],
            bg_color_pressed = self.main_window.themes["app_color"]["green"],
        )

        self.icon_button_2 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_replay.svg"),
            parent = self,
            app_parent = self.main_window.ui.central_widget,
            tooltip_text = "重新播放",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.main_window.themes["app_color"]["green"],
            icon_color = self.main_window.themes["app_color"]["icon_color"],
            icon_color_hover = self.main_window.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.main_window.themes["app_color"]["white"],
            icon_color_active = self.main_window.themes["app_color"]["icon_active"],
            bg_color = self.main_window.themes["app_color"]["light_green"],
            bg_color_hover = self.main_window.themes["app_color"]["dark_three"],
            bg_color_pressed = self.main_window.themes["app_color"]["green"],
        )
        self.icon_button_3 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_delete.svg"),
            parent = self,
            app_parent = self.main_window.ui.central_widget,
            tooltip_text = "关闭",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.main_window.themes["app_color"]["green"],
            icon_color = self.main_window.themes["app_color"]["icon_color"],
            icon_color_hover = self.main_window.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.main_window.themes["app_color"]["white"],
            icon_color_active = self.main_window.themes["app_color"]["icon_active"],
            bg_color = self.main_window.themes["app_color"]["red"],
            bg_color_hover = self.main_window.themes["app_color"]["dark_three"],
            bg_color_pressed = self.main_window.themes["app_color"]["green"],
        )

        self.ui.btn_operation_layout.addWidget(self.icon_button_1)
        self.ui.btn_operation_layout.addWidget(self.icon_button_2)
        self.ui.btn_operation_layout.addWidget(self.icon_button_3)

        # 绑定按钮点击事件到关闭窗口的方法
        self.icon_button_1.clicked.connect(self.playModel)
        self.icon_button_2.clicked.connect(self.replayModel)
        self.icon_button_3.clicked.connect(self.closeParentWindow)

    def playModel(self):
        print("开始播放")
    
    def replayModel(self):
        print("重复播放")

    def closeParentWindow(self):
        # 访问 parent() 返回的是设置的 widget 所在的 QMdiSubWindow
        reply = QMessageBox.question(
            self,
            "确认操作",
            "是否删除？选择是或否",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.parent().close()
        else:
            print("操作取消")

