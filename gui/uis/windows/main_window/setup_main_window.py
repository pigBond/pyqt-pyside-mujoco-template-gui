# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

from gui.uis.cards.ui_py_card import Ui_Card 

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
                {
            "btn_icon" : "icon_send.svg",
            "btn_id" : "btn_train_page",
            "btn_text" : "训练",
            "btn_tooltip" : "训练",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_emoticons.svg",
            "btn_id" : "btn_show_page",
            "btn_text" : "展示",
            "btn_tooltip" : "展示",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_save.svg",
            "btn_id" : "btn_evaluate_page",
            "btn_text" : "评估",
            "btn_tooltip" : "评估",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_menu_2",
            "btn_text" : "menu 2",
            "btn_tooltip" : "menu 2",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "设置",
            "btn_tooltip" : "Open Settings",
            "show_top" : False,
            "is_active" : False
        },
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_home)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # TODO:这里是后面可以用的代码
        # show部分----------------------------------------------------------------------
        # page show
        # def addCard():
        #     subWindow = QMdiSubWindow()
        #     subWindow.setWindowTitle(f"子窗口 {1}")
        #     subWindow.resize(350, 350)
        #     # ui_card = Ui_Card()
        #     # widget = QWidget()
        #     # ui_card.setupUi(widget)
        #     # subWindow.setWidget(widget)
        #     py_card=PyCard()
        #     subWindow.setWidget(py_card)
        #     # 将子窗口添加到MDI区域
        #     self.ui.load_pages.mdiArea_show.addSubWindow(subWindow)
        #     subWindow.show()

        # left_column
        # self.ui.left_column.menus.testButton.clicked.connect(addCard)
        #-------------------------------------------------------------------------------


        # TODO：添加好看的按钮
        # ADD CUSTOM BUTTON
        self.btn_1 = PyPushButton(
            text="Btn_1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["pink"],
        )
        self.btn_1.setMaximumHeight(40)
        # ADD TO LAYOUT
        # self.ui.left_column.menus.btn_1_layout.addWidget(self.btn_1)


        # ICON BUTTON 2
        self.icon_button_2 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN with tooltip",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["green"],
        )
        # self.ui.left_column.menus.btn_1_layout.addWidget(self.icon_button_2)



        #////////////////////////////////////////////////////////////////////////


        # ADD TOGGLE BUTTON
        self.toggle_1=PyToggle(
            active_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["dark_one"],
            circle_color=self.themes["app_color"]["icon_color"],
            width=50
        )

        # ADD TO LAYOUT
        self.ui.left_column.menus.btn_2_layout.addWidget(self.toggle_1,Qt.AlignCenter,Qt.AlignCenter)

        # ADD LOGO TO HOME
        self.logo=QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        # ADD TO LAYOUT
       # self.ui.load_pages.logo_layout.addWidget(self.logo,Qt.AlignCenter,Qt.AlignCenter)


        # ADD DEFAULY WIDGET
        self.line_edit=QLineEdit()
        self.button=QPushButton("Send")

        def print_text():
            print(self.line_edit.text())
            self.line_edit.setText("")

        self.button.clicked.connect(print_text)
        self.ui.load_pages.logo_layout.addWidget(self.line_edit)
        self.ui.load_pages.logo_layout.addWidget(self.button)


        # PAGE WINDOW
        # page train

        #page evaluate
        
        #SHOW部分
        # ///////////////////////////////////////////////////////////////
        json_data=[
            {
                "model": "A1_run_on_B1",
                "algorithm": "A1",
                "environment": "B1",
                "task": "run",
            },
            {
                "model": "A2_run_on_B1",
                "algorithm": "A2",
                "environment": "B1",
                "task": "run",
            },
            {
                "model": "A1_run_on_B2",
                "algorithm": "A1",
                "environment": "B2",
                "task": "run",
            },
            {
                "model": "X2_run_on_Y2",
                "algorithm": "X2",
                "environment": "Y2",
                "task": "run",
            },
            {
                "model": "Z3_walk_on_W3",
                "algorithm": "Z3",
                "environment": "W3",
                "task": "walk",
            },
            {
                "model": "V4_run_on_U4",
                "algorithm": "V4",
                "environment": "U4",
                "task": "run",
            },
        ]

        self.multiCheckbox_show=PyMultiCheck(self,json_data)
        self.ui.left_column.menus.gridLayout_show.addWidget(self.multiCheckbox_show)


        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)