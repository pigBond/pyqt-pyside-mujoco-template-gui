# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_columnDnLLEw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *



class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(243, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.btn_1_widget = QWidget(self.menu_1)
        self.btn_1_widget.setObjectName(u"btn_1_widget")
        self.btn_1_widget.setMinimumSize(QSize(0, 40))
        self.btn_1_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_1_layout = QVBoxLayout(self.btn_1_widget)
        self.btn_1_layout.setSpacing(0)
        self.btn_1_layout.setObjectName(u"btn_1_layout")
        self.btn_1_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_1_widget)

        self.btn_2_widget = QWidget(self.menu_1)
        self.btn_2_widget.setObjectName(u"btn_2_widget")
        self.btn_2_widget.setMinimumSize(QSize(0, 40))
        self.btn_2_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_2_layout = QVBoxLayout(self.btn_2_widget)
        self.btn_2_layout.setSpacing(0)
        self.btn_2_layout.setObjectName(u"btn_2_layout")
        self.btn_2_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_2_widget)

        self.default_button = QPushButton(self.menu_1)
        self.default_button.setObjectName(u"default_button")
        self.default_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout.addWidget(self.default_button)

        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btn_4_widget = QWidget(self.menu_2)
        self.btn_4_widget.setObjectName(u"btn_4_widget")
        self.btn_4_widget.setMinimumSize(QSize(0, 40))
        self.btn_4_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_4_layout = QVBoxLayout(self.btn_4_widget)
        self.btn_4_layout.setSpacing(0)
        self.btn_4_layout.setObjectName(u"btn_4_layout")
        self.btn_4_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_4_widget)

        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.menu_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font-size: 9pt")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.menus.addWidget(self.menu_2)
        self.menu_train = QWidget()
        self.menu_train.setObjectName(u"menu_train")
        self.verticalLayout_3 = QVBoxLayout(self.menu_train)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.menu_train)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)

        self.verticalLayout_3.addWidget(self.label)

        self.menus.addWidget(self.menu_train)
        self.menu_show = QWidget()
        self.menu_show.setObjectName(u"menu_show")
        self.verticalLayout_4 = QVBoxLayout(self.menu_show)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_show = QGridLayout()
        self.gridLayout_show.setObjectName(u"gridLayout_show")

        self.verticalLayout_4.addLayout(self.gridLayout_show)

        self.testButton = QPushButton(self.menu_show)
        self.testButton.setObjectName(u"testButton")

        self.verticalLayout_4.addWidget(self.testButton)

        self.menus.addWidget(self.menu_show)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.default_button.setText(QCoreApplication.translate("LeftColumn", u"Default Button", None))
        self.label_1.setText(QCoreApplication.translate("LeftColumn", u"Menu 1 - Left Menu", None))
        self.label_2.setText(QCoreApplication.translate("LeftColumn", u"Menu 2 - Left Menu", None))
        self.label_3.setText(QCoreApplication.translate("LeftColumn", u"This is just an example menu.\n"
"Add Qt Widgets or your custom widgets here.", None))
        self.label.setText(QCoreApplication.translate("LeftColumn", u"\u8fd9\u91cc\u662f menu.train \u7684\u8bad\u7ec3\u53c2\u6570", None))
        self.testButton.setText(QCoreApplication.translate("LeftColumn", u"testButton", None))
    # retranslateUi

